#現在の作業ディレクトリに効果音のファイルを格納してください
# pip install pygame を実行してください
#!テスト完了
import random
import pygame

I_class_number = [42, 43, 38, 37, 40]#!各クラス人数入力
max_population = 0
for i in range(0, 4):
    if max_population < I_class_number[i]:
        max_population = I_class_number[i]

I_table = [[0 for i in range(max_population+1)] for j in range(6)]

def proportion(percent_all, percent_1I):
    if percent_all < percent_1I:
        print("異常な数値です")
        return -1
    else:
        return (percent_all-percent_1I)/4

def judge(grade):
    while True:
        number = random.randint(1, I_class_number[grade-1])
        if I_table[grade][number] != 0:
            pass
        else:
            I_table[grade][number]=1
            pygame.mixer.init()
            #pygame.mixer.music.load('nc38022.mp3') #('効果音のファイル名')
            #pygame.mixer.music.play()
            print(grade, end="")
            print('I', end="")
            print(number)
            break

def judge_grade(grade):
    judge_i = False
    for i in range(1, I_class_number[grade-1]+1):
        if I_table[grade][i] == 0:
            judge_i = True
            break
    if judge_i:
        judge(grade)
        return True
    else:
        return False


percent_all = 100#*全ての確率
percent_1I = 22#*1iの確率
percent_other = int(proportion(percent_all, percent_1I))

while True:
    get_key = input()
    if get_key == "":
        grade_random = random.randint(1,percent_all)
        if  grade_random <= percent_1I:
            if judge_grade(1) == False:
                pass
        elif grade_random <= percent_1I+percent_other:
            if judge_grade(2) == False:
                pass
        elif grade_random <= percent_1I+2*percent_other:
            if judge_grade(3) == False:
                pass
        elif grade_random <= percent_1I+3*percent_other:
            if judge_grade(4) == False:
                pass
        elif grade_random <= percent_all:
            if judge_grade(5) == False:
                pass
