import logging
import numpy as np
import methods


def func1(x: np.float32) -> np.float32:
    return (x - 4)/(x - 9)


def func2(x: np.float32) -> np.float32:
    return np.abs(np.power(x, 2) - 1)


def main():
    logging.basicConfig(level=logging.INFO)

    funcs = [func1, func2]
    intervals = [
        [[-3, 0], [-3, 9], [9, 15]],  # Интервалы для функции 1
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
                    try:
                        result, iterations = methods.dichotomic_search(
                            func=func, a=a, b=b, eps=eps, l=l
                        )
                        logging.info(
                            "extremum for %s on [%.3f, %.3f] is %.3f. Iterations: %i",
                            func.__name__, a, b, result, iterations
                        )
                    except AssertionError as err:
                        logging.error("%s", str(err))
                    continue


if __name__ == "__main__":
    main()
