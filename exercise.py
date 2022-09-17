from enum import Enum
import sys

class DAY_list(Enum):
    DAY_MONDAY = 2
    DAY_TUESDAY = 3
    DAY_WEDNESDAY = 4
    DAY_THURSDAY = 5
    DAY_FRIDAY = 6
    DAY_SATURDAY = 7
    DAY_SUNDAY =  1

def test(check):
    
    for temp in (data.value for data in DAY_list):

        if temp == check:
            break

        print(temp)

if __name__ == "__main__":
    args = sys.argv
    test(int(args[1]))