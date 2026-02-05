#仮想環境に入るコマンド
#source /home/haru/dev/bayby/venv/bin/activate

#プロジェクトフォルダにいる時
#cd /home/haru/dev/bayby
#source venv/bin/activate

#成功するとvenvになる
#(venv) haru@haru-pc:~/dev/bayby$

#仮想環境を無効化する時
#deactivate

print("hello world")

a = 2
b = 3
print(a * b)

#足し算
c = int(input("数字を入力: "))
d = int(input("数字を入力: "))
print(c + d)

#エラーチェック
e = input("数字を入力: ")
f = input("数字を入力: ")

if not e.isdigit():
    print("⭐️" * len(e))
elif not f.isdigit():
    print("⭐️" * len(f))
else:
    e = int(e)
    f = int(f)
    print(e + f)

text = input("なにか入力する: ")
print("⭐️" * len(text))