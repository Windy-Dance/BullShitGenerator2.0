# coding : utf-8
# Author : Parallel
# Create On
import random

import read

boshes = read.readJSON("data.json")
bosh = boshes['bosh']
famous = boshes['famous']
pb = boshes['poemb']
pa = boshes['poema']
cb = boshes['cysb']
ca = boshes['cysa']
before = boshes['before']
after = boshes['after']
end = boshes['end']

with open("cybash.txt", "r", encoding="utf-8") as f:
    cy = f.readlines()
with open("sentence.txt", "r", encoding="utf-8") as f:
    sent = f.readlines()
with open("poem.txt", "r", encoding="utf-8") as f:
    poem = f.readlines()


def random_it(lists):
    pool = list(lists) * 2
    while True:
        random.shuffle(pool)
        for element in pool:
            yield element


let_bosh = random_it(bosh)
let_famous = random_it(famous)
let_poem = random_it(poem)
let_cy = random_it(cy)
let_sent = random_it(sent)


def add_famous():
    xx = next(let_famous)
    xx = xx.replace("a", random.choice(before))
    xx = xx.replace("b", random.choice(after))
    return xx


def add_poem():
    xx = next(let_poem)
    while xx == "":
        xx = next(let_poem)
    xx = random.choice(pb) + xx + random.choice(pa)
    return xx.replace("\n", "")


def add_cy():
    xx = next(let_cy)
    xx = random.choice(cb) + xx + random.choice(ca)
    xx = xx.replace("\n", "")
    xx = xx.replace("\ufeff", "")
    return xx


def add_sent():
    xx = next(let_sent)
    return xx.replace("\n", "")


def next_line():
    line = " "
    line += "\r\n"
    line += "    "
    return line


def main():
    title = str(input("输入你的文章主题："))
    num = int(input("请输入文章字数："))
    tmp = str("    ")
    line = ""

    while len(tmp) < num:
        tree = random.randint(1, 280)
        if tree < 8:
            line += next_line()
        elif tree < 40:
            line += add_famous()
        elif tree < 100:
            line += add_sent()
        elif tree < 140:
            line += add_cy()
        elif tree < 190:
            line += add_poem()
        else:
            line += next(let_bosh)
        tmp += line
        line = ""

    random.shuffle(end)
    end_of_passage = random.choice(end)
    tmp = tmp + "\n" + end_of_passage
    tmp = tmp.replace("x", title)
    print(tmp, flush=True)

    you = str(input("要导出为txt文件么?(y/n)"))
    if you.lower() == "y":
        you = str(input("输入文件名称："))
        with open(f"{you}.txt", "a+", encoding="utf-8") as g:
            g.write(tmp)
        you = input("文件已经保存成功，按下回车退出...")
    else:
        you = input("好的，按下回车退出...")


if __name__ == '__main__':
    main()