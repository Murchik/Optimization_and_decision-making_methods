import logging
from typing import Callable
import numpy as np
import methods


def func1(x: np.float32) -> np.float32:
    if np.isclose(x, 9):
        return np.finfo(np.float32).max
    return (x - 4)/(x - 9)


def func2(x: np.float32) -> np.float32:
    return np.abs(np.power(x, 2) - 1)


def apply_method(
    method: Callable,
    func: Callable,
    a: np.float32, b: np.float32,
    eps: np.float32, l: np.float32
) -> None:
    print(
        f"{method.__name__} for {func.__name__} with a={a}, b={b}, eps={eps}, l={l}"
    )

    try:
        result, func_calls, table = method(
            func=func, a=a, b=b, eps=eps, l=l
        )
    except AssertionError as err:
        logging.error("%s\n", str(err))
        return

    table.float_format = ".3"
    print(table)
    print(f"Found x={result}, func_calls={func_calls}\n")


def main():
    logging.basicConfig(level=logging.INFO)

    funcs = [func1, func2]
    intervals = [
        [[-3, 0],  [-3, 9], [9, 15]],  # Интервалы для функции 1
        [[-10, 1], [-2, 0], [-2, 8]]  # Интервалы для функции 2
    ]
    epses = [0.1, 0.01, 0.001]
    ls = [0.1, 0.01]

    for idx, func in enumerate(funcs):
        for interval in intervals[idx]:
            a = interval[0]
            b = interval[1]
            for eps in epses:
                for l in ls:
                    apply_method(
                        method=methods.dichotomic_search, func=func,
                        a=a, b=b,
                        eps=eps, l=l
                    )
                    apply_method(
                        method=methods.golden_search, func=func,
                        a=a, b=b,
                        eps=eps, l=l
                    )
                    apply_method(
                        method=methods.fibonacci_search, func=func,
                        a=a, b=b,
                        eps=eps, l=l
                    )


if __name__ == "__main__":
    main()
