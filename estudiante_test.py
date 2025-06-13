import unittest
from estudiante import Estudiante


class TestEstudiante(unittest.TestCase):
    """Tests de unidad para la clase Estudiante."""
    
    def setUp(self):
        """Configuración inicial para los tests."""
        self.estudiante1 = Estudiante("MZA", 507.25, 488.68, -0.26, "rural", "privado")
        self.estudiante2 = Estudiante("SFE", 466.76, 550.32, 0.01, "urbano", "estatal")
        self.estudiante3 = Estudiante("MZA", 507.25, 488.68, -0.26, "rural", "privado")
    
    def test_constructor(self):
        """Test del constructor de Estudiante."""
        est = Estudiante("CRR", 492.72, 542.52, 0.34, "rural", "estatal")
        
        self.assertEqual(est.provincia, "CRR")
        self.assertEqual(est.puntaje_matematica, 492.72)
        self.assertEqual(est.puntaje_lengua, 542.52)
        self.assertEqual(est.puntaje_nse, 0.34)
        self.assertEqual(est.ambito, "rural")
        self.assertEqual(est.sector, "estatal")
    
    def test_repr(self):
        """Test del método __repr__."""
        # Test con rural y privado
        expected1 = "<Mat:507.25, Len:488.68, NSE:-0.26, Rural, Privado, MZA>"
        self.assertEqual(str(self.estudiante1), expected1)
        
        # Test con urbano y estatal
        expected2 = "<Mat:466.76, Len:550.32, NSE:0.01, Urbano, Estatal, SFE>"
        self.assertEqual(str(self.estudiante2), expected2)
        
        # Test con números decimales exactos
        est = Estudiante("CRR", 492.72, 542.52, 0.34, "rural", "estatal")
        expected3 = "<Mat:492.72, Len:542.52, NSE:0.34, Rural, Estatal, CRR>"
        self.assertEqual(str(est), expected3)
    
    def test_eq_iguales(self):
        """Test del método __eq__ con estudiantes iguales."""
        # Mismos valores exactos
        self.assertTrue(self.estudiante1 == self.estudiante3)
        
        # Valores float muy cercanos (dentro del umbral de 0.001)
        est1 = Estudiante("BA", 500.000, 400.000, 0.500, "urbano", "estatal")
        est2 = Estudiante("BA", 500.0005, 399.9995, 0.5005, "urbano", "estatal")
        self.assertTrue(est1 == est2)
    
    def test_eq_diferentes(self):
        """Test del método __eq__ con estudiantes diferentes."""
        # Diferentes en todos los aspectos
        self.assertFalse(self.estudiante1 == self.estudiante2)
        
        # Diferentes solo en provincia
        est1 = Estudiante("BA", 500.0, 400.0, 0.5, "urbano", "estatal")
        est2 = Estudiante("COR", 500.0, 400.0, 0.5, "urbano", "estatal")
        self.assertFalse(est1 == est2)
        
        # Diferentes solo en puntaje_matematica (fuera del umbral)
        est3 = Estudiante("BA", 500.0, 400.0, 0.5, "urbano", "estatal")
        est4 = Estudiante("BA", 500.002, 400.0, 0.5, "urbano", "estatal")
        self.assertFalse(est3 == est4)
        
        # Diferentes solo en ambito
        est5 = Estudiante("BA", 500.0, 400.0, 0.5, "urbano", "estatal")
        est6 = Estudiante("BA", 500.0, 400.0, 0.5, "rural", "estatal")
        self.assertFalse(est5 == est6)
        
        # Diferentes solo en sector
        est7 = Estudiante("BA", 500.0, 400.0, 0.5, "urbano", "estatal")
        est8 = Estudiante("BA", 500.0, 400.0, 0.5, "urbano", "privado")
        self.assertFalse(est7 == est8)
    
    def test_eq_tipo_diferente(self):
        """Test del método __eq__ con tipo diferente."""
        self.assertFalse(self.estudiante1 == "no soy un estudiante")
        self.assertFalse(self.estudiante1 == 123)
        self.assertFalse(self.estudiante1 == None)
    
    def test_puntajes_negativos(self):
        """Test con puntajes negativos."""
        est = Estudiante("TDF", -10.5, -20.3, -1.5, "rural", "estatal")
        self.assertEqual(est.puntaje_matematica, -10.5)
        self.assertEqual(est.puntaje_lengua, -20.3)
        self.assertEqual(est.puntaje_nse, -1.5)
        
        expected = "<Mat:-10.50, Len:-20.30, NSE:-1.50, Rural, Estatal, TDF>"
        self.assertEqual(str(est), expected)


if __name__ == '__main__':
    unittest.main() 