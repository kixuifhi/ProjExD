
import random
#alphabet = ['a','b','c','d','e'fghijklmnopqrstuvwxyz]
alphabet = [chr(ord("a")+i) for i in range(26)]
ending = 5
num = 10
minus = 2
count = 0


def main():
    seikai = quiz()
    kaitou(seikai)

def quiz():
    alphabet = [chr(ord("A")+i) for i in range(26)]
    t1 = random.sample(alphabet,k=num)
    t2 = random.sample(t1,len(t1)-minus)
    t3 = 
    m1 = "対象文字:"
    m2 = "欠損文字"
    print(m1)
    print(t1)
    print(m2)
    print(t2)
    return 


def kaitou(seikai):
    ans = input("欠損文字はいくつあるでしょうか?")
    ans2 = int(ans)
    if ans2 == minus:
        print("正解です。具体的な文字を")
        ans11 = input("1つ目の文字を入力してください")
        if ans11 in seikai:
            ans12 = input("2つ目の文字を入力してください")
            if ans12 in seikai:
                print("正解です。(終了。)")
            else:
                print("不正解")
        else:
            print("不正解")
            
    else:
        print("不正解です、またチャレンジしてください")
        while count < ending:
            main()
            count +=1
            if count > ending:
                break

if __name__ == "__main__":
    main()