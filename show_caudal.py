# Impresión de resultados de caudal por método racional.
from caudales import calculo_caudal_racional

def mostrar_resultados_caudal_racional(
    duraciones_min: list,
    preci_prom: float,
    region: str,
    num_curva: float,
    area_km2: float,
) -> str:
    resultados = calculo_caudal_racional(
        num_curva=num_curva,
        area_km2=area_km2,
        duraciones_min=duraciones_min,
        preci_prom=preci_prom,
        region=region,
    )

    msj = ""
    msj += "======== RESULTADOS CAUDAL (METODO RACIONAL) ========\n"
    msj += f"Region: {region} | Precipitacion media (M): {preci_prom}\n"
    msj += f"Coeficiente de escorrentia (C): {num_curva} | Area (A): {area_km2} km2\n"
    msj += "Formula: Q = 0.278 * C * I(mm/h) * A(km2)\n"

    Tr_actual = None
    for Tr, dur_h, intensidad_mm_h, caudal_m3_s in resultados:
        if Tr != Tr_actual:
            msj += f"\nPERIODO DE RETORNO Tr = {Tr} anios\n"
            msj += "-" * 78 + "\n"
            msj += (
                f"{'Duracion (min)':>13} | {'Duracion (h)':>11} | "
                f"{'I (mm/h)':>10} | {'Q (m3/s)':>11}\n"
            )
            msj += "-" * 78 + "\n"
            Tr_actual = Tr

        dur_min = dur_h * 60
        msj += (
            f"{dur_min:13.0f} | {dur_h:11.3f} | {intensidad_mm_h:10.3f} | {caudal_m3_s:11.3f}\n"
        )

    return msj
