# Solución de una ecuación diferencial separable con Euler

Este proyecto resuelve una ecuación diferencial separable de dos maneras: analíticamente mediante separación de variables y numéricamente mediante el método de Euler explícito.

## Problema

Consideramos el problema de valor inicial

$$
\frac{dy}{dt}=y, \qquad y(0)=1,
$$

en el intervalo $t\in[0,1]$, usando un paso $h=0.2$ para la aproximación numérica.

## Solución analítica

Separamos las variables:

$$
\frac{dy}{y}=dt.
$$

Integramos ambos lados:

$$
\ln|y|=t+C.
$$

Al despejar, $y=Ce^t$. La condición inicial $y(0)=1$ implica $C=1$, por lo que la solución exacta es

$$
y(t)=e^t.
$$

## Método de Euler

Para una ecuación $y'=f(t,y)$, el método de Euler explícito aplica la recurrencia

$$
y_{n+1}=y_n+h f(t_n,y_n), \qquad t_{n+1}=t_n+h.
$$

En este problema, $f(t,y)=y$, $h=0.2$ y $y_0=1$, así que

$$
y_{n+1}=y_n+0.2y_n=1.2y_n.
$$

Se realizan cinco pasos para llegar desde $t_0=0$ hasta $t_5=1$.

## Ejecución

Se requiere Python 3; el programa utiliza únicamente la biblioteca estándar. Desde la carpeta del proyecto, ejecuta:

```bash
python euler_separable.py
```

El programa imprime, para cada nodo $t_n$, la aproximación de Euler, el valor exacto $e^{t_n}$ y el error absoluto.

## Resultado esperado

| $n$ | $t_n$ | Euler $y_n$ | Exacta $e^{t_n}$ | Error absoluto |
|---:|---:|---:|---:|---:|
| 0 | 0.0 | 1.000000 | 1.000000 | 0.000000 |
| 1 | 0.2 | 1.200000 | 1.221403 | 0.021403 |
| 2 | 0.4 | 1.440000 | 1.491825 | 0.051825 |
| 3 | 0.6 | 1.728000 | 1.822119 | 0.094119 |
| 4 | 0.8 | 2.073600 | 2.225541 | 0.151941 |
| 5 | 1.0 | 2.488320 | 2.718282 | 0.229962 |

## Archivos

- `euler_separable.py`: calcula y muestra la aproximación de Euler y la solución exacta.
- `README.md`: describe el planteamiento y el procedimiento.
