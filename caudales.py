#Calculo de caudales por los metodos: Racional y dos diagramas unitarios.
#Metodo racional.
#𝑄=0,278∗𝐶∗𝑖∗𝐴
from data import duraciones_min,preci_prom,region,area_km2,num_curva
from IDF import calcular_idf
def calculo_caudal_racional(
                            num_curva: float,
                            area_km2: float,
                            duraciones_min: list = duraciones_min,
                            preci_prom: float = preci_prom,
                            region: str = region,
                            )->list:
     idf_resultados = calcular_idf(duraciones_min, preci_prom, region)

     resultados_caudal = []
     for Tr, dur_h, intensidad_mm_h in idf_resultados:
         caudal_racional = 0.278 * num_curva * intensidad_mm_h * area_km2
         resultados_caudal.append((Tr, dur_h, intensidad_mm_h, caudal_racional))

     return resultados_caudal
      

   
if __name__ == "__main__":
    print(calculo_caudal_racional(num_curva, area_km2))

    
    
    
     
    
