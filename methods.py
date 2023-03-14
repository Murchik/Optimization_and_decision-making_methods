import logging
from typing import Callable
import functools
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
        "starting dichotomic extremum search for %s on interval [%.3f, %.3f] with eps=%f, l=%f",
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


def golden_search(func: Callable[[np.float32], np.float32],
                  a: np.float32, b: np.float32,
                  eps: np.float32,
                  l: np.float32
                  ) -> tuple[np.float32, np.integer]:
    """
    Метод золотого сечения.
    Идея метода состоит в использовании на \
    каждой итерации для сокращения интервала неопределенности одной из \
    внутренних точек предыдущей итерации.

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
        "starting golden extremum search for %s on interval [%.3f, %.3f] with eps=%f, l=%f",
        func.__name__, a, b, eps, l
    )

    alpha = (np.sqrt(5) - 1) / 2  # 0.61803...

    # Шаг 0
    lm = a + (1 - alpha) * (b - a)
    mu = a + alpha * (b - a)

    f_lm = func(lm)
    f_mu = func(mu)

    k = 1
    while True:
        # Шаг 1
        logging.debug(
            "b - a <= l? %.3f - %.3f (%.3f) < %.3f? - %r",
            b, a, b - a, l, b - a < l or np.isclose(b - a, l)
        )
        if b - a < l or np.isclose(b - a, l):
            break

        if f_lm > f_mu:
            # Шаг 2
            a = lm
            # b = b

            lm = mu
            mu = a + alpha * (b - a)

            f_lm = f_mu
            f_mu = func(mu)

        # f_lm <= f_mu
        else:
            # Шаг 3
            # a = a
            b = mu

            mu = lm
            lm = a + (1 - alpha) * (b - a)

            f_mu = f_lm
            f_lm = func(lm)

        # Шаг 4
        k += 1

        logging.debug(
            "k=%i\n\t    a: %.3f,     b: %.3f\n\t   lm: %.3f,    mu: %.3f\n\tf(lm): %.3f, f(mu): %.3f",
            k, a, b, lm, mu, f_lm, f_mu
        )
        logging.debug("new [a, b]: [%.3f, %.3f]", a, b)

    return (a + b) / 2, k


def fibonacci_search(func: Callable[[np.float32], np.float32],
                     a: np.float32, b: np.float32,
                     eps: np.float32,
                     l: np.float32
                     ) -> tuple[np.float32, np.integer]:
    """
    Метод Фибоначчи.
    Метод аналогичен методу золотого сечения. \
    Отличие состоит в том, что коэффициент сжатия интервала \
    неопределенности меняется от итерации к итерации согласно \
    последовательности Фибоначчи.

    Args:
        func (Callable[[np.float32], np.float32]): целевая функция f(x)
        a (np.float32): левая граница интервала неопределенности
        b (np.float32): правая граница интервала неопределенности
        eps (np.float32): константа различимости
        l (np.float32): конечная длина интервала

    Returns:
        tuple[np.float32, np.integer]: tuple[точка минимума, кол-во потребовавшихся итераций]
    """
    assert eps > 0, "'eps' should not be negative"
    assert l > 0, "'l' should not be negative"
    assert b > a, f"invalid interval [{a}, {b}]"

    assert l > 2 * eps, "l must be more than 2 eps"

    logging.debug(
        "starting fibonacci extremum search for %s on interval [%.3f, %.3f] with eps=%f, l=%f",
        func.__name__, a, b, eps, l
    )

    # Вычислить кол-во итераций алгоритма
    n = 1
    fib_n = fibonacci_of(n)
    while not fib_n > (b - a) / l:
        n += 1
        fib_n = fibonacci_of(n)

    # Подготовить массив с числами Фибоначи
    fib: list[np.float32] = fibonacci_seq(n)

    # Шаг 0
    k = 1

    lm = a + fib[n - k - 1] / fib[n - k + 1] * (b - a)
    mu = a + fib[n - k] / fib[n - k + 1] * (b - a)

    f_lm = func(lm)
    f_mu = func(mu)

    while True:
        # Шаг 1
        if f_lm > f_mu:
            # Шаг 2
            a = lm
            #  b = b

            lm = mu
            mu = a + fib[n - k - 1] / fib[n - k] * (b - a)

            if k == n - 2:
                break

            f_lm = f_mu
            f_mu = func(mu)

        # f_lm <= f_mu
        else:
            # Шаг 3
            # a = a
            b = mu

            mu = lm
            lm = a + fib[n - k - 2] / fib[n - k] * (b - a)

            if k == n - 2:
                break

            f_mu = f_lm
            f_lm = func(lm)

        # Шаг 4
        k += 1

        logging.debug(
            "k=%i\n\t    a: %.3f,     b: %.3f\n\t   lm: %.3f,    mu: %.3f\n\tf(lm): %.3f, f(mu): %.3f",
            k, a, b, lm, mu, f_lm, f_mu
        )
        logging.debug("new [a, b]: [%.3f, %.3f]", a, b)

    # Шаг 5
    # lm = lm
    mu = lm + eps

    f_lm = func(lm)
    f_mu = func(mu)

    if f_lm > f_mu:
        a = lm
        # b = b
    else:
        # a = a
        b = lm

    return (a + b) / 2, k


@functools.cache
def fibonacci_of(n: np.integer) -> np.integer:
    """Метод вычисления N-ого числа Фибоначчи

    Args:
        n (np.integer): какое число Фибоначчи нужно вычислить

    Returns:
        np.integer: N-ое число Фибоначчи
    """
    return 1 if n < 2 else fibonacci_of(n - 1) + fibonacci_of(n - 2)


def fibonacci_seq(n: np.integer) -> list[np.integer]:
    """Метод вычисления последовательности чисел Фибоначчи

    Args:
        n (np.integer): сколько чисел Фибоначчи необходимо вычислить

    Returns:
        list[np.integer]: лист с числами Фибоначчи от 0-ого до N-ого (включая N-ое)
    """
    return [fibonacci_of(i) for i in range(n + 1)]
