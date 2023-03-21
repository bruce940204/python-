#TEST
school1=("實踐大學")
school2=("逢甲大學") 
school3=("金門大學")
school4=("文化大學")
school5=("元智大學")
school6=("高雄科技應用大學")
local=int(input("(1:高雄 2:台中 3:桃園 4:台北 5:金門) 請輸入你的縣市: "))
if local==1:
    print(school1,school6)
elif local==2:
    print(school2)
elif local==3:
    print(school5)
elif local==4:
    print(school4)
else:
    print(school3)


#後期資料統一彙整輸出
if local==1:
    print('你的學校:%s' %school1,school6)
elif local==2:
    print('你的學校:%s' %school2)    
elif local==3:
    print('你的學校:%s' %school5)
elif local==4:
    print('你的學校:%s' %school4)
else:
    print('你的學校:%s' %school3)











