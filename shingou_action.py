from enum import Enum
import sys

class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(color):

    if color in (data.value for data in Shingou):
        raise Exception("信号機の色に対応していません")

    shingou = Shingou(color)

    #信号の色で処理を変える
    if shingou is Shingou.RED:
        print('とまれ')
    elif shingou is Shingou.BLUE:
        print('すすめ')
    elif shingou is Shingou.YELLOW:
        print('ちゅうい')

    return shingou