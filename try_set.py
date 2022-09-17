import datetime
from random import randint, random
import random

def main():

    a = [random.randint(0, 100000000) for i in range(1000000)]

    checked_list = [randint(0, 100000000) for i in range(100)]

    start_time = datetime.datetime.now()

    print("##↓---------------------------------------------------↓##")    

    print(f'start_time:{start_time}')

    for temp in checked_list:
        if temp in a:
            print(f'temp:{temp} in a')

    end_time = datetime.datetime.now() - start_time

    print(f'end_time:{end_time}')

    print("---------------------------------------------------")

    b = set(a)

    start_time = datetime.datetime.now()

    print(f'start_time:{start_time}')

    for temp in checked_list:
        if temp in b:
            print(f'temp:{temp} in b')

    end_time = datetime.datetime.now() - start_time

    print(f'end_time:{end_time}')

    print("##↑---------------------------------------------------↑##")


if __name__ == '__main__':
    main()