import unittest
import csv
import os
from pais import Pais
from estudiante import Estudiante
from resumen import Resumen


class TestPais(unittest.TestCase):
    """Tests de unidad para la clase Pais."""
    
    def setUp(self):
        """Configuración inicial para los tests."""
        # Usar el archivo de test que creamos
        self.archivo_test = "test_datos.csv"
        self.pais = Pais(self.archivo_test)
    
    def test_constructor_y_tamano(self):
        """Test del constructor y método tamano()."""
        self.assertEqual(self.pais.tamano(), 6)  # 6 estudiantes en test_datos.csv
        
        # Verificar que el tamaño sea O(1)
        import time
        start = time.time()
        for _ in range(1000):
            _ = self.pais.tamano()
        end = time.time()
        # Debería ser muy rápido (mucho menos de 1 segundo para 1000 llamadas)
        self.assertLess(end - start, 1.0)
    
    def test_provincias(self):
        """Test del atributo provincias."""
        expected_provincias = {"MZA", "BA", "COR"}
        self.assertEqual(self.pais.provincias, expected_provincias)
    
    def test_resumen_provincia(self):
        """Test del método resumen_provincia()."""
        # Test para MZA (2 estudiantes)
        resumen_mza = self.pais.resumen_provincia("MZA")
        self.assertEqual(resumen_mza.cantidad, 2)
        # Promedio matemática MZA: (466.76 + 455.47) / 2 = 461.115
        self.assertAlmostEqual(resumen_mza.promedio_matematica, 461.115, places=2)
        # Promedio lengua MZA: (550.31 + 527.25) / 2 = 538.78
        self.assertAlmostEqual(resumen_mza.promedio_lengua, 538.78, places=2)
        # Ambos son urbanos (proporción rural = 0)
        self.assertEqual(resumen_mza.proporcion_ambito_rural, 0.0)
        # Ambos son estatales (proporción estatal = 1)
        self.assertEqual(resumen_mza.proporcion_sector_estatal, 1.0)
        
        # Test para BA (2 estudiantes)
        resumen_ba = self.pais.resumen_provincia("BA")
        self.assertEqual(resumen_ba.cantidad, 2)
        # Ambos son rurales (proporción rural = 1)
        self.assertEqual(resumen_ba.proporcion_ambito_rural, 1.0)
        # 1 privado, 1 estatal (proporción estatal = 0.5)
        self.assertEqual(resumen_ba.proporcion_sector_estatal, 0.5)
        
        # Test para COR (2 estudiantes)
        resumen_cor = self.pais.resumen_provincia("COR")
        self.assertEqual(resumen_cor.cantidad, 2)
        # Ambos son urbanos (proporción rural = 0)
        self.assertEqual(resumen_cor.proporcion_ambito_rural, 0.0)
        # 1 estatal, 1 privado (proporción estatal = 0.5)
        self.assertEqual(resumen_cor.proporcion_sector_estatal, 0.5)
    
    def test_resumen_provincia_inexistente(self):
        """Test del método resumen_provincia() con provincia inexistente."""
        resumen = self.pais.resumen_provincia("XXX")
        self.assertEqual(resumen.cantidad, 0)
        self.assertEqual(resumen.promedio_matematica, 0.0)
        self.assertEqual(resumen.promedio_lengua, 0.0)
        self.assertEqual(resumen.promedio_nse, 0.0)
        self.assertEqual(resumen.proporcion_ambito_rural, 0.0)
        self.assertEqual(resumen.proporcion_sector_estatal, 0.0)
    
    def test_resumenes_pais(self):
        """Test del método resumenes_pais()."""
        resumenes = self.pais.resumenes_pais()
        
        # Debe tener resúmenes para las 3 provincias
        self.assertEqual(len(resumenes), 3)
        self.assertIn("MZA", resumenes)
        self.assertIn("BA", resumenes)
        self.assertIn("COR", resumenes)
        
        # Verificar que los resúmenes sean correctos
        self.assertEqual(resumenes["MZA"].cantidad, 2)
        self.assertEqual(resumenes["BA"].cantidad, 2)
        self.assertEqual(resumenes["COR"].cantidad, 2)
    
    def test_estudiantes_en_intervalo_matematica(self):
        """Test del método estudiantes_en_intervalo() para matemática."""
        provincias = {"MZA", "BA"}
        
        # Contar estudiantes con puntaje matemática entre 450 y 500
        count = self.pais.estudiantes_en_intervalo("mat", 450.0, 500.0, provincias)
        # En MZA: 466.76 (incluido), 455.47 (incluido) = 2
        # En BA: 449.16 (no incluido < 450), 444.71 (no incluido < 450) = 0
        # Total: 2
        self.assertEqual(count, 2)
        
        # Contar estudiantes con puntaje matemática entre 400 y 450
        count2 = self.pais.estudiantes_en_intervalo("mat", 400.0, 450.0, provincias)
        # En MZA: ninguno (ambos >= 450)
        # En BA: 449.16 (incluido), 444.71 (incluido) = 2
        # Total: 2
        self.assertEqual(count2, 2)
    
    def test_estudiantes_en_intervalo_lengua(self):
        """Test del método estudiantes_en_intervalo() para lengua."""
        provincias = {"MZA"}
        
        # Contar estudiantes con puntaje lengua entre 500 y 600
        count = self.pais.estudiantes_en_intervalo("len", 500.0, 600.0, provincias)
        # En MZA: 550.31 (incluido), 527.25 (incluido) = 2
        self.assertEqual(count, 2)
    
    def test_estudiantes_en_intervalo_nse(self):
        """Test del método estudiantes_en_intervalo() para NSE."""
        provincias = {"BA", "COR"}
        
        # Contar estudiantes con NSE entre -1.0 y 0.0
        count = self.pais.estudiantes_en_intervalo("nse", -1.0, 0.0, provincias)
        # En BA: NSE 0.597 y 0.926 (ambos fuera del intervalo) = 0
        # En COR: NSE 0.150 (fuera) y -0.250 (incluido) = 1
        # Total: 1
        self.assertEqual(count, 1)
    
    def test_estudiantes_en_intervalo_provincia_inexistente(self):
        """Test del método estudiantes_en_intervalo() con provincia inexistente."""
        provincias = {"XXX"}
        count = self.pais.estudiantes_en_intervalo("mat", 0.0, 1000.0, provincias)
        self.assertEqual(count, 0)
    
    def test_exportar_por_provincias(self):
        """Test del método exportar_por_provincias()."""
        archivo_salida = "test_export.csv"
        provincias = {"MZA", "BA"}
        
        try:
            self.pais.exportar_por_provincias(archivo_salida, provincias)
            
            # Verificar que el archivo se creó
            self.assertTrue(os.path.exists(archivo_salida))
            
            # Leer y verificar el contenido del archivo
            with open(archivo_salida, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                
                # Debe tener 2 filas (MZA y BA)
                self.assertEqual(len(rows), 2)
                
                # Verificar las columnas
                expected_columns = ['provincia', 'cantidad', 'promedio_matematica', 'promedio_lengua', 
                                  'promedio_nse', 'proporcion_ambito_rural', 'proporcion_sector_estatal']
                self.assertEqual(list(rows[0].keys()), expected_columns)
                
                # Verificar que las provincias están presentes
                provincias_en_archivo = {row['provincia'] for row in rows}
                self.assertEqual(provincias_en_archivo, {"MZA", "BA"})
                
                # Verificar algunos valores específicos
                for row in rows:
                    if row['provincia'] == 'MZA':
                        self.assertEqual(row['cantidad'], '2')
                        self.assertEqual(row['proporcion_ambito_rural'], '0.0')
                        self.assertEqual(row['proporcion_sector_estatal'], '1.0')
                    elif row['provincia'] == 'BA':
                        self.assertEqual(row['cantidad'], '2')
                        self.assertEqual(row['proporcion_ambito_rural'], '1.0')
                        self.assertEqual(row['proporcion_sector_estatal'], '0.5')
        
        finally:
            # Limpiar archivo de test
            if os.path.exists(archivo_salida):
                os.remove(archivo_salida)
    
    def test_archivo_csv_vacio(self):
        """Test con archivo CSV vacío."""
        # Crear archivo CSV solo con header
        archivo_vacio = "test_vacio.csv"
        try:
            with open(archivo_vacio, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['provincia', 'seccion', 'idalumno', 'sector', 'ambito', 
                               'ldesemp', 'mdesemp', 'lpuntaje', 'mpuntaje', 'NSE_puntaje',
                               'NSE_nivel', 'edadA_junio2023', 'migracion', 'sobreedad',
                               'Nivel_Ed_Madre', 'Nivel_Ed_Padre', 'region', 'clima_escolar'])
            
            pais_vacio = Pais(archivo_vacio)
            self.assertEqual(pais_vacio.tamano(), 0)
            self.assertEqual(len(pais_vacio.provincias), 0)
            
        finally:
            if os.path.exists(archivo_vacio):
                os.remove(archivo_vacio)


if __name__ == '__main__':
    unittest.main() 