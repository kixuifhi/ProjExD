import random
def main():
    seikai = syutudai()
    kaitou(seikai)

def syutudai():
    qas = [
        {"q":"サザエの旦那の名前は?","a":["マスオ","ますお","益男"]},
        {"q":"カツオの妹の名前は?","a":["わかめ","ワカメ"]},
        {"q": "タラオはカツオから見てどんな関係?","a":["甥","おい"]},
    ]

    r = random.randint(0,2)
    print(qas[r]["q"])
    return qas[r]["a"]

def kaitou(seikai):
    ans = input("答えるんだ:")
    if ans in seikai:
        print("正解")

    else:
        print("不正解")

if __name__ == "__main__":
    main()

