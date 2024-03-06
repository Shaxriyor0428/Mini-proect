from json import loads,dumps

class UseRepsit:
    def __init__(self,myFile):
        self.myFile = myFile
    
    def readFileJson(self):
        if not self.myFile:
            print("Bosh fayl ")
        with open(self.myFile,"r") as file:
            cover = file.read()
            data = loads(cover)
            return data
        
    def addNewUser(self):
        converted = self.readFileJson()
        if converted:
            newId = converted[-1]["user_id"] +1
        else:
            newId = 1
        qoshil = {
            "user_id":newId,
            "first_name" :input("first name: "),
            "last_name":input("last name: "),
            "age" :  int(input("age: "))
        }
        converted.append(qoshil)
        yangi = dumps(converted,indent=4)
        with open(self.myFile,"w") as d1:
            d1.write(yangi)
            print("Muvvafaqiyatli qo'shildi! ")

    
    def deleteId(self):
        delet = int(input("o'chirmoqchi bo'lgan Id ni kirit: "))
        try :
            if delet <= 100 and delet >= 1:
                hisob = self.readFileJson()
                found = False
                i = 0
                while i < len(hisob):
                    if hisob[i]["user_id"] == delet:
                        del hisob[i]
                        newFile = dumps(hisob,indent=4)
                        with open(self.myFile,"w") as file:
                            file.write(newFile)
                        print("Successfully deleted!")
                        found =True
                        break
                    else:
                        i += 1
                if not found:
                    print("BUnday Id yoq")
            else:
                print("Yoshi 1 dan katta va 100 dan kichik kirit:")
        except ValueError as err:
            print("yosh kiritishda xatolik",err)


    def gitOneId(self):
        dat = self.readFileJson()
        getId = int(input("olmoqchi bolgan ID ni kiriting: "))
        for i in range(len(dat)):
            if dat[i]["user_id"] == getId:
                print(dat[i])
                break
        else:
            print("Bunday Id mavjud emas")


    def oneUserChange(self):
        converted = self.readFileJson()
        tanla = int(input("o'zgartirmoqchi bo'lgan Userni tanlang "))
        try :
            for i in range(len(converted)):
                if converted[i]["user_id"] == tanla:
                    converted[i]["user_id"] = converted[i]["user_id"]
                    converted[i]["first_name"] = input("first name: ")
                    converted[i]["last_name"] = input("last name: ")
                    converted[i]["age" ] = int(input("age: "))
                    yangi = dumps(converted,indent=4)
                    with open(self.myFile,"w") as f:
                        f.write(yangi)
                    print("Muvvafaqiyatli o'zgartirildi!")
                    break 
            else:
                print("Bunday Id yo'q! ")


        except ValueError as error:
            print("xatolik ozgaritishda",error)

obj = UseRepsit("user.json")
from os import system
from time import sleep
print("Shaxriyor Ziyodullayevning mini proekting xush kelibsiz! ")
while True:
    print("""
    1. Yangi User qo'shish
    2. Userni Id si bo'yicha o'chirish
    3. Bitta Userni Id bo'yicha olish
    4. Bitta Userni ID bo'yicha o'zgaritirish
    5. Chiqish ! chiqish uchun 5 ni tanlang
            
    """)
    try :

        choose = input("tanlang:  ")
        if not choose.isdigit() :
            print("iltimos raqam kiriting!!! ")
            continue
        else:
            choose = int(choose)
            if choose >= 0 and choose < 6:
                if choose == 1:
                    print("Yangi user kiritg: ")
                    obj.addNewUser()
                    continue
                elif choose == 2:
                    obj.deleteId()
                    continue
                elif choose == 3:
                    obj.gitOneId()
                    continue
                elif choose == 4:
                    obj.oneUserChange()
                    continue
                elif choose == 5:
                    break
            else:
                print("Iltimos 1 dan 6 gacha raqaqm tanlang: ")
                continue
    except ValueError as err:
        print("raqam kirit: ")
print("Siz dasturdan chiqdingiz! ")












