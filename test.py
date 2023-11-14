from Question import Question as Q




"""

人は、状態を持っている

メイン
    質問をする




アンサー
クエスチョン

・ステートは各種ブーリアンを持つ


アンサー
・入力がyかnならT、それ以外ならF


・質問文は
  input()で、質問文を表示させる
  アンサーで、正規化する
  アンサー結果をブーリアンに変換する



"""


print("すべての質問にyまたはnで答えて下さい")

#オブジェクト
class Answer:

    def ans2(str):
        canAnswer = ans(str)
        if canAnser:
            return True
        else:
            print("入力が間違っています")
            return False



    def ans(str):
        if str=="y":
            return True
        elif str=="n":
            return True
        else:
            return False

#値
questionText=""


# アンサー関数
Answer.ans(input(f"{questionText}"))

# クエスチョン関数
q = Q()
q.check()



def boolTrigger():
    
    def __init__(self):
        # インスタンス変数にデフォルト値を与える
        self.hasMoney = ""
        self.isHungry = ""
        self.isDrink = ""
        self.isSnack = ""



