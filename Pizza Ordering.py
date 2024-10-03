print("====SELAMAT DATANG DI PIZZA HUT DARDERDOR ^^==== \n")
print("Kami menyediakan pizza dengan berbagai topping")
print("Topping yang kami miliki adalah:")
print("mozzarella cheese, papperoni, pineapples, dan chicken breast")



topping = input("Silahkan, mau pilih topping apa? ")
if topping == "mozzarella cheese":
    print("Baik, untuk topping yang dipilih mozzarella cheese. \n")
    HargaTopping = 50000
elif topping == "papperoni":
    print("baik, untuk topping yang dipilih papperoni. \n")
    HargaTopping = 55000
elif topping == "pineapples":
    print("Baik, untuk topping yang dipilih pineapples. \n")
    HargaTopping = 45000
elif topping == "chicken breast":
    print("Baik, untuk topping yang dipilih chicken breast. \n")
    HargaTopping = 60000
else:
    print("maaf, kami tidak menyediakan topping itu. \n")
    


print("Untuk crust pizza, kami mempunyai:")
print("pan, thin, dan stuffed crust ")
crust = input("Untuk crust pizza? ")
if crust == "pan":
    print("Oke, pan crust . \n")
    HargaCrust = 25000
elif crust == "thin":
    print("oke, thin crust \n")
    HargaCrust = 35000
elif crust == "stuffed crust":
    print("oke, stuffed crust. \n")
    HargaCrust = 40000
else:
    print("Maaf, kami tidak menyediakan crust tersebut. \n")


print("Untuk ukuran kami menyediakan ukuran:")
print("small, medium, dan large")
size = input("Ukuran apa yang diinginkan? ")
if size == "small":
    print("Siap, pizza dengan ukuran small \n")
    HargaSize = 65000
elif size == "medium":
    print("Siap, pizza dengan ukuran medium \n")
    HargaSize = 80000
elif size == "large":
    print("Siap, pizza dengan ukuran large \n")
    HargaSize = 100000
else:
    print("maaf, kami tidak menyediakan ukuran tersebut. \n")


tambahan = input("Mau tambahan topping cheese?(ya/tidak) ")
if tambahan == "ya":
    print("Baik, dengan tambahan cheese \n")
    HargaTambahan = 13000
else:
    print("Baiklah, tanpa tambahan cheese \n")
    HargaTambahan = 0


HargaTotal = int(HargaTopping) + int(HargaCrust) + int(HargaSize) + int(HargaTambahan)
print("Total harganya sebesar Rp.", HargaTotal)
print("Terimakasih sudah memesan pizza kami, selamat menikmati :) ")