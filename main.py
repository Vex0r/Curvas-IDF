from show_IDF import mostrar_parametros, mostrar_resultados_idf
region = "Andina"
duraciones_min = [5,10,15,30,60,120]
preci_prom = 146.51
print("========RESULTADOS CURVA IDF========")
print(f'==Parametros de la Region {region}==')
print(mostrar_parametros(region))
print(mostrar_resultados_idf(duraciones_min, preci_prom, region))


