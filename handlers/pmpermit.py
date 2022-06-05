from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Merhaba, RapidMusic asistan hizmetidir.\n\n ❗️ Dikkat:\n - Ben Sizinle Sohbet Edemem.\n - Bilgi veya Komutlar için grubunuzun sohbetinde **/bilgi** yazarsanız müzik komutlarını ögrenebilirsiniz. \n - ASİSTAN HESABINA YAZACAĞINIZ HİÇ BİR KOMUT GEÇERLİ DEĞİLDİR. \n\n 🚨 **RapidMusicAsistant Grubunuza Katılmıyorsa >> DAVETLE KATILMA ÖZELLİĞİ VE SES YÖNETİMİ ÖZELLİKLERİ VEREREK YÖNETİCİ YAPIN. <<**\n\n ⚠️ DİKKAT: Burada bir mesaj gönderiyorsanız. Yöneticinin iletinizi göreceği anlamına gelir.\n - Özel bilgileri burada paylaşmayınız. (Müzik Botunu Lütfen Gizli Gruplara almayınız.) 📚 Bilgi için [Sahip 🧩](@EfsaneLions) 🇹🇷\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM İzin Etkin")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM İzin Devre Dışı")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**Hey Userbot Yazışması artık başarılı.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Yaklaşık olarak PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu şekilde PM")
        return
    message.continue_propagation()
