
# クエスチョンメソッド

print("すべての質問にyまたはnで答えて下さい")


#
class Question:
    #パッシブな状態
    hasMoney = ""
    #現在の状態
    isHungry = ""
    isDrink = ""
    isSnack = ""
    


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


