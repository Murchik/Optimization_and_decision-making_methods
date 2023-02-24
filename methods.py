import logging
from typing import Callable
import numpy as np


def dichotomic_search(func: Callable[[np.float32], np.float32],
                      a: np.float32, b: np.float32,
                      eps: np.float32,
                      l: np.float32
                      ) -> tuple[np.float32, np.integer]:
    # Верхняя (правая) граница интервала должна быть больше чем нижняя (левая)
    assert b > a, f"invalid interval [{a}, {b}]"

    # TODO: !!! Избавиться от бесконечного цикла при l = 2eps !!!
    # l должно быть больше чем 2 * eps, иначе цикл 'while not b - a < l' будет
    # бесконечным, сравнивая 0.X000000000000003 c 0.X
    assert l > 2.0 * \
        eps, f"endless loop because l <= 2eps. l={l}, eps={eps}"

    k = 1
    while not b - a < l:

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

    return a, k

    # TODO: Метод золотого сечения

    # TODO: Метод Фибоначи
