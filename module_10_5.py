import multiprocessing
from datetime import datetime



def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.now()

    for filename in filenames:
        read_info(filename)

    end = datetime.now()
    print(f"{end - start} (линейный)")

    with multiprocessing.Pool(processes=8) as pool:
        start_1 = datetime.now()
        pool.map(read_info, filenames)
    end_1 = datetime.now()
    print(f"{end_1 - start_1} (многопроцессный)")