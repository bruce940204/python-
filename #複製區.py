#複製區
school1=("m:實踐大學")
school2=("n:逢甲大學") 
school3=("o:金門大學")
school4=("p:文化大學")
school5=("q:元智大學")
school6=("r:高雄科技應用大學")
print(school1,school2,school3,school4,school5,school6)


department=input 
m=("m1","m2","m3","m4","m5","m6","m7","m8","m9","m10")
n=("n1","n2","n3","n4","n5","n6","n7","n8","n9","n10")
o=("o1","o2","o3","o4","o5","o6","o7","o8","o9","o10")
p=("p1","p2","p3","p4","p5","p6","p7","p8","p9","p10")
q=("q1","q2","q3","q4","q5","q6","q7","q8","q9","q10")
r=("r1","r2","r3","r4","r5","r6","r7","r8","r9","r10")



for local in range(0,6):
    if local>1 and local<=2:
        print(school2)
for local in range(0,6):
    if local>2 and local<=3:
        print(school5)
for local in range(0,6):
    if local>3 and local<=4:
        print(school4)
for local in range(0,6):
    if local>4 and local<=5:
        print(school3)


file=open("test.py",mode="r")
print(file.read())
file.close()


import subprocess
subprocess.call("test.py", shell=True)