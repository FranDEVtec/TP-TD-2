import csv
from typing import List, Dict, Set
from estudiante import Estudiante
from resumen import Resumen


class Pais:
    """
    Clase que modela el dataset de resultados de un país y las consultas que se pueden hacer sobre los mismos.
    """
    
    def __init__(self, archivo_csv: str) -> None:
        """
        Construye un nuevo objeto de la clase Pais a partir del archivo CSV pasado como argumento.
        
        Args:
            archivo_csv: nombre del archivo CSV con los datos de estudiantes
        """
        self._estudiantes: List[Estudiante] = []
        self._tamano: int = 0
        self.provincias: Set[str] = set()
        
        # Leer el archivo CSV y crear objetos Estudiante
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                provincia = row['provincia']
                sector = row['sector']
                ambito = row['ambito']
                puntaje_lengua = float(row['lpuntaje'])
                puntaje_matematica = float(row['mpuntaje'])
                puntaje_nse = float(row['NSE_puntaje'])
                
                estudiante = Estudiante(provincia, puntaje_matematica, puntaje_lengua, 
                                      puntaje_nse, ambito.lower(), sector.lower())
                
                self._estudiantes.append(estudiante)
                self.provincias.add(provincia)
                self._tamano += 1
    
    def tamano(self) -> int:
        """
        Devuelve la cantidad de estudiantes en el dataset.
        Complejidad temporal: O(1)
        
        Returns:
            Cantidad de estudiantes en el dataset
        """
        return self._tamano
    
    def resumen_provincia(self, provincia: str) -> Resumen:
        """
        Devuelve un objeto de la clase Resumen con estadísticas para la provincia dada.
        Complejidad temporal: O(N) donde N es la cantidad de estudiantes en el país.
        
        Args:
            provincia: código de la provincia
            
        Returns:
            Objeto Resumen con las estadísticas de la provincia
        """
        estudiantes_provincia = [est for est in self._estudiantes if est.provincia == provincia]
        return Resumen(estudiantes_provincia)
    
    def resumenes_pais(self) -> Dict[str, Resumen]:
        """
        Devuelve un diccionario donde las claves son las provincias presentes y los valores son sus resúmenes.
        Complejidad temporal: O(N*P) donde N es la cantidad de estudiantes y P la cantidad de provincias.
        
        Returns:
            Diccionario con provincias como claves y sus resúmenes como valores
        """
        resumenes = {}
        for provincia in self.provincias:
            resumenes[provincia] = self.resumen_provincia(provincia)
        return resumenes
    
    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias: Set[str]) -> int:
        """
        Devuelve la cantidad de estudiantes de las provincias indicadas que tienen un puntaje 
        en la categoría especificada mayor o igual que x y menor estricto que y.
        Complejidad temporal: O(N*P) donde N es la cantidad de estudiantes y P la cantidad de provincias.
        
        Requiere:
            - categoria ∈ {'mat', 'len', 'nse'}
            - x <= y (intervalo válido)
            - provincias es un conjunto no nulo
            
        Args:
            categoria: 'mat', 'len' o 'nse'
            x: límite inferior (inclusive)
            y: límite superior (exclusivo)
            provincias: conjunto de provincias a considerar
            
        Devuelve:
            Cantidad de estudiantes que cumplen TODAS las condiciones:
            - estudiante.provincia ∈ provincias
            - x <= puntaje_categoria < y
        """
        count = 0
        for estudiante in self._estudiantes:
            if estudiante.provincia in provincias:
                puntaje = 0.0
                if categoria == 'mat':
                    puntaje = estudiante.puntaje_matematica
                elif categoria == 'len':
                    puntaje = estudiante.puntaje_lengua
                elif categoria == 'nse':
                    puntaje = estudiante.puntaje_nse
                
                if x <= puntaje < y:
                    count += 1
        
        return count
    
    def exportar_por_provincias(self, archivo_csv: str, provincias: Set[str]) -> None:
        """
        Genera un nuevo archivo CSV con una fila por cada una de las provincias indicadas.
        
        Args:
            archivo_csv: nombre del archivo CSV de salida
            provincias: conjunto de provincias a incluir en el archivo
        """
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['provincia', 'cantidad', 'promedio_matematica', 'promedio_lengua', 
                         'promedio_nse', 'proporcion_ambito_rural', 'proporcion_sector_estatal']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for provincia in provincias:
                resumen = self.resumen_provincia(provincia)
                writer.writerow({
                    'provincia': provincia,
                    'cantidad': resumen.cantidad,
                    'promedio_matematica': resumen.promedio_matematica,
                    'promedio_lengua': resumen.promedio_lengua,
                    'promedio_nse': resumen.promedio_nse,
                    'proporcion_ambito_rural': resumen.proporcion_ambito_rural,
                    'proporcion_sector_estatal': resumen.proporcion_sector_estatal
                }) 