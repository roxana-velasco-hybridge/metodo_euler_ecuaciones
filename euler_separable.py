"""Solución exacta y aproximación de Euler para y' = y, y(0) = 1."""

from math import exp, isclose


def main() -> None:
    """Calcula la solución de Euler entre 0 y 1 con paso 0.2."""
    t_inicial = 0.0
    t_final = 1.0
    paso = 0.2
    y = 1.0
    t = t_inicial
    numero_pasos = round((t_final - t_inicial) / paso)

    print("Ecuación diferencial: y' = y, con y(0) = 1")
    print("Solución exacta: y(t) = e^t")
    print(f"Método de Euler: intervalo [{t_inicial}, {t_final}], h = {paso}\n")
    print(f"{'n':>2} {'t_n':>6} {'y_Euler':>12} {'y_exacta':>12} {'error abs.':>12}")

    for n in range(numero_pasos + 1):
        valor_exacto = exp(t)
        error = abs(valor_exacto - y)
        print(f"{n:2d} {t:6.1f} {y:12.6f} {valor_exacto:12.6f} {error:12.6f}")

        if n < numero_pasos:
            y = y + paso * y
            t += paso

    assert isclose(t, t_final), "El cálculo no terminó en el extremo del intervalo."


if __name__ == "__main__":
    main()
