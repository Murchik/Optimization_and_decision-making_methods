import logging
from typing import Callable
import numpy as np


def dichotomic_search(func: Callable[[np.float32], np.float32],
                      a: np.float32, b: np.float32,
                      eps: np.float32,
                      l: np.float32
                      ) -> tuple[np.float32, np.integer]:
    assert b > a, f"invalid interval [{a}, {b}]"
    assert 2 * eps > 0

    logging.debug(
        "starting extremum search for %s on interval [%.3f, %.3f] with eps=%f, l=%f",
        func.__name__, a, b, eps, l
    )

    k = 1
    # Если идти до значения <= 2*eps, то будет бесконечный цикл
    while b - a > (2 + eps) * eps:
        if b - a < l:
            break

        lm = (a + b) / 2 - eps
        mu = (a + b) / 2 + eps

        f_lm = func(lm)
        f_mu = func(mu)

        logging.debug(
            "k=%i\n\ta:  %.3f, b:  %.3f\n\tlm: %.3f, mu: %.3f\n\tf(lm): %.3f, f(mu): %.3f",
            k, a, b, lm, mu, f_lm, f_mu
        )

        if f_lm < f_mu:
            # a = a
            b = mu
        else:
            a = lm
            # b = b

        logging.debug("new [a, b]: [%.3f, %.3f]", a, b)
        logging.debug("%.3f < %.3f? - %r]", b - a, l, (b - a < l))

        k += 1

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
