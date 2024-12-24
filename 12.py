text1 = input("1-Matinni kiriting ") #Birinchi matnni kiriting
text2 = input("2-Matinni kiriting ") #Ikkinchi matnni kiriting

result1 = text2 is text1
print("result1 = ",result1) #Bu yerda 1-matinni chiqarib olamiz 

text2 = text1
result2 = text2 is text1
print("text2: ", result2) #Bu yerda 2-matinni chiqarib olamiz