# Trabajo Práctico 2 - Análisis de Datos Educativos

Este proyecto implementa un sistema para procesar y analizar datos de las Pruebas Aprender 2023.

## Estructura del Proyecto

- `estudiante.py`: Clase Estudiante para modelar datos individuales
- `resumen.py`: Clase Resumen para estadísticas de grupos de estudiantes
- `pais.py`: Clase Pais para manejar el dataset completo
- `*_test.py`: Tests unitarios para cada clase
- `test_datos.csv`: Archivo CSV pequeño para testing
- `informe.md`: Análisis de complejidad algorítmica

## Uso Básico

### Crear un estudiante
```python
from estudiante import Estudiante

est = Estudiante("MZA", 500.0, 400.0, 0.5, "rural", "estatal")
print(est)  # <Mat:500.00, Len:400.00, NSE:0.50, Rural, Estatal, MZA>
```

### Crear un resumen de estudiantes
```python
from resumen import Resumen

estudiantes = [est1, est2, est3]
resumen = Resumen(estudiantes)
print(resumen.promedio_matematica)
```

### Cargar y analizar dataset
```python
from pais import Pais

pais = Pais("Aprender2023_curado.csv")
print(f"Total de estudiantes: {pais.tamano()}")

# Resumen por provincia
resumen_mza = pais.resumen_provincia("MZA")
print(resumen_mza)

# Exportar datos
pais.exportar_por_provincias("salida.csv", {"MZA", "BA"})
```

## Ejecutar Tests

```bash
python3 -m unittest estudiante_test.py
python3 -m unittest resumen_test.py
python3 -m unittest pais_test.py
```

## Requisitos

- Python 3.x
- Solo bibliotecas estándar: `csv`, `unittest` # TP-TD-2
