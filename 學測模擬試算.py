
a=float(input("請輸入你的 國文 級分: "))
b=float(input("請輸入你的 數 A 級分: "))
c=float(input("請輸入你的 英文 級分: "))
d=float(input("請輸入你的 自然 級分: "))
e=float(input("請輸入你的 數 B 級分: "))
f=float(input("請輸入你的 社會 級分: "))
number="你的倍率換算: ",round((a)/15*100,2),round((b)/15*100,2),round((c)/15*100,2),round((d)/15*100,2),round((e)/15*100,2),round((f)/15*100,2)
print(number)
school1=("11:實踐大學")
school2=("22:逢甲大學") 
school3=("33:金門大學")
school4=("44:文化大學")
school5=("55:元智大學")
school6=("66:高雄科技應用大學")
locals=("1:高雄 2:台中 3:桃園 4:台北 5:金門")
print(locals)
local=int(input("請輸入你的縣市: "))
if local==1:
    print(school1,school6)
elif local==2:
    print(school2)
elif local==3:
    print(school5)
elif local==4:
    print(school1,school4)
else:
    print(school3)
schools=int(input("請輸入你的學校:"))

if schools==11:
   import subprocess
   subprocess.call("school1.py", shell=True)
elif schools==22:
   import subprocess
   subprocess.call("school2.py", shell=True)
elif schools==33:
   import subprocess
   subprocess.call("school3.py", shell=True)
elif schools==44:
   import subprocess
   subprocess.call("school4.py", shell=True)
elif schools==55:
   import subprocess
   subprocess.call("school5.py", shell=True)
else:
   import subprocess
   subprocess.call("school6.py", shell=True)







