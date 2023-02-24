import logging
import numpy as np


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Hello World!")

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    idx = 0
    logging.info("a[%s]:%s", str(idx), str(arr[idx]))


if __name__ == "__main__":
    main()
