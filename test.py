'''
FizzBuzzの拡張として、複数の(整数i , 文字列s)のペアと一つの整数mが渡され、
mがiの倍数ならsを出力するプログラムを作成しなさい。

sはiの小さい順に出力してください(※iが小さい順に並んでいるとは限りません)
どのsも出力されなければmを出力してください
入力は"input.txt"を読み込みます
iとsのペアは"input.txt"に一行ずつ"i:s"形式で渡されます
mは"input.txt"の下から２番目の行で渡されます
"input.txt"の最終行は空行です
'''



dic = {}
lst = []
#ファイルの読み込み
f = open("input.txt", "r", encoding="utf_8")
while True:
  #ファイルを１行ずつ出力
  line = f.readline()
  if line:
    #文字列に「：」が含まれている時の処理
      if line.find(':') != -1:
        num, word = line.split(':')
        num = int(num)
        word = word.replace('\n' , '')
        dic[num] = word
        lst.append(num)
    #文字列に「：」が含まれていない時の処理
      else:
        m = int(line)
  else:
    break


ans = ''
sort_lst = sorted(lst)#配列のソート
for i in sort_lst:#FizzBuzz
  if m % i == 0:
    ans+=dic[i]

if ans == '':#FizzBuzz処理でどの数に対しても割り切れなかった時
  print(m)
else:#文字列（ans）の出力
  print(ans)
