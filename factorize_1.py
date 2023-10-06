import time


def factorize(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    numbers = [1024, 354, 98, 32, 64, 777]

    start_time = time.time()
    results = {num: factorize(num) for num in numbers}
    end_time = time.time()

    print(f"Результаты: {results}")
    print(f"Время выполнения: {end_time - start_time} секунд")
