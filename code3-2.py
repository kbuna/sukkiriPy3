#3-2
name = input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")
food = input(f"{name}さんの好きな食べ物を教えてください>>")
if food == "カレー":
    print("素敵です。カレーは最高ですよね！")
else:
    print(f"私も{food}が好きですよ")


print()

#3-3　ブロックとインデント
score = int(input("試験の点数を入力してください>>"))
if score >= 60:
    print("合格!")
    print("よく頑張りましたね！")
else:
    print("残念ながら不合格です")
    print("追試を受けてください")

print()

#3-4 in演算子
name = input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")
food = input(f"{name}さんの好きな食べ物を教えてください>>")
if "カレー" in food:
    print("素敵です。カレーは最高ですよね！")
else:
    print(f"私も{food}が好きですよ")

print()



#3-5 リスト内に含まれているか
scores =[80,100,20,60]
if 100 in scores:
    print("100点満点の試験があったんですね、おめでとう!")
else:
    print("次はどれか1つでも100点をとろう")

  
print()


#3-6 ディクショナリーのキーをチェックする
scores ={"network":60,"database":80,"security":50}

key = input("追加する科目名を入力してください>>")
if key in scores:
    print("すでに登録済みです")
else:
    data = int(input("得点を入力してください>>"))
    scores[key] =data
print(scores)

print()


#3-7 条件式の評価結果を確認する
score = int(input("試験の点数を入力>>"))
print(score >= 60)

print()


"""
# pythonの True Falseは大文字

# 論理演算子 and or not 

if score >= 60 and score <= 100:
if score < 60 or score > 100:
if not(score < 60 or score > 100):

if 60 <= score <=100:

# 真偽値に評価されない条件式
score = 0
if score:
    #
else:
    #

#条件式の結果が真偽値にならない場合、
#0ならfalse、0以外はtrueと解釈してそれぞれのブロックを実行する
# 他にも             False None 0 0.0 
# 空の文字列　       " "" 
# 空のコレクション   [] {} ()
# はfalseとして判断される

"""

#3-8 elseブロックのない分岐

name=input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")

if name == "松田":
    print("松田さんに会えてうれしいです")
else:
    pass

food = input(f"{name}さんの好きな食べ物を教えてください>>")
if "カレー" in food:
    print("素敵です。とにかくカレーは最高ですよね！")
else:
    print(f"私も{food}が好きですよ")

# 3-9 if-elif構文 多分岐するif文
score= int(input("試験の点数を入力してください >>"))
if score < 0 or score >100:
    print("異常な得点です")
    print("入力しなおしてください")
elif score >= 60:
    print("合格！")
    print("よく頑張りましたね！")
else:
    print("残念ながら不合格です")
    print("追試を受けてください")

# 3-10 
print("すべての質問にyまたはnで答えて下さい")
okane_aruka = "y"
if okane_aruka == "y":
    onaka_suiteruka = input("お腹がすごく空いてますか？ >>")
    nomitai_kibunka = input("ビールを飲みたいですか？ >>")
    if onaka_suiteruka == "y" and nomitai_kibunka == "y":
        print("焼肉はいかがですか")
    elif onaka_suiteruka == "y":
        print("カレーはいかがですか")
    elif nomitai_kibunka == "y":
        print("焼き鳥はいかがですか")
    else:
        print("パスタはいかがですか")
    yashoku_iruka = input("夜食は必要ですか？ >>")
    if yashoku_iruka == "y":
        print("コンビニのチキンはいかがですか")
else:
    print("家で食べましょう")


# 3-10 
print("すべての質問にyまたはnで答えて下さい")

hasMoney= "y"

if  hasMoney== "y":
    isHungry = input("お腹がすごく空いてますか？ >>")
    isDrink = input("ビールを飲みたいですか？ >>")

    if isHungry == "y" and isDrink == "y":
        print("焼肉はいかがですか")
    elif isHungry == "y":
        print("カレーはいかがですか")
    elif isDrink == "y":
        print("焼き鳥はいかがですか")
    else:
        print("パスタはいかがですか")

    isSnack = input("夜食は必要ですか？ >>")
    if isSnack == "y":
        print("コンビニのチキンはいかがですか")

else:
    print("家で食べましょう")





