class Estudiante:
    """
    Clase que modela los resultados y otros datos de un estudiante individual.
    """
    
    def __init__(self, provincia: str, puntaje_matematica: float, puntaje_lengua: float, 
                 puntaje_nse: float, ambito: str, sector: str) -> None:
        """
        Construye un nuevo objeto de la clase Estudiante.
        
        Args:
            provincia: la provincia de la escuela en la que estudia el estudiante
            puntaje_matematica: puntaje en matemática del estudiante
            puntaje_lengua: puntaje en lengua del estudiante
            puntaje_nse: el puntaje del nivel socioeconómico del estudiante
            ambito: ámbito de la escuela del estudiante ('rural' o 'urbano')
            sector: tipo de gestión de la escuela del estudiante ('estatal' o 'privado')
        """
        self.provincia: str = provincia
        self.puntaje_matematica: float = puntaje_matematica
        self.puntaje_lengua: float = puntaje_lengua
        self.puntaje_nse: float = puntaje_nse
        self.ambito: str = ambito
        self.sector: str = sector
    
    def __repr__(self) -> str:
        """
        Devuelve una representación como string del estudiante.
        
        Returns:
            String con formato: <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, AMBITO, SECTOR, PROVINCIA>
        """
        # Capitalizar ambito y sector para el formato requerido
        ambito_formato = self.ambito.capitalize()
        sector_formato = self.sector.capitalize()
        
        return (f"<Mat:{self.puntaje_matematica:.2f}, Len:{self.puntaje_lengua:.2f}, "
                f"NSE:{self.puntaje_nse:.2f}, {ambito_formato}, {sector_formato}, {self.provincia}>")
    
    def __eq__(self, other) -> bool:
        """
        Devuelve True si ambos estudiantes tienen provincia, puntajes, ámbito y sector iguales.
        Dos valores float son considerados iguales si la diferencia absoluta es menor que 0.001.
        
        Requiere:
            - other puede ser cualquier objeto (se verifica tipo internamente)
            
        Asegura:
            - True si y solo si other es Estudiante con todos los atributos iguales
            - False en cualquier otro caso
        
        Args:
            other: otro objeto para comparar
            
        Devuelve:
            True si son iguales según criterio de igualdad definido, False en caso contrario
        """
        if not isinstance(other, Estudiante):
            return False
            
        return (self.provincia == other.provincia and
                abs(self.puntaje_matematica - other.puntaje_matematica) < 0.001 and
                abs(self.puntaje_lengua - other.puntaje_lengua) < 0.001 and
                abs(self.puntaje_nse - other.puntaje_nse) < 0.001 and
                self.ambito == other.ambito and
                self.sector == other.sector) 