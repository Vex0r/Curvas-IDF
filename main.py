from show_IDF import mostrar_parametros, mostrar_resultados_idf
from show_caudal import mostrar_resultados_caudal_racional
from data import region, duraciones_min,preci_prom,num_curva,area_km2
print("========RESULTADOS CURVA IDF========")
print(f'==Parametros de la Region {region}==')
print(mostrar_parametros(region))
print(mostrar_resultados_idf(duraciones_min, preci_prom, region))
print(
        mostrar_resultados_caudal_racional(
            duraciones_min=duraciones_min,
            preci_prom=preci_prom,
            region=region,
            num_curva=num_curva,
            area_km2=area_km2,
        )
        )