# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur. 
with open("C:/Users/Administrator/Desktop/python_temelleri/dosyaYonetimi I-0/newfile.txt","w",encoding="UTF-8") as file:
    file.write("Çınar Turan\n")
    file.write("Sadık Turan\n")
    file.write("Sena Turan")
    print(file)

with open("C:/Users/Administrator/Desktop/python_temelleri/dosyaYonetimi I-0/newfile.txt") as file:
    print(file.read())