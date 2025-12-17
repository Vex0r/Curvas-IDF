#imprimir resultados en pantalla.
from IDF import parametros_region, calcular_idf

def mostrar_parametros(region:str):
    valor_reg = parametros_region(region)
    msj = ""
    for  variable, valor in valor_reg.items(): #mostrar clave:valor del diccionario
        msj += f'{variable} = {valor}\n'
    return msj


def mostrar_resultados_idf(duraciones_min: list, preci_prom: float, region: str) -> str:
    res_idf = calcular_idf(duraciones_min, preci_prom, region)
    msj = ""
    T_actual = None
    for T, dur_h, valor in res_idf:
        if T != T_actual:
            msj += f"\nPERÍODO DE RETORNO Tr = {T} años\n"
            msj += "-" * 40 + "\n"
            T_actual = T

        msj += f"Duración: {round(dur_h, 2)} h | IDF: {round(valor, 3)}\n"

    return msj