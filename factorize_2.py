import multiprocessing
import time


def factorize(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def parallel_factorize(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize, numbers)
        return results


if __name__ == "__main__":
    numbers = [1024, 354, 98, 32, 64, 777]

    start_time = time.time()
    results = parallel_factorize(numbers)
    end_time = time.time()

    print(f"Результаты: {results}")
    print(f"Время выполнение: {end_time - start_time} секунд")
