price = float(input ("Tovar narxini kiriting = "))
discount = float (input ("Chegirma foizini kiriting = "))

# Maxsulot chegirmasi hisoblandi
pay = price * discount / 100
to_pay = price - pay 

# Bajarilgan ammalar terminalga chiqarildi
print(to_pay)