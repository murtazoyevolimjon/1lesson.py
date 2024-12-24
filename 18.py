Phone_number = input("Telefon raqam kiriting(Namuna: 885790309): ") #Telefon raqamimzni kiritib olamiz 
result = "+998 (" + phone_number[0:2] + ")-" + phone_number[2:5] + "-" + phone_number[5:7] + "-" + phone_number[7:9] #Va kiritgan telefon raqamizni boshiga +998 qo'shib olamiz
print("Result:", result) #Va natijani chiqaramiz 
