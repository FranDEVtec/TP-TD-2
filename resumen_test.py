import unittest
from estudiante import Estudiante
from resumen import Resumen


class TestResumen(unittest.TestCase):
    """Tests de unidad para la clase Resumen."""
    
    def setUp(self):
        """Configuración inicial para los tests."""
        # Crear estudiantes de prueba
        self.est1 = Estudiante("MZA", 500.0, 400.0, 0.5, "rural", "estatal")
        self.est2 = Estudiante("MZA", 600.0, 500.0, -0.5, "urbano", "privado")
        self.est3 = Estudiante("BA", 400.0, 300.0, 1.0, "rural", "estatal")
        self.est4 = Estudiante("BA", 300.0, 200.0, 0.0, "urbano", "estatal")
        
        self.estudiantes_mza = [self.est1, self.est2]
        self.estudiantes_ba = [self.est3, self.est4]
        self.todos_estudiantes = [self.est1, self.est2, self.est3, self.est4]
    
    def test_constructor_lista_vacia(self):
        """Test del constructor con lista vacía."""
        resumen = Resumen([])
        
        self.assertEqual(resumen.cantidad, 0)
        self.assertEqual(resumen.promedio_matematica, 0.0)
        self.assertEqual(resumen.promedio_lengua, 0.0)
        self.assertEqual(resumen.promedio_nse, 0.0)
        self.assertEqual(resumen.proporcion_ambito_rural, 0.0)
        self.assertEqual(resumen.proporcion_sector_estatal, 0.0)
    
    def test_constructor_un_estudiante(self):
        """Test del constructor con un solo estudiante."""
        resumen = Resumen([self.est1])
        
        self.assertEqual(resumen.cantidad, 1)
        self.assertEqual(resumen.promedio_matematica, 500.0)
        self.assertEqual(resumen.promedio_lengua, 400.0)
        self.assertEqual(resumen.promedio_nse, 0.5)
        self.assertEqual(resumen.proporcion_ambito_rural, 1.0)  # 100% rural
        self.assertEqual(resumen.proporcion_sector_estatal, 1.0)  # 100% estatal
    
    def test_constructor_multiples_estudiantes(self):
        """Test del constructor con múltiples estudiantes."""
        resumen = Resumen(self.estudiantes_mza)
        
        self.assertEqual(resumen.cantidad, 2)
        self.assertEqual(resumen.promedio_matematica, 550.0)  # (500 + 600) / 2
        self.assertEqual(resumen.promedio_lengua, 450.0)     # (400 + 500) / 2
        self.assertEqual(resumen.promedio_nse, 0.0)          # (0.5 - 0.5) / 2
        self.assertEqual(resumen.proporcion_ambito_rural, 0.5)    # 1 de 2 rural
        self.assertEqual(resumen.proporcion_sector_estatal, 0.5)  # 1 de 2 estatal
    
    def test_promedios_todos_estudiantes(self):
        """Test de cálculo de promedios con todos los estudiantes."""
        resumen = Resumen(self.todos_estudiantes)
        
        self.assertEqual(resumen.cantidad, 4)
        # Promedio matemática: (500 + 600 + 400 + 300) / 4 = 450
        self.assertEqual(resumen.promedio_matematica, 450.0)
        # Promedio lengua: (400 + 500 + 300 + 200) / 4 = 350
        self.assertEqual(resumen.promedio_lengua, 350.0)
        # Promedio NSE: (0.5 - 0.5 + 1.0 + 0.0) / 4 = 0.25
        self.assertEqual(resumen.promedio_nse, 0.25)
        # Rural: 2 de 4 = 0.5
        self.assertEqual(resumen.proporcion_ambito_rural, 0.5)
        # Estatal: 3 de 4 = 0.75
        self.assertEqual(resumen.proporcion_sector_estatal, 0.75)
    
    def test_repr(self):
        """Test del método __repr__."""
        resumen = Resumen(self.estudiantes_mza)
        expected = "<Mat:550.00, Len:450.00, NSE:0.00, Rural:0.50, Estado:0.50, N:2>"
        self.assertEqual(str(resumen), expected)
        
        # Test con lista vacía
        resumen_vacio = Resumen([])
        expected_vacio = "<Mat:0.00, Len:0.00, NSE:0.00, Rural:0.00, Estado:0.00, N:0>"
        self.assertEqual(str(resumen_vacio), expected_vacio)
    
    def test_eq_iguales(self):
        """Test del método __eq__ con resúmenes iguales."""
        resumen1 = Resumen(self.estudiantes_mza)
        resumen2 = Resumen(self.estudiantes_mza)
        self.assertTrue(resumen1 == resumen2)
        
        # Test con listas vacías
        resumen_vacio1 = Resumen([])
        resumen_vacio2 = Resumen([])
        self.assertTrue(resumen_vacio1 == resumen_vacio2)
    
    def test_eq_diferentes(self):
        """Test del método __eq__ con resúmenes diferentes."""
        resumen_mza = Resumen(self.estudiantes_mza)
        resumen_ba = Resumen(self.estudiantes_ba)
        self.assertFalse(resumen_mza == resumen_ba)
        
        resumen_todos = Resumen(self.todos_estudiantes)
        self.assertFalse(resumen_mza == resumen_todos)
    
    def test_eq_precision_float(self):
        """Test del método __eq__ con precisión de float."""
        # Crear estudiantes con diferencias muy pequeñas
        est_a = Estudiante("X", 500.0, 400.0, 0.5, "rural", "estatal")
        est_b = Estudiante("X", 500.0005, 399.9995, 0.5005, "rural", "estatal")
        
        resumen_a = Resumen([est_a])
        resumen_b = Resumen([est_b])
        
        # Deberían ser iguales (diferencia < 0.001)
        self.assertTrue(resumen_a == resumen_b)
        
        # Crear estudiantes con diferencias mayores al umbral
        est_c = Estudiante("X", 500.002, 400.0, 0.5, "rural", "estatal")
        resumen_c = Resumen([est_c])
        
        # No deberían ser iguales (diferencia >= 0.001)
        self.assertFalse(resumen_a == resumen_c)
    
    def test_eq_tipo_diferente(self):
        """Test del método __eq__ con tipo diferente."""
        resumen = Resumen(self.estudiantes_mza)
        self.assertFalse(resumen == "no soy un resumen")
        self.assertFalse(resumen == 123)
        self.assertFalse(resumen == None)
    
    def test_ambito_sector_case_insensitive(self):
        """Test que el cálculo de proporciones sea insensible a mayúsculas/minúsculas."""
        # Crear estudiantes con diferentes casos
        est1 = Estudiante("X", 500.0, 400.0, 0.5, "RURAL", "ESTATAL")
        est2 = Estudiante("X", 600.0, 500.0, -0.5, "Rural", "Estatal")
        est3 = Estudiante("X", 400.0, 300.0, 1.0, "rural", "estatal")
        est4 = Estudiante("X", 300.0, 200.0, 0.0, "urbano", "privado")
        
        resumen = Resumen([est1, est2, est3, est4])
        
        # 3 de 4 son rurales (75%)
        self.assertEqual(resumen.proporcion_ambito_rural, 0.75)
        # 3 de 4 son estatales (75%)
        self.assertEqual(resumen.proporcion_sector_estatal, 0.75)


if __name__ == '__main__':
    unittest.main() 