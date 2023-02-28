import logging
from typing import Callable
import numpy as np


def dichotomic_search(func: Callable[[np.float32], np.float32],
                      a: np.float32, b: np.float32,
                      eps: np.float32,
                      l: np.float32
                      ) -> tuple[np.float32, np.integer]:
    """
    Метод дихотомии.
    Идея метода состоит в вычислении на каждой \
    очередной итерации двух значений целевой функции в точках, отстоящих на \
    величину 'eps' в обе стороны от середины интервала неопределенности.

    Args:
        func (Callable[[np.float32], np.float32]): целевая функция f(x)
        a (np.float32): левая граница интервала неопределенности
        b (np.float32): правая граница интервала неопределенности
        eps (np.float32): константа различимости
        l (np.float32): конечная длина интервала

    Returns:
        tuple[np.float32, np.integer]: tuple[точка минимума, кол-во потребовавшихся итераций]
    """
    assert eps >= 0, "'eps' should not be negative"
    assert l >= 0, "'l' should not be negative"
    assert b > a, f"invalid interval [{a}, {b}]"

    assert l > 2 * eps, "l must be more than 2 eps"

    logging.debug(
        "starting extremum search for %s on interval [%.3f, %.3f] with eps=%f, l=%f",
        func.__name__, a, b, eps, l
    )

    k = 1
    while True:
        # Шаг 1
        logging.debug(
            "b - a <= l? %.3f - %.3f (%.3f) < %.3f? - %r",
            b, a, b - a, l, b - a < l or np.isclose(b - a, l)
        )
        if b - a < l or np.isclose(b - a, l):
            break
        lm = (a + b) / 2 - eps
        mu = (a + b) / 2 + eps

        # Шаг 2
        f_lm = func(lm)
        f_mu = func(mu)
        if f_lm < f_mu:
            # a = a
            b = mu
        else:
            a = lm
            # b = b

        # Шаг 3
        k += 1

        logging.debug(
            "k=%i\n\t    a: %.3f,     b: %.3f\n\t   lm: %.3f,    mu: %.3f\n\tf(lm): %.3f, f(mu): %.3f",
            k, a, b, lm, mu, f_lm, f_mu
        )
        logging.debug("new [a, b]: [%.3f, %.3f]", a, b)

    return (a + b) / 2, k

    # TODO: Метод золотого сечения

    # TODO: Метод Фибоначи


def fibonacci_seq(n: np.integer) -> list[np.integer]:
    return [fibonacci_of(i) for i in range(n + 1)]


def fibonacci_of(n: np.integer) -> np.integer:
    fib_cache = {0: 0, 1: 1}
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return fib_cache[n]
