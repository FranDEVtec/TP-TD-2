#!/usr/bin/env python3

# Test simple para verificar que todo funciona
from estudiante import Estudiante
from resumen import Resumen
from pais import Pais

def test_estudiante():
    """Test básico de la clase Estudiante."""
    print("Probando clase Estudiante...")
    est = Estudiante("MZA", 500.0, 400.0, 0.5, "rural", "estatal")
    print(f"Estudiante creado: {str(est)}")
    
    # Test de igualdad
    est2 = Estudiante("MZA", 500.0, 400.0, 0.5, "rural", "estatal")
    print(f"Igualdad: {est == est2}")
    
    est3 = Estudiante("BA", 500.0, 400.0, 0.5, "rural", "estatal")
    print(f"Diferencia: {est == est3}")

def test_resumen():
    """Test básico de la clase Resumen."""
    print("\nProbando clase Resumen...")
    est1 = Estudiante("MZA", 500.0, 400.0, 0.5, "rural", "estatal")
    est2 = Estudiante("MZA", 600.0, 500.0, -0.5, "urbano", "privado")
    
    resumen = Resumen([est1, est2])
    print(f"Resumen: {str(resumen)}")

def test_pais():
    """Test básico de la clase Pais."""
    print("\nProbando clase Pais...")
    try:
        pais = Pais("test_datos.csv")
        print(f"Tamaño del país: {pais.tamano()}")
        print(f"Provincias: {pais.provincias}")
        
        resumen_mza = pais.resumen_provincia("MZA")
        print(f"Resumen MZA: {str(resumen_mza)}")
        
    except Exception as e:
        print(f"Error al probar Pais: {e}")

if __name__ == "__main__":
    test_estudiante()
    test_resumen() 
    test_pais()
    print("\n¡Tests completados!") 