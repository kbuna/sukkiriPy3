

class Question:
    def check():
        if self.hasMoney == "y":
            self.isHungry = input("お腹がすごく空いてますか？ >>")
            self.isDrink = input("ビールを飲みたいですか？ >>")

            if self.isHungry == "y" and self.isDrink == "y":
                print("焼肉はいかがですか")
            elif self.isHungry == "y":
                print("カレーはいかがですか")
            elif self.isDrink == "y":
                print("焼き鳥はいかがですか")
            else:
                print("パスタはいかがですか")

            self.isSnack = input("夜食は必要ですか？ >>")
            if self.isSnack == "y":
                print("コンビニのチキンはいかがですか")
        else:
            print("家で食べましょう")

