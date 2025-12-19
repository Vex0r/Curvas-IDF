"""
`data.py` — Datos de entrada (caso de estudio)

Edita únicamente la sección **CASO** y respeta las unidades.

Unidades usadas en el proyecto:
- `t` (duración): min
- `M` (precipitación media): mm (según tu fuente)
- `I` (intensidad): mm/h (sale de `IDF.py`)
- `A` (área de drenaje): km²
- `Q` (caudal pico): m³/s

Regiones soportadas (Vargas & Díaz-Granados, 1998):
`"Andina" | "Caribe" | "Pacifica" | "Orinoquia"`
"""

from __future__ import annotations

SUPPORTED_REGIONS: tuple[str, ...] = ("Andina", "Caribe", "Pacifica", "Orinoquia")

# ============================================================================
# CASO (EDITAR AQUÍ)
# ============================================================================
# Nomenclatura hidrológica:
# - `M`: precipitación media (mm)
# - `C`: coeficiente de escorrentía (adimensional)
# - `A`: área de drenaje (km²)
CASO: dict[str, object] = {
    "region": "Andina",
    "duraciones_min": [5, 10, 15, 30, 60, 120],
    "M_mm": 146.51,
    "C": 0.748,
    "A_km2": 957.81,
}

# ============================================================================
# EXPORTS (NO EDITAR) — compatibilidad con el resto del proyecto
# ============================================================================
region: str = str(CASO["region"])
duraciones_min: list[int] = list(CASO["duraciones_min"])  # type: ignore[arg-type]
preci_prom: float = float(CASO["M_mm"])
num_curva: float = float(CASO["C"])
area_km2: float = float(CASO["A_km2"])


def validar_caso(caso: dict[str, object] | None = None) -> list[str]:
    caso = CASO if caso is None else caso
    errores: list[str] = []

    region_local = str(caso.get("region", ""))
    if region_local not in SUPPORTED_REGIONS:
        errores.append(f"`region` debe ser una de {SUPPORTED_REGIONS}; recibido: {region_local!r}.")

    duraciones = caso.get("duraciones_min")
    if not isinstance(duraciones, list) or not duraciones:
        errores.append("`duraciones_min` debe ser una lista no vacía de minutos (enteros).")
    else:
        try:
            dur_int = [int(d) for d in duraciones]
        except Exception:
            errores.append("`duraciones_min` debe contener solo números (min).")
        else:
            if any(d <= 0 for d in dur_int):
                errores.append("`duraciones_min` debe contener valores > 0 (min).")
            if dur_int != sorted(dur_int):
                errores.append("`duraciones_min` debe estar ordenada ascendente.")

    m_mm = caso.get("M_mm")
    if not isinstance(m_mm, (int, float)) or float(m_mm) <= 0:
        errores.append("`M_mm` (precipitación media) debe ser un número > 0 (mm).")

    c = caso.get("C")
    if not isinstance(c, (int, float)) or not (0 < float(c) <= 1):
        errores.append("`C` (coef. escorrentía) debe estar en (0, 1].")

    a_km2 = caso.get("A_km2")
    if not isinstance(a_km2, (int, float)) or float(a_km2) <= 0:
        errores.append("`A_km2` (área) debe ser un número > 0 (km²).")

    return errores


if __name__ == "__main__":
    errs = validar_caso()
    if errs:
        raise SystemExit("Errores en `CASO`:\n- " + "\n- ".join(errs))
    print("OK: `CASO` válido.")
