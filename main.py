import os
import glob
import logging
from typing import Callable
import numpy as np
import methods
from prettytable import PrettyTable


SAVE_PATH = "./results"


def save_table(path: str, filename: str, table: PrettyTable):
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/{filename}.csv", "w", encoding="UTF-8") as f:
        f.write(table.get_csv_string())


def apply_method(
    method: Callable,
    func: Callable,
    a: np.float32, b: np.float32,
    eps: np.float32, l: np.float32
) -> None:
    print(
        f"{method.__name__} for {func.__doc__} with a={a}, b={b}, eps={eps}, l={l}"
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
    print(
        f"Found x={result:.4f}, f(x)={func(result):.4f}, func_calls={func_calls}\n"
    )

    save_table(
        path=SAVE_PATH,
        filename=f"{method.__name__}_{func.__name__}_a{a}_b{b}_eps{eps}_l{l}",
        table=table
    )


def func1(x: np.float32) -> np.float32:
    """f(x) = (x - 4)/(x - 9)"""
    if np.isclose(x, 9):
        return np.finfo(np.float32).max
    return (x - 4)/(x - 9)


def func2(x: np.float32) -> np.float32:
    """f(x) = |x^2 - 1|"""
    return np.abs(np.power(x, 2) - 1)


def main():
    logging.basicConfig(level=logging.INFO)

    os.makedirs(SAVE_PATH, exist_ok=True)
    # Очистить директорию, если в ней есть файлы
    if len(os.listdir(SAVE_PATH)) != 0:
        files = glob.glob(f"{SAVE_PATH}/*", recursive=True)
        for f in files:
            os.remove(f)

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
