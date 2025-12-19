# Curvas IDF y caudales pico (metodo racional)

Herramienta en Python para apoyo en analisis hidrologico: calculo de **curvas IDF** y estimacion de **caudal pico** mediante el **metodo racional**, con impresion de resultados en consola.

Autor: **Oscar Rueda**

## Alcance y fundamento

### Curvas IDF

La intensidad de lluvia `I` (mm/h) se calcula mediante una expresion regional del metodo de **Vargas & Diaz-Granados (1998)**:

`I = (A * T^B * M^D) / ( (t/60)^C )`

Donde:

- `T`: periodo de retorno (anios)
- `t`: duracion (min)
- `M`: precipitacion media (segun tu fuente de datos)
- `A, B, C, D`: parametros por region

El script calcula intensidades para `T = [2, 5, 10, 25, 50, 100]` y para cada duracion definida en `duraciones_min`.

### Caudal pico (metodo racional)

Se estima el caudal pico:

`Q = 0.278 * C * I * A`

- `Q`: caudal pico (m3/s)
- `C`: coeficiente de escorrentia (adimensional)
- `I`: intensidad de lluvia (mm/h), proveniente de la IDF
- `A`: area de drenaje (km2)
- `0.278`: factor de conversion a m3/s para las unidades indicadas

## Requisitos

- Python 3.10+ (recomendado 3.12)

## Archivos principales

- `data.py`: datos de entrada del caso (region, duraciones, `M`, `C`, `A`).
- `IDF.py`: calculo de intensidades IDF.
- `show_IDF.py`: impresion en consola de parametros y resultados IDF.
- `caudales.py`: calculo de caudal racional a partir de intensidades IDF.
- `show_caudal.py`: impresion en consola de resultados de caudal (tabla por `Tr`).
- `main.py`: ejemplo de ejecucion (IDF + caudal).

## Configuracion de entrada

Edita `data.py` con tus datos:

- `region`: `"Andina" | "Caribe" | "Pacifica" | "Orinoquia"`
- `duraciones_min`: lista de duraciones (min)
- `preci_prom`: precipitacion media `M`
- `num_curva`: coeficiente `C`
- `area_km2`: area `A` (km2)

## Ejecucion

Imprimir resultados IDF y caudal racional (ejemplo):

```bash
python main.py
```

Imprimir solo caudal racional:

```bash
python show_caudal.py
```

## Salidas

- `IDF.calcular_idf(duraciones_min, preci_prom, region)` retorna una lista de tuplas: `(Tr, duracion_h, intensidad_mm_h)`.
- `caudales.calculo_caudal_racional(...)` retorna una lista de tuplas: `(Tr, duracion_h, intensidad_mm_h, Q_m3_s)`.

## Consideraciones de ingenieria

- El metodo racional se usa tipicamente para cuencas pequenas (dependiendo de lineamientos locales); valida su aplicabilidad para tu proyecto.
- Verifica consistencia de unidades: `I` en mm/h y `A` en km2 (tal como se usa en la formula con 0.278).
- Los parametros regionales deben corresponder a la region y a la fuente metodologica adoptada.

## Nota de codificacion (acentos/ni)

Este repositorio esta en **UTF-8**. Si en Windows PowerShell ves caracteres extranos, ejecuta `chcp 65001` antes de imprimir archivos o revisa el README desde tu editor (p. ej., VS Code).

Sugerencia (PowerShell):

```powershell
chcp 65001
$OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```
