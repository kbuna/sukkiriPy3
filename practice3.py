


# ifの中身チェック
token = False
#box=(f"{token}")
box = "False"
print(box)

#3-2
day=[20,3,28,39,30,31,33,95]
if [28,30,31] in day: 
    print("aru")
else:
    print("nai")

"""
nai
    if[]
    box=False

aru
    if[1]
    box=[False]
    token = False #box=(f"{token}") 
    box="False"

""" 



#practice3

"""
1 price1.1倍した値が30万以下ならば
2 ×
3 関西リストに"gihu"が含まれていれば
4 a+bが60未満、かつ、dayが3ならば
5 偽判定
  Falseかどうか？

#3-2
1 if initial == "K":
2 if point >=80 and point < 256:
     80 <= point < 256:
3 if bmi < 20 or bmi >25:
4 if year % 4 == 0:
5 if not([28,30,31] in day):
     not(day in [28,30,31]) 


"""




#3-3 (1)
isError = False
n = 20
if isError == False and n <= 100:
    print("hello")

#(2)
num = int(input("数値を入力してください"))
if num %2 ==0:
    print("偶数")
elif num %2 ==1:
    print("奇数")
else:
    print("エラーが起きています")


#(3)
line = input("挨拶してください")
if line=="こんにちは":
    print("ようこそ！")
elif line=="景気は？":
    print("ぼちぼちです！")
elif line=="さようなら":
    print("お元気で！")
else:
    print("どうしました？ヒント：普通に：関西：お別れ")

"""
#3-4
ブロック1 31日まである月
1,3,5,7,8,10,12
ブロック2 ２月を除く
4,6.9,11
ブロック3 2月のみ
2
"""