country = input('請輸入國家:')
age = input('請輸入年齡:') #input會自動把輸入變成字串(加上'')
age = int(age) #casting型別轉換，轉換成整數ｉｎｔ
if country == '台灣':
    if age >= 20 : 
        print('民法完全行為能力人')
    elif age >= 7 and age <= 20 :
        print('限制行為能力人')
    else:
        print('無行為能力人')
else:
    print('尼ㄅ4逮丸倫ㄛ')