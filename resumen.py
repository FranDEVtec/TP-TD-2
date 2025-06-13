from typing import List
from estudiante import Estudiante


class Resumen:
    """
    Clase que encapsula varias estadísticas de interés, calculadas sobre algún conjunto de estudiantes.
    """
    
    def __init__(self, estudiantes: List[Estudiante]) -> None:
        """
        Construye un nuevo objeto de la clase Resumen a partir de una lista de estudiantes.
        
        Requiere:
            - estudiantes es una lista válida (puede estar vacía)
            - todos los elementos son objetos Estudiante
            
        Asegura:
            - cantidad = len(estudiantes)
            - Si lista vacía: promedios y proporciones = 0.0
            - Si no vacía: estadísticas calculadas según definiciones matemáticas
            
        Args:
            estudiantes: lista de objetos Estudiante para calcular las estadísticas
        """
        self.cantidad: int = len(estudiantes)
        
        if self.cantidad == 0:
            self.promedio_matematica: float = 0.0
            self.promedio_lengua: float = 0.0
            self.promedio_nse: float = 0.0
            self.proporcion_ambito_rural: float = 0.0
            self.proporcion_sector_estatal: float = 0.0
        else:
            # Calcular promedios
            suma_matematica = sum(est.puntaje_matematica for est in estudiantes)
            suma_lengua = sum(est.puntaje_lengua for est in estudiantes)
            suma_nse = sum(est.puntaje_nse for est in estudiantes)
            
            self.promedio_matematica: float = suma_matematica / self.cantidad
            self.promedio_lengua: float = suma_lengua / self.cantidad
            self.promedio_nse: float = suma_nse / self.cantidad
            
            # Calcular proporciones
            rural_count = sum(1 for est in estudiantes if est.ambito.lower() == 'rural')
            estatal_count = sum(1 for est in estudiantes if est.sector.lower() == 'estatal')
            
            self.proporcion_ambito_rural: float = rural_count / self.cantidad
            self.proporcion_sector_estatal: float = estatal_count / self.cantidad
    
    def __repr__(self) -> str:
        """
        Devuelve una representación como string del resumen.
        
        Returns:
            String con formato: <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, Rural:FLOAT, Estado:FLOAT, N:INT>
        """
        return (f"<Mat:{self.promedio_matematica:.2f}, Len:{self.promedio_lengua:.2f}, "
                f"NSE:{self.promedio_nse:.2f}, Rural:{self.proporcion_ambito_rural:.2f}, "
                f"Estado:{self.proporcion_sector_estatal:.2f}, N:{self.cantidad}>")
    
    def __eq__(self, other) -> bool:
        """
        Devuelve True si ambos resúmenes tienen cantidad, promedios y proporciones iguales.
        Dos valores float son considerados iguales si la diferencia absoluta es menor que 0.001.
        
        Args:
            other: otro objeto Resumen para comparar
            
        Returns:
            True si son iguales, False en caso contrario
        """
        if not isinstance(other, Resumen):
            return False
            
        return (self.cantidad == other.cantidad and
                abs(self.promedio_matematica - other.promedio_matematica) < 0.001 and
                abs(self.promedio_lengua - other.promedio_lengua) < 0.001 and
                abs(self.promedio_nse - other.promedio_nse) < 0.001 and
                abs(self.proporcion_ambito_rural - other.proporcion_ambito_rural) < 0.001 and
                abs(self.proporcion_sector_estatal - other.proporcion_sector_estatal) < 0.001) 