# Curvas Intensidad–Duración–Frecuencia (IDF)
# Método: Vargas & Díaz-Granados (1998)
#
# I(mm/h) = (A · T^B · M^D) / ( (t/60)^C )
#
# Donde:
# - T: periodo de retorno (años)
# - t: duración (min)
# - M: precipitación media

region = "Andina"


def parametros_region(region: str) -> dict:
    # Ecuación 8 (Vargas & Díaz-Granados, 1998)
    match region:
        case "Andina":  # Tiene un R^2 de 0.93
            return {"A": 0.94, "B": 0.18, "C": 0.66, "D": 0.83}
        case "Caribe":  # Tiene un R^2 de 0.72
            return {"A": 24.85, "B": 0.22, "C": 0.50, "D": 0.10}
        case "Pacifica":  # Tiene un R^2 de 0.88
            return {"A": 13.92, "B": 0.19, "C": 0.58, "D": 0.20}
        case "Orinoquia":  # Tiene un R^2 de 0.91
            return {"A": 5.53, "B": 0.17, "C": 0.63, "D": 0.42}
        case _:
            raise ValueError(f"Región no soportada: {region!r}")


def calcular_idf(duraciones_min: list, preci_prom: float, region: str) -> list:
    tiempos_retorno = [2, 5, 10, 25, 50, 100]
    duracion_h = [d / 60 for d in duraciones_min]
    val_reg = parametros_region(region)

    M = preci_prom
    A = val_reg["A"]
    B = val_reg["B"]
    C = val_reg["C"]
    D = val_reg["D"]

    idf_resultados = []
    for T in tiempos_retorno:
        for dur_h in duracion_h:
            intensidad_mm_h = (A * (T**B) * (M**D)) / (dur_h**C)
            idf_resultados.append((T, dur_h, intensidad_mm_h))

    return idf_resultados

