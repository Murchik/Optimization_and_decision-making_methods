import functools
from typing import Callable
import numpy as np
from prettytable import PrettyTable


def dichotomic_search(func: Callable[[np.float32], np.float32],
                      a: np.float32, b: np.float32,
                      eps: np.float32,
                      l: np.float32
                      ) -> tuple[np.float32, np.integer, PrettyTable]:
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
        tuple[np.float32, np.integer]: tuple[точка минимума, кол-во вызовов функции, таблица со значениями переменных на каждом шаге]
    """
    assert eps >= 0, "'eps' should not be negative"
    assert l >= 0, "'l' should not be negative"
    assert b > a, f"invalid interval [{a}, {b}]"

    assert l > 2 * eps, "l must be more than 2 eps"

    table = PrettyTable()
    table.field_names = ["k", "a", "b", "lm",  "mu", "f(lm)", "f(mu)"]

    func_calls = 0

    # Начальный этап
    k = 1

    # Основной этап
    while True:
        # Шаг 1
        if b - a < l:
            break
        lm = (a + b) / 2 - eps
        mu = (a + b) / 2 + eps

        # Шаг 2
        f_lm = func(lm)
        f_mu = func(mu)
        func_calls += 2

        table.add_row([k, a, b, lm, mu, f_lm, f_mu])

        if f_lm < f_mu:
            # a = a
            b = mu
        else:
            a = lm
            # b = b

        # Шаг 3
        k += 1

    return (a + b) / 2, func_calls, table


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
        tuple[np.float32, np.integer]: tuple[точка минимума, кол-во вызовов функции, таблица со значениями переменных на каждом шаге]
    """
    assert eps >= 0, "'eps' should not be negative"
    assert l >= 0, "'l' should not be negative"
    assert b > a, f"invalid interval [{a}, {b}]"

    table = PrettyTable()
    table.field_names = ["k", "a", "b", "lm",  "mu", "f(lm)", "f(mu)"]

    func_calls = 0
    alpha = (np.sqrt(5) - 1) / 2  # 0.61803...

    # Начальный этап
    k = 1

    lm = a + (1 - alpha) * (b - a)
    mu = a + alpha * (b - a)

    f_lm = func(lm)
    f_mu = func(mu)
    func_calls += 2

    # Основной этап
    while True:
        table.add_row([k, a, b, lm, mu, f_lm, f_mu])

        # Шаг 1
        if b - a < l:
            break

        if f_lm > f_mu:

            # Шаг 2
            a = lm
            # b = b

            lm = mu
            f_lm = f_mu

            mu = a + alpha * (b - a)
            f_mu = func(mu)
            func_calls += 1

        # f_lm <= f_mu
        else:

            # Шаг 3
            # a = a
            b = mu

            mu = lm
            f_mu = f_lm

            lm = a + (1 - alpha) * (b - a)
            f_lm = func(lm)
            func_calls += 1

        # Шаг 4
        k += 1

    return (a + b) / 2, func_calls, table


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
        tuple[np.float32, np.integer]: tuple[точка минимума, кол-во вызовов функции, таблица со значениями переменных на каждом шаге]
    """
    assert eps > 0, "'eps' should not be negative"
    assert l > 0, "'l' should not be negative"
    assert b > a, f"invalid interval [{a}, {b}]"

    table = PrettyTable()
    table.field_names = ["k", "a", "b", "lm",  "mu", "f(lm)", "f(mu)"]

    func_calls = 0

    # Начальный этап
    k = 1

    # Вычислить кол-во итераций алгоритма
    n = 1
    fib_n = fibonacci_of(n)
    while not fib_n > (b - a) / l:
        n += 1
        fib_n = fibonacci_of(n)

    # Подготовить массив с числами Фибоначи
    fib: list[np.float32] = fibonacci_seq(n)

    lm = a + fib[n - 2] / fib[n] * (b - a)
    mu = a + fib[n - 1] / fib[n] * (b - a)

    f_lm = func(lm)
    f_mu = func(mu)
    func_calls += 2

    # Основной этап
    while True:
        table.add_row([k, a, b, lm, mu, f_lm, f_mu])

        # Шаг 1
        if f_lm > f_mu:

            # Шаг 2
            a = lm
            #  b = b
            lm = mu
            f_lm = f_mu

            mu = a + fib[n - k - 1] / fib[n - k] * (b - a)

            if k == n - 2:
                break

            f_mu = func(mu)
            func_calls += 1

        # f_lm <= f_mu
        else:

            # Шаг 3
            # a = a
            b = mu
            mu = lm
            f_mu = f_lm

            lm = a + fib[n - k - 2] / fib[n - k] * (b - a)

            if k == n - 2:
                break

            f_lm = func(lm)
            func_calls += 1

        # Шаг 4
        k += 1

    # Шаг 5
    k += 1

    # lm = lm
    mu = lm + eps

    # f_lm = func(lm)
    f_mu = func(mu)
    func_calls += 1

    table.add_row([k, a, b, lm, mu, f_lm, f_mu])

    if f_lm > f_mu:
        a = lm
        # b = b
    else:
        # a = a
        b = lm

    return (a + b) / 2, func_calls, table


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
