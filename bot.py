import asyncio
import random
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Bot tokeni
BOT_TOKEN = "7642585590:AAGU5oyggVjBobBIqMlGVWEej8yW0vB0rOk"

# Bot obyektlari
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Foydalanuvchilar ma'lumotlari
user_data = {}

# Test ma'lumotlari (namuna)
quizzes = {
  "1": [
        
        {
            "question": "Boshqarishning umumiy funksiyasi deganda nimani tushunasiz?",
            "options": [
                "Rejalashtirish va mehnatni tashkil qilish, hisobga olish va nazorat.",
                "Faoliyatni boshqarish va muvofiqlashtirish.",
                "Kadrlarni tanlash, joylashtirish va tarbiyalash.",
                "Barcha javoblar to‘gri."
            ],
            "correct": 3
        },
        {
            "question": "Kutubxona-axborot faoliyatini boshqarishda qanday asosiy usullar bor?",
            "options": [
                "Tashkiliy-huquqiy.",
                "Yo‘naltiruvchi- meʼyorlashtirish.",
                "Amaliy taʼsir usullari.",
                "Barcha javoblar to‘g‘ri"
            ],
            "correct": 3
        },
        {
            "question": "Boshqarishning chiziqli tizimi deganda nimani tushunasiz?",
            "options": [
                "Barcha farmoyishlar bo‘ysunuvchi tartibda yuqoridan pastga qarab berilishini.",
                "Direktorni bo‘lim mudiriga beradigan farmoyishini.",
                "Bo‘lim mudirini shu‘ba mudiriga beradigan farmoyishini.",
                "Guruh boshlig‘ini operativ xodimga beradigan farmoyishini."
            ],
            "correct": 0
        },
        {
            "question": "Kutubxona kengashi qanday organ?",
            "options": [
                "Jamoatchilik organi.",
                "Maxsus organ.",
                "Maxsus tashkil etiladigan organ.",
                "Boshqaruv organi."
            ],
            "correct": 0
        },
        {
            "question": "Rahbarlarga qo‘yiladigan kasbiy mahorat talablariga nimalar kiradi?",
            "options": [
                "Maxsus bilimlar.",
                "Ko‘nikmalar.",
                "Boshqaruv bilimlari va amaliy tajriba.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarlarning tashkiliy sifatlariga nimalar kiradi?",
            "options": [
                "Ishbilarmonlik va mustaqillik.",
                "Maqsadga intilish va tadbirkorlik",
                "Tashabbuskorlik va tezkorlik.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarlarning aqliy-iroda sifatlariga nimalar kiradi?",
            "options": [
                "Intiluvchanlik va tavakkalchilik.",
                "Talabchanlik, ishchi-xodimlarni bo‘ysundirish.",
                "Qiziqtirish qobiliyati, masʼuliyatni sezish, kamchiliklarni bilish va tan olish.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarlarning ruhiy xususiyatlarini taʼriflang?",
            "options": [
                "Muloqatga intilish.",
                "Xushmuomalalik.",
                "Taʼsirchanlik",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Axborot-kutubxona rahbarining asosiy boshqaruv vazifalarini taʼriflang?",
            "options": [
                "Rejalashtirish va tashkil etish.",
                "Muvofiqlashtirish va motivatsiya.",
                "Nazorat va rahbarlik qilish, qaror qabul qilish va kommunikatsiya",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "G.Minsberg fikriga ko‘ra menedjer tashkiliy maqsadlarga erishish jarayonida qanday rollarni bajaradi?",
            "options": [
                "Shaxslar orasida ish taqsimlovchi, axborotchi, tashkillashtiruvchilik roli.",
                "Insonlararo munosabatlarni bajaruvchilik roli.",
                "Rahbarning axborotchilik va turli qarorlar qabul qiluvchilik roli.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Avtokrat uslubga xos bo‘lgan belgilarni ko‘rsating?",
            "options": [
                "Rahbar jamoa bilan kelishmagan holda buyruqlar beradi. Qaror qabul qilishga qo‘l ostidagilarni yo‘latmaydi.",
                "Mehnat jamoasidan o‘zini yiroq tutadi va faqat o‘z fikri bilan hisoblashadi.",
                "Xodimlarni tashkilotga taalluqli bo‘lgan axborot va maʼlumotlar bilan tanishtirishni, bildirishni shart deb bilmaydi.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Demokratik uslubga xos bo‘lgan belgilarni ko‘rsating?",
            "options": [
                "Mehnat jamoasining fikrini bilib, boshqaruv funksiyalarini amalga oshirish.",
                "Ishlab chiqarishni boshqarishga xodimlarni keng jalb qilish.",
                "Xodimlarni yaxshi bilish, u rganishga intilish. O‘zini kamtar tutish.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Liberal uslubga taʼrif bering.",
            "options": [
                "Irodasizlik. Tashabbussizlik va qabul qilinayotgan qarorlarning masʼuliyatini o‘z bo‘yniga olmaslikka intilish.",
                "Kamtarlik",
                "Ishlab chiqarishni boshqarishga xodimlarni keng jalb qilish.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 0
        },
        {
            "question": "Motivatsiya nima?",
            "options": [
                "Shaxsiy, guruhli va jamoa maqsadlariga erishish uchun insonga taʼsir ko‘rsatish.",
                "Shaxsiy maqsadlarga erishishi uchun insonga taʼsir ko‘rsatish.",
                "Guruhni maqsadlariga erishishi uchun insonga taʼsir ko‘rsatish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 0
        },
        {
            "question": "Mak Gregorning X (iks) nazariyasini ko‘rsating?",
            "options": [
                "Odam ishlashni yoqtirmaydi.",
                "Odamni ishlashga majbur etish, nazorat qilish, zimmasiga yuklatilgan majburiyatlarini bajarmagan taqdirda jazo choralarini ko‘rilishi bilan popisa qilish lozim.",
                "O‘rtacha odam uning ustidan rahbarlik qilinishini xohlaydi, u masʼuliyatdan o‘zini olib qochadi, takliflar bilan chiqmaydi.",
                "Barcha javoblar to‘gri."
            ],
            "correct": 3
        },
        {
            "question": "Mak Gregorning U (igrik) nazariyasini ko‘rsating?",
            "options": [
                "Odam ishlashni, mustaqillikni va masʼuliyatni yoqtiradi.",
                "Nazorat yumshoq va sezilarsiz bo‘lishi shart",
                "Ko‘rsatma va buyruqlar berishdan qochish lozim.",
                "Barcha javoblar to‘gri."
            ],
            "correct": 3
        },
        {
            "question": "Boshqaruvning 'yaponcha stili' deganda nimani tushunasiz?",
            "options": [
                "Bu-milliy anʼanalarni va mamlakatning iqtisodiy xususiyatlarini hisobga olish.",
                "Bu insondagi ijodkorlik xislatlarini faollashtirish.",
                "Bu- milliy anʼanalarni xususiyatlarini hisobga olish.",
                "Barcha javoblar to‘gri."
            ],
            "correct": 0
        },
        {
            "question": "Motivatsiyaning tarkibiy tuzilmasi qanday omillarga bog‘lik bo‘ladi?",
            "options": [
                "Farovonlik darajasiga.",
                "Anʼanalarga.",
                "Odamlarni yoshiga",
                "Barcha javoblar to‘gri."
            ],
            "correct": 3
        },
        {
            "question": "Kutubxona kengashi nimalar bilan shug‘ullanadi?",
            "options": [
                "Kutubxona faoliyatining asosiy yo‘nalishlarini belgilaydi",
                "Kutubxona faoliyatini muhokama qiladi",
                "Kutubxona xodimlarining ishini baholaydi",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Kutubxona rahbariyatida qanday boshqaruv usullari mavjud?",
            "options": [
                "Iqtisodiy usullar",
                "Tashkiliy-uslubiy usullar",
                "Psixologik-uslubiy usullar",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning asosiy vazifalari qanday?",
            "options": [
                "Jamoa ishini tashkil qilish",
                "Kadrlarni boshqarish",
                "Moliyaviy resurslarni taqsimlash",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Demokratik rahbar kimdir?",
            "options": [
                "Jamoa fikriga ahamiyat beruvchi",
                "Qarorlarni birgalikda qabul qiluvchi",
                "Xodimlarning shaxsiy rivojiga yordam beruvchi",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Avtoritar rahbar kimdir?",
            "options": [
                "Barcha qarorlarni o‘zi qabul qiluvchi",
                "Xodimlarning mustaqil fikrlariga qarshilik ko‘rsatuvchi",
                "Faqat o‘z fikriga amal qiluvchi",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Liberal rahbar kimdir?",
            "options": [
                "Xodimlarga katta erkinlik beruvchi",
                "Mas'uliyatni kamaytiruvchi",
                "Ish jarayoniga aralashmaydigan",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning muvaffaqiyatli bo‘lishi uchun qanday fazilatlar kerak?",
            "options": [
                "Tashabbuskorlik",
                "Ijodkorlik",
                "O‘zgarishlarga moslasha olish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning asosiy xatolari qanday?",
            "options": [
                "Xodimlarning fikrlariga quloq solmaslik",
                "Vaqtni noto‘g‘ri boshqarish",
                "Aloqalarning yetarli emasligi",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning kommunikativ qobiliyatlari qanday bo‘lishi kerak?",
            "options": [
                "Yaxshi nutq sozlash",
                "Faol tinglash",
                "Aniq va tushunarli gapirish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning qaror qabul qilish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Tez va o‘rinli qaror qabul qilish",
                "Alternativlarni ko‘rib chiqish",
                "Xavfni baholay olish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning strategik fikrlash qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Uzoq muddatli rejalashtirish",
                "Istiqbolli fikrlash",
                "O‘zgarishlarni oldindan ko‘ra olish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning jamoani boshqarish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Jamoa ruhini ko‘tarish",
                "Xodimlarning salohiyatini ochish",
                "Jamoada hamjihatlikni taʼminlash",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning vaqtni boshqarish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Vaqtni samarali taqsimlash",
                "Muhim va muhim bo‘lmagan ishlarni ajrata olish",
                "Vaqtni tejash usullarini bilish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning konfliktlarni hal qilish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Konfliktlarni oldini olish",
                "Konfliktlarni hal qilish usullarini bilish",
                "Konfliktlarni ijobiy hal qilish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning o‘zini o‘zi boshqarish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "O‘z his-tuyg‘ularini boshqara olish",
                "Stressga chidamli bo‘lish",
                "O‘z kamchiliklarini tan olish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning innovatsion qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Yangi g‘oyalarga ochiq bo‘lish",
                "Tajribalardan o‘rganish",
                "Yechimlarni izlash",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Rahbarning o‘qish qobiliyati qanday bo‘lishi kerak?",
            "options": [
                "Doimiy o‘qish",
                "Yangi bilimlarni o‘zlashtirish",
                "Mutaxassislik sohasidagi yangiliklarni kuzatish",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
         {
            "question": "O‘zbekistonda qachon va qayerda oliy ma’lumotli kutubxonachilar tayyorlash boshlangan?",
            "options": [
                "1958 yilda Qo‘qon pedagogika institutining kutubxonachilik fakultetida",
                "1973 yilda Jizzax pedagogika institutining kutubxonachilik fakultetida",
                "1960 yilda Toshkent davlat pedagogika institutida",
                "1975 yilda Toshkent davlat madaniyat institutida"
            ],
            "correct": 0
        },
        {
            "question": "Kutubxonachilik ishini ilmiy boshqarish asosini nima tashkil etadi?",
            "options": [
                "Uzluksiz maqsadli ravishda kutubxonachilik obektlariga ta’sir ko‘rsatish",
                "Salbiy tendensiyalarga qarshi o‘z-o‘zini boshqarib borish, rivojlanish",
                "Kutubxonachilik ishi va boshqarishning dialektik o‘zaro faoliyati, ya’niy boshqaruv subekti",
                "Uzluksiz maqsadli ravishda kutubxonachilik jarayonlariga ta’sir ko‘rsatish"
            ],
            "correct": 2
        },
        {
            "question": "Axborot-kutubxona muassasalarining qaysi mutaxassisi kutubxonachi-amaliyotchi va yangi innovatsion g‘oyalar o‘rtasidagi vositachi xisoblanadi?",
            "options": [
                "Uslubch",
                "Bibliograf",
                "Kataloglashtiruvchi",
                "Operator"
            ],
            "correct": 0
        },
        {
            "question": "Maxsus kutubxonalarni asosiy guruhlarini ko‘rsating?",
            "options": [
                "Ijtimoiy-ilmiy, tabiiy-ilmiy va amaliy",
                "Tabiiy-ilmiy va amaliy",
                "Ijtimoiy-ilmiy, ilmiy va ommabop",
                "Ijtimoiy-siyosiy, tabiiy-ilmiy va texnik"
            ],
            "correct": 0
        },
        {
            "question": "“2011-2015 yillarda axborot-kommunikasiya texnologiyalari asosida axborot-kutubxona va axborot-resurs markaz xizmatlarini yanada sifatli rivojlantirish choralari to'g'risida”gi qarori qachon qabul qilindi?",
            "options": [
                "2011 yil 23 fevral",
                "2011 yil 10 yanvar",
                "2011 yil 13 aprel",
                "2011 yil 20 may"
            ],
            "correct": 0
        },
        {
            "question": "“Yig'ma elektron katalog markazi” qaysi kutubxonada tashkil etilgan?",
            "options": [
                "Respublika ilmiy pedagogika kutubxonasida",
                "Navoiy nomidagi Milliy kutubxonasida",
                "Universal kutubxonasida",
                "Akademiya kutubxonasida"
            ],
            "correct": 1
        },
        {
            "question": "ARMAT qanday tizim?",
            "options": [
                "Kataloglashtirish",
                "Lokal tarmoq",
                "Korporativ axborot-resurs markazlarining avtomatlashtirilgan tizimi.",
                "Butlash"
            ],
            "correct": 2
        },
        {
            "question": "“Oliy o'quv yurtlari uchun elektron darsliklar bazasini shakllantirish metodikasi va dasturiy majmua” qaysi institutda nechanchi yillarda bajarildi?",
            "options": [
                "2008-2009 yil A.Qodiriy nomidagi Toshkent Davlat madaniyat institutida",
                "2007-2009 yil A. Qodiriy nomidagi Toshkent Davlat madaniyat institutida",
                "2009-2010 yil A. Qodiriy nomidagi Toshkent Davlat madaniyat institutida",
                "2006-2008 yil A. Qodiriy nomidagi Toshkent Davlat madaniyat institutida"
            ],
            "correct": 0
        },
        {
            "question": "“Elektron kataloglashtirishning kooperativ tizimi” qaysi kutubxonada nechanchi yillarda bajarildi?",
            "options": [
                "2005-2006 yil A. Navoiy nomidagi O'zbekiston Milliy kutubxonasida",
                "2004-2005 yil A. Navoiy nomidagi O'zbekiston Milliy kutubxonasida",
                "2006-2009 yil A. Navoiy nomidagi O'zbekiston Milliy kutubxonasida",
                "2006-2008 yil A. Navoiy nomidagi O'zbekiston Milliy kutubxonasida"
            ],
            "correct": 3
        },
        {
            "question": "“Axborot-resurs markazlarini elektron ilmiy ta'limiy axborotlar bilan ta'minlash” qaysi kutubxonada nechanchi yillarda bajarildi?",
            "options": [
                "2008-2009 yillarda A. Navoiy nomidagi Milliy kutubxonasi",
                "2009-2011 yillarda A. Navoiy nomidagi Milliy kutubxonasi",
                "2010-2011 yillarda A. Navoiy nomidagi Milliy kutubxonasi",
                "2011-2012 yillarda A. Navoiy nomidagi Milliy kutubxonasi"
            ],
            "correct": 1
        }

  ],
"2": [
            {
            "question": "Elektron kutubxona to’g’risidagi namunaviynizom qachon qabul qilindi?",
            "options": [
                "2011 yil 5 iyul",
                "2011 yil 20 may",
                "2006 yil 20 iyun",
                "2011 yil 23 yanvar"
            ],
            "correct": 0
        },
        {
            "question": "Bibliografik ma'lumotlarni qaysi formatdan konvertasiya qilishi mumkin?",
            "options": [
                "Dublin Yadrosi 19 formatdan",
                "Dublin Yadrosi 20 formatdan",
                "Dublin Yadrosi 21 formatdan",
                "Dublin Yadrosi 23 formatdan"
            ],
            "correct": 0
        },
        {
            "question": "Elektron bibliografik resurslarga qanday tizim orqali masofadan kiritishni ta'minlaydi?",
            "options": [
                "Oddiy aloqa vositasi orqali.",
                "Ziyo Net orqali.",
                "Internet orqali masofadan kirishni.",
                "Lokal tarmoq orqali"
            ],
            "correct": 2
        },
        {
            "question": "“ZiyoNET” ta’lim tarmog‘i qachon tashkil etilgan?",
            "options": [
                "2005 yil 2 sentyabr",
                "2011 yil 25 may",
                "2006 yil 20 iyun",
                "2007 yil 18 avgust"
            ],
            "correct": 0
        },
        {
            "question": "Ixtiyoriy ko'rinishdagi an'anaviy va noan'anaviy nashrlarga ishlov berishga qanday nashrlar kiradi?",
            "options": [
                "Notalar, referatlar, qo'lyozmalar.",
                "Kitoblar, darsliklar, jurnallar, maqolalar, audio va videomateriallar",
                "Darsliklar, jurnallar, to'plamlar.",
                "Maqolalar, audio va videomateriallar"
            ],
            "correct": 1
        },
        {
            "question": "Tizim administratorining AIO' bajariladigan ishlar necha banddan iborat?",
            "options": [
                "6 ta",
                "8 ta",
                "7 ta",
                "5 ta"
            ],
            "correct": 0
        },
        {
            "question": "Kataloglashtiruvchining AIO' bajariladigan ishlar nimalardan iborat?",
            "options": [
                "Ma'lumotlarni to'ldirish, elektron katalog va ma'lumotlar bazasini shakllantirish.",
                "Elektron kutubxona foydalanuvchilarini ro'yxatga olish, ma'lumotlar bazalarida qidirishni bajarish.",
                "Qidirib topilgan hujjatlar to'g'risida bibliografik ma'lumotlar olish.",
                "Barcha javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "Foydalanuvchining (Kitobxonning) AIO' qanday ishlar bajariladi?",
            "options": [
                "Tizim interfeyisini o'zlariga mos tilga o'tkazishlari.",
                "Bibliografik tavsifning barcha elementlari bo'yicha oddiy va kengaytirilgan qidirishni bajarishlari.",
                "Topilgan hujjatlarning to'liq matnini ko'rib chiqishlari.",
                "Barcha javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "Bosh sahifada foydalanuvchilar uchun qanday imkoniyatlar yaratilgan?",
            "options": [
                "Katalog menyusidan foydalanib kerakli ma'lumotlar bazasini tanlash",
                "Qidirish, Kengaytirilgan Qidirish tugmasini bosish orqali elektron kutubxona fondida qidiruv bajarish",
                "Topilgan hujjatlarning bibliografik tavsifini, annotasiyasini, mundarijasiniva elektron kutubxonada erkin ko'rishga mo'ljallangan to'liq matnlarni ko'rib chiqish mumkin.",
                "Barcha javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "ARMATning maxsus moduli qaysi kutubxonalarga qanday tarmoq orqali ma'lumotlarni taqdim eta oladi?",
            "options": [
                "AKM, ARM va kutubxonalarning elektron bibliografik resurslarini INTERNET tarmog'ida taqdim qila oladi.",
                "Oddiy kompyuterlar orqali",
                "Lokal tarmoqlar orqali",
                "Qog'oz nusxadagi ma'lumotlar orqali"
            ],
            "correct": 0
        },
        {
            "question": "Foydalanuvchi o'ziga berilgan qanday ma'lumotlar orqali EKning “Kitobxoni” maqomiga ega bo'ladi?",
            "options": [
                "Regstrasiya",
                "Parol va Login",
                "Qidiruv",
                "Katalog"
            ],
            "correct": 1
        },
        {
            "question": "Kataloglashtiruvchining AIO' yana qanday ishlar bajariladi?",
            "options": [
                "Bibliografik tavsifning elementlari bo'yicha qidiruv bajarish, yangi hujjatlar bibliografik tavsif elementlari asosida katalog bazasini shakllantirish.",
                "Ma'lumotlar bazasidagi hujjatlarni tahrirlash.",
                "Ma'lumotlar bazasidagi hujjatlarni tahrirlash, ma'lumotlar bazalarini (dinami va statik) shakllantirish.",
                "Hamma javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "Hujjat sarlovhasi nechanchi maydonga kiritiladi?",
            "options": [
                "239 maydonga",
                "241 maydonga",
                "245 maydonga",
                "242 maydonga"
            ],
            "correct": 2
        },
        {
            "question": "Elektron kutubxona to’g’risidagi namunaviy nizom qachon qabul qilindi?",
            "options": [
                "2011 yil 5 iyul",
                "2011 yil 20 may",
                "2006 yil 20 iyun",
                "2011 yil 23 yanvar"
            ],
            "correct": 0
        },
        {
            "question": "Hujjat tegishli bo'lgan mavzu (predmet)ni aniqlash uchun nechanchi maydonda ish bajariladi?",
            "options": [
                "010 maydoni orqali",
                "019 maydoni orqali",
                "013 maydoni orqali",
                "020 maydoni orqali"
            ],
            "correct": 1
        },
        {
            "question": "Hujjat annotasiyasi (referati) nechanchi maydon orqali kiritiladi?",
            "options": [
                "430 A",
                "510 A",
                "520 A",
                "515 B"
            ],
            "correct": 2
        },
        {
            "question": "Ma'lumotlar bazasiga kiritilgan hujjatning bibliografik tavsifini kartochka ko'rinishida bosib chiqarish uchun qaysi tugma bosiladi?",
            "options": [
                "Chop qilish tugmasi.",
                "Qidirish tugmasi",
                "Parol",
                "Regstrasiya"
            ],
            "correct": 0
        },
    {
        "question": "Moddiy rag‘batlantirishning qanday turlarini bilasiz?",
        "options": [
            "Ish haqiga qo‘shimcha qilish",
            "Maoshni oshirish",
            "Lavozimni o‘zgartirib ish haqini oshirish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Rag‘batlantirishning yana qanday usullarini bilasiz?",
        "options": [
            "Tan olish va bo‘sh vaqt",
            "Qiziqarli ish va erkinlik",
            "Huzur-halovat va istiqbol",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Ideal xodimning umumiy xislatlarini ko‘rsating?",
        "options": [
            "Ishning sifatli bajarilishini ta'minlaydi, javobgarlikni his qiladi, ishga qiziqadi, o‘z ishiga sadoqatli",
            "O‘z boshlig‘iga xayrixoh va aqli bilan tavakkal qiladi. Tashabbus ko‘rsatadi, yordam berishga har doim tayyor bo‘ladi",
            "Ishni qanday tashkil qilishni biladi, qat'iy harakatlar qiladi",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Ijtimoiy munosabatlarning birinchi bosqichi nima?",
        "options": [
            "Odamlarni boshqarish",
            "Odamlarni munosabatlarini boshqarish",
            "Odamlarni ijtimoiy-iqtisodiy munosabatlarini boshqarish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Ijtimoiy munosabatlarning ikkinchi bosqichi nima?",
        "options": [
            "Ishchilar va xizmatchilar orasidagi munosabatlar",
            "Aqliy mehnat kishilari orasidagi munosabat",
            "Ijodkorlar orasidagi munosabatlar",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Ijtimoiy munosabatlarning uchinchi bosqichi nima?",
        "options": [
            "Mehnat jamoalari orasidagi munosabatlar",
            "Jamoa a'zolari orasidagi munosabatlar",
            "Odamlar orasidagi munosabatlar",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Insonlarni ijtimoiy boshqarish deganda nimani tushunasiz?",
        "options": [
            "Har bir insonning ijtimoiy rolini aniqlash, ya'ni uning ishlab chiqarishdagi yoki xizmat ko‘rsatish sohasidagi o‘rni, vazifalari, huquq va majburiyatini bildirish",
            "Har bir insonning o‘z funksiyasini, majburiyat va huquqini, ijtimoiy rolini anglatish",
            "Har bir insondan o‘z ijtimoiy rolini bajarishni talab qilish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Kasbiy jamoaning ijtimoiy-iqtisodiy rivojlanishining birinchi guruh tadbirlarini qayd eting.",
        "options": [
            "Fan-texnikaning eng yangi yutuqlarini joriy qilish",
            "Kadrlarning kasbiy bilimlariga va mahoratiga talabni oshirish",
            "Kadrlarning madaniy-texnik darajasiga, qayta tayyorlash va o‘qitishga talabni oshirish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Kasbiy jamoaning ijtimoiy-iqtisodiy rivojlanishining ikkinchi guruh tadbirlarini qayd eting?",
        "options": [
            "Ishchi va xizmatchilarni turmush darajasini oshirish va madaniy-maishiy turmush sharoitini yaxshilash",
            "Ishchi va xizmatchilarni maoshini oshirish",
            "Ishchi va xizmatchilarni turmush darajasini oshirish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 0
    },
    {
        "question": "Inson xulqini, harakatlarini tashkil qiladigan omillarni bilasizmi?",
        "options": [
            "Ijtimoiy va tabiiy muhit",
            "Ehtiyojlar, manfaatlar, xohish, intilish, maqsad shaklida ehtiyojlarni anglash",
            "Harakatga turtki berish, qiziqtirish (motivatsiya). O‘z-o‘ziga ishonch, yo‘nalish, vazifa berish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Formal guruhlar nima?",
        "options": [
            "Rahbariyat tomonidan maxsus qoidalar, qarorlar asosida, ularning faoliyatlari bayon qilingan holda tuzilgan guruh",
            "Rahbariyat tomonidan tuzilgan guruh",
            "Maxsus tuzilgan guruh",
            "Maxsus qoidalar buyicha tuzilgan guruh"
        ],
        "correct": 0
    },
    {
        "question": "Formal guruhlarning asosiy belgilarini ko‘rsating?",
        "options": [
            "Yagona ichki tizimda ijtimoiy munosabatlarning elementi sifatida, qat'iy belgilangan vazifalarni bajarishi",
            "Guruh tarkibidagilarning istak va xohishidan qat'iy nazar obyektiv ravishda mavjud bo‘lishi. Guruhning ijtimoiy intizomini belgilashi",
            "Guruh qiziqishlari va qadriyatlar tizimini o‘zida aks ettiruvchi ijtimoiy psixologik o‘ziga xoslikka ega bo‘lishi",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Noformal guruhlar qanday paydo bo‘ladi?",
        "options": [
            "Jamoa a'zolari orasida bir-biriga mos kelishlar natijasida",
            "Jamoa a'zolarining umumiy qiziqishlari natijasida",
            "Jamoa a'zolarining bir xil ish bilan shug‘ullanish natijasida",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Noformal guruhlarning o‘ziga xos xususiyatlarini ko‘rsating?",
        "options": [
            "Ijtimoiy nazoratni bo‘lishi va o‘zgarishlarga qarshilik ko‘rsatish",
            "Guruh a'zosini muomalada, o‘zini tutishda, kiyinishda yozilmagan qoidalarga amal qilishi",
            "O‘zgarishlarga qarshilik ko‘rsatish",
            "Guruhda yetakchini bo‘lishi"
        ],
        "correct": 0
    },
    {
        "question": "Nizo nima?",
        "options": [
            "Bu - rahbar, ishchi va boshqa xodimlar orasida muayyan masalalarni hal qilishda tomonlarning bir-biri bilan bir yechimga kela olmasligidir",
            "Bu - rahbar va xodim orasidagi kelishmovchiliklar",
            "Bu - xodimlar o‘rtasidagi o‘zaro kelishmovchiliklar",
            "Bu - guruhlar o‘rtasidagi kelishmovchiliklar"
        ],
        "correct": 0
    },
    {
        "question": "Nizo (konflikt)larning nechta asosiy turi mavjud?",
        "options": [
            "Ikkita: inson shaxsiyati va guruh orasidagi nizolar",
            "Uchta: shaxsning o‘z ishiga xos ichki nizolar, inson shaxsiyati va guruh orasidagi nizolar va shaxsiy nizolar",
            "To‘rtta: shaxsning o‘z ishiga xos ichki nizolar; inson shaxsiyati va guruh orasidagi nizolar; insonlar orasidagi nizolar; guruhlar orasidagi nizolar",
            "Beshta: shaxsning o‘z ishiga xos ichki nizolar; inson shaxsiyati va guruh orasidagi nizolar; insonlar orasidagi nizolar; guruhlar orasidagi nizolar; shaxsiy nizolar"
        ],
        "correct": 2
    },
    {
        "question": "Axborot-kutubxona fondini tashkil qilish necha etapdan iborat?",
        "options": [
            "4 etapdan iborat",
            "3 etapdan iborat",
            "5 etapdan iborat",
            "2 etapdan iborat"
        ],
        "correct": 0
    },
    {
        "question": "Kataloglar necha xilga bo‘linadi?",
        "options": [
            "Alfavit katalog, sistemali katalog",
            "Predmet katalog, elektron katalog",
            "Mavzuli katalog, xronologik katalog",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Alfavit katalog deb nimaga aytiladi?",
        "options": [
            "Barcha resurslar ularning fan sohalari bo‘yicha mazmuni va belgilariga qarab guruhlarga ajratiladi",
            "Tuzilayotganda barcha resurslarning mazmuniga asoslanadi, bibliografik tavsifi bilim sohalari bo‘yicha emas, hujjatda bayon etilayotgan predmet nomlarining alfavit tartibiga binoan joylashtiriladi",
            "Barcha mavjud resurslarning tavsifi mualliflarning familiyalari yoki sarlavhalarning alfaviti bo‘yicha joylashtiriladi",
            "To‘g‘ri javob yo‘q"
        ],
        "correct": 2
    },
    {
        "question": "Bibliografik tavsif nima?",
        "options": [
            "Bosma asar yoki mavjud resurs haqidagi ma'lumotlar yig‘indisi",
            "Kitobxonga hujjatning mazmunini to‘liq ochib beradi",
            "Foydalanuvchi uchun zarur bo‘lgan ma'lumotlarni to‘liq ochib beradi",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Hujjat so‘zining ma'nosi va u qaysi tildan olingan?",
        "options": [
            "Yunon tilidan olingan bo‘lib, axborot berish",
            "Lotin tilidan olingan bo‘lib, xabar berish",
            "Grek tilidan olingan bo‘lib, o‘rgatish",
            "Arab tilidan olingan bo‘lib, o‘qish"
        ],
        "correct": 1
    },
    {
        "question": "Umuman ijtimoiy fanlar klassifikatsiya jadvalining qaysi bo‘limida joylashgan?",
        "options": [
            "20",
            "60",
            "79",
            "87"
        ],
        "correct": 1
    },
    {
        "question": "Sportga oid adabiyotlar klassifikatsiya jadvalining qaysi bo‘limida joylashgan?",
        "options": [
            "75",
            "32",
            "85",
            "88"
        ],
        "correct": 0
    },
    {
        "question": "Klassifikatsiya jadvalining namunaviy bo‘linishlar tizimi nechta guruhga taqsimlanadi?",
        "options": [
            "To‘rtta: umumiy namunaviy bo‘linishlar, hududiy namunaviy bo‘linishlar, maxsus namunaviy bo‘linishlar, ijtimoiy tizimlarning namunaviy bo‘linishlari",
            "Uchta: hududiy bo‘linishlar, maxsus bo‘linishlar, ijtimoiy bo‘linishlar",
            "Ikkita: mukammal jadvallar, umumiy jadvallar",
            "To‘g‘ri javob yo‘q"
        ],
        "correct": 0
    },
    {
        "question": "AKM va ARM fondlarini saqlash va asrashga qanday omillar ta'sir ko‘rsatadi?",
        "options": [
            "Ijtimoiy omillar",
            "Fizikaviy-ximiyaviy omillar",
            "Biologik omillar",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "AKM va ARM fondidagi adabiyotlarni formal belgilari bo‘yicha joylashtirish jarayoniga nimalar kiradi?",
        "options": [
            "Sistemali, mavzuli",
            "Predmetli, alifbo",
            "Alifbo, sanasi, geografiyasi",
            "Formati, sistemali"
        ],
        "correct": 2
    },
    {
        "question": "„Ilmlarni kelib chiqishi va tasnifi“ risolasi Sharqda klassifikatsiyaning paydo bo‘lishiga hissa qo‘shgan qaysi allomaning qalamiga mansub?",
        "options": [
            "Abu Ali Ibn Sino",
            "Abu Nasr Farobiy",
            "Abu Abdulloh al-Xorazmiy",
            "Az-Zamaxshariy"
        ],
        "correct": 1
    },
    {
        "question": "Indekslar mazmuni jihatidan necha turga bo‘linadi?",
        "options": [
            "Katalog indeksi",
            "Shifr indeksi",
            "To‘liq indeks",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "66.3(5O‘zb)+63.3(5O‘zb)+87.60(5O‘zb) ushbu tavsif qaysi indeksga tegishli?",
        "options": [
            "Katalog indeks",
            "Shifr indeks",
            "To‘liq indeks",
            "To‘g‘ri javob yo‘q"
        ],
        "correct": 2
    },
    {
        "question": "Axborot-kutubxona fondi necha xil usulda joylashtiriladi?",
        "options": [
            "Ikki xil usulda",
            "Uch xil usulda",
            "To‘rt xil usulda",
            "Besh xil usulda"
        ],
        "correct": 0
    },
    {
        "question": "Axborot-kutubxona muassasalarini to‘ldirishning qanday usullari mavjud?",
        "options": [
            "Joriy to‘ldirish",
            "Retrospektiv to‘ldirish",
            "Fondan chiqarish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Axborot-kutubxona fondi nima?",
        "options": [
            "Tizimlashtirilgan axborot-kutubxona resurslarining majmui",
            "Texnik vositalar yordamida qayta aks ettirilgan tasvir",
            "Axborot-kutubxona resurslarining hisob hujjatlarini aks ettirish",
            "Axborot-kutubxona resurslaridagi adabiyotlarni ro‘yxatdan o‘tkazish"
        ],
        "correct": 0
    },
    {
        "question": "Axborot-kutubxona resurslari fondini hisobga olishning qanday turlari mavjud?",
        "options": [
            "Yakka hisobga olish",
            "Jamlama hisobga olish",
            "Umumiy hisobga olish",
            "To‘g‘ri javob A va B"
        ],
        "correct": 3
    },
    {
        "question": "Axborot-kutubxona fondlarini tashkil qilish qanday jarayonlardan iborat?",
        "options": [
            "Modellashtirish, to‘ldirish",
            "Hisobga olish, kitoblarga ishlov berish",
            "Joylashtirish, saqlash, yetkazib berish, fondni boshqarish",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Axborot-kutubxona fondini qanday holatlarda tekshiriladi?",
        "options": [
            "Moddiy javobgar shaxs almashtirilganda",
            "Axborot-kutubxona resurslarini o‘g‘irlash yoki buzish holatlari aniqlanganda",
            "Tabiiy ofat, yong‘in va boshqa holatlarda",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "Klassifikatsiya so‘zining ma'nosi?",
        "options": [
            "Predmetlarni yig‘ish",
            "Predmetlarni sinflarga ajratish",
            "Hujjatlarni alifbo tartibida joylashtirmoq",
            "Hujjatlarni to‘plamoq"
        ],
        "correct": 1
    },
    {
        "question": "Kutubxonalar fondini to‘ldirish usullari va manbalari?",
        "options": [
            "Sotib olish, obuna bo‘lish",
            "Majburiy nusxa olish, kitob ayirboshlash",
            "Nusxa ko‘chirish, sovg‘a tariqasida in‘om etiladigan kitoblar",
            "Barcha javoblar to‘g‘ri"
        ],
        "correct": 3
    },
    {
        "question": "„Fond“ so‘zi kutubxonashunoslikda nechanchi yilda paydo bo‘lgan?",
        "options": [
            "1930-yil",
            "1940-yil",
            "1900-yil",
            "1920-yil"
        ],
        "correct": 3
    },
    {
        "question": "Fond so‘zi qaysi tildan kirib kelgan va qanday ma'noni anglatadi?",
        "options": [
            "Lotin tilidan kirib kelgan bo‘lib, hujjat degan ma'noni anglatadi",
            "Nemis tilidan kirib kelgan bo‘lib, nimaningdir asosi degan ma'noni bildiradi",
            "Fors tilidan kirib kelgan bo‘lib, tag, yer, asos degan ma'noni anglatadi",
            "Arab tilidan kirib kelgan bo‘lib, kutubxona degan ma'noni bildiradi"
        ],
        "correct": 1
    },
    {
        "question": "Axborot so‘zi qaysi tildan olingan va qanday ma'noni anglatadi?",
        "options": [
            "Lotin tilidan olingan bo‘lib, tushuntirish ma'nosini anglatadi",
            "Fransuz tilidan olingan bo‘lib, yangilik degan ma'noni anglatadi",
            "Nemis tilidan olingan bo‘lib, ma'lumot degan ma'noni bildiradi",
            "To‘g‘ri javob yo‘q"
        ],
        "correct": 0
    },
    {
        "question": "Belgilangan ma'lum bir qoidaga ko‘ra nashr haqidagi umumiy va xususiy ma'lumotlarni aks ettirish maqsadida, ma'lum bir ketma-ketlikda bir qancha bibliografik elementlardan tashkil topgan tavsif sohalari yig‘indisi nima deb yuritiladi?",
        "options": [
            "Monografik tavsif",
            "Analitik tavsif",
            "Bibliografik tavsif",
            "Indekslash"
        ],
        "correct": 2
    },
    {
        "question": "Yog‘och texnologiyasi, yengil sanoat ishlab chiqarishi. Poligrafiya ishlab chiqarilishi. Fotokinotexnika KBK jadvalining qaysi bo‘limida joylashgan?",
        "options": [
            "37",
            "36",
            "35",
            "34"
        ],
        "correct": 0
    },
    {
        "question": "Ichki kasalliklar KBK jadvalining qaysi bo‘limida joylashgan?",
        "options": [
            "54.1",
            "54.5",
            "54.6",
            "54.8"
        ],
        "correct": 0
    },
    {
        "question": "Sotsiologiyaga oid adabiyotlar KBK jadvalining qaysi bo‘limida joylashgan?",
        "options": [
            "60.5",
            "60.6",
            "60.7",
            "65"
        ],
        "correct": 0
    }
],

    "3": [
        {
            "question": "Ommaviy axborot va targ`ibot vositalari, kitob ishi. Kitobshunoslik KBK jadvalining qaysi bo`limida joylashgan?",
            "options": ["73", "74", "75", "76"],
            "correct": 3
        },
        {
            "question": "Badiiy adabiyotlar, badiiy asarlar KBK jadvalining qaysi bo`limida joylashgan?",
            "options": ["81", "82", "83", "84"],
            "correct": 3
        },
        {
            "question": "Falsafaga oid adabiyotlar KBK jadvalining qaysi bo`limida joylashgan?",
            "options": ["87", "86", "70", "72"],
            "correct": 0
        },
        {
            "question": "Psixologiya tarixi KBK jadvalining qaysi bo`limida joylashgan?",
            "options": ["88.1", "88.2", "88.3", "88.4"],
            "correct": 0
        },
        {
            "question": "Kutubxonaning Ma’lumot-bibliografik apparati (MBA) ni tarifini toping:",
            "options": [
                "O‘zaro bog‘liq elementlari bir-birini to‘ldiruvchi, yagona maqsadga, ya’ni kitobxonlarning axborot talablarini qisqa muddatda bajarishga qaratilgan axborot qidiruv tizimi.",
                "Kutubxona fondining mazmunini yorituvchi katalog va kartotekalar hamda bibliografik ko‘rsatkichlarning yig‘indisi.",
                "Turli guruh kitobxonlarining talab va ehtiyojlarini qondirishga qaratilgan kataloglar va kartotekalar yig‘indisi.",
                "Kitobxonlarning so‘roqlarini bajaruvchi turli enseklopediyalar, spravochniklar, bibliografik qo‘llanmalar majmuasidir."
            ],
            "correct": 0
        },
        {
            "question": "Axborot-kutubxona markazi (AKM) da MBA ni tashkil etishda asosan qaysi bo‘lim javobgar hisoblanadi?",
            "options": [
                "Adabiyotlarga ishlov berish bo‘limi",
                "Bibliografiya bo‘limi",
                "Fondni saqlash bo‘limi",
                "Xizmat ko‘rsatish bo‘limlari, fondni jamlash bo‘limi"
            ],
            "correct": 1
        },
        {
            "question": "Axborot ehtiyojlarini o‘rganishning usullari qanday nomlanadi?",
            "options": [
                "Iste’molchilarni guruhlarga ajratish",
                "O‘qilgan adabiyotlari haqida suhbat",
                "So‘roqlash, intervyu",
                "Kuzatish, hujjatli ma’lumotlarni o‘rganish, so‘roqlash."
            ],
            "correct": 3
        },
        {
            "question": "Bibliografik faoliyat nima?",
            "options": [
                "Kitobxonlarga bibliografik xizmat ko‘rsatish",
                "Kutubxonalar, ilmiy texnika organlari, nashriyotlar va hujjatlar aloqa yo‘llari tizimidagi boshqa jamoat institutlari tomonidan ilmiy-yordamchi, ishlab chiqarish, tarbiyaviy, targ‘ibotchilik va boshqa maqsadlarda bibliografik axborotga bo‘lgan ehtiyojni har tomonlama qondirishga xizmat qiluvchi hujjatli axborot faoliyati sohasidir.",
                "Bibliografik xizmat ko‘rsatish, SBA ni yuritish, bibliografik qo‘llanmalar tuzish",
                "Iste’molchilar so‘roqlarini bajarish."
            ],
            "correct": 1
        },
        {
            "question": "Ma`lumot va bibliografik nashrlar fondining tarkibi qaysilar?",
            "options": [
                "Bosh manba materiallari, ma’lumot adabiyotlari, bibliografik qo‘llanmalar",
                "Ensiklopediyalar, spravochniklar, lug‘atlar, yo‘l ko‘rsatkichlari",
                "Turli bibliografik qo‘llanmalar",
                "Prezident asarlari, qonunlar"
            ],
            "correct": 0
        },
        {
            "question": "Bibliografiyalash jarayoning asosiy mazmuni nimadan iborat?",
            "options": [
                "Bibliografik axborotni yaratish",
                "Bibliografik yozuvlarni gruppalash",
                "Yordamchi ko‘rsatkichlarini tuzish",
                "Bibliografik ehtiyojlarni tuzish"
            ],
            "correct": 0
        },
        {
            "question": "Adabiyot tanlashning asosiy jarayonlari qaysilar?",
            "options": [
                "Adabiyotlarni yuqori to‘liqlikda aniqlash",
                "Adabiyotlarni ma’lum bir xronologik davr uchun aniqlash",
                "Eskirgan adabiyotlarni chiqarib yuborish",
                "Adabiyotlarni mazmunan, belgilangan davr uchun zarur xillari va turlarini ajratish."
            ],
            "correct": 3
        },
        {
            "question": "Qanday bibliografik qo‘llanmalarda bibliografik yozuvlar sistemali tartibda joylashtiriladi?",
            "options": [
                "Tavsiya",
                "Davlat",
                "Repertuar",
                "Tarmoq"
            ],
            "correct": 1
        },
        {
            "question": "«Turkiston to‘plamlari» bibliografik ko‘rsatkichining muallifini aniqlang?",
            "options": [
                "Dmitrovskiy N.V",
                "Mejov V.I",
                "Smirnov D.V",
                "Dorn B.A"
            ],
            "correct": 1
        },
        {
            "question": "Respublikamizda nashr qilinadigan hamma matbuot asarlarini nashr qilish, joyi, tili, mazmunidan qattiy nazar qaysi bibliografiya hisobga oladi?",
            "options": [
                "Shaxs bibliografiyasi",
                "O‘lkashunoslik bibliografiyasi",
                "Tarmoq bibliografiya si",
                "Davlat bibliografiyasi"
            ],
            "correct": 3
        },
        {
            "question": "“Fixrist”, ya`ni “Bibliografiya” asarini O`rta asr Sharq allomalaridan qaysi biri yozgan?",
            "options": [
                "Abu Ali Ibn Sino",
                "Ar-Roziy",
                "Abu Rayxon Beruniy",
                "Abu Nasr Farobiy"
            ],
            "correct": 2
        },
        {
            "question": "Bir sahifadan to`rt sahifagacha bo`lgan hajmdagi nashrlar qanday nomlanadi?",
            "options": [
                "Kitob",
                "Risola",
                "Periodika",
                "Varaqa"
            ],
            "correct": 3
        },
        {
            "question": "O‘zbekiston Respublikasi Prezidentining qabul qilingan \"Kitob mahsulotlarini nashr ettirish va tarqatish tizimini rivojlantirish, kitob mutolaasi va kitobxonlik madaniyatini oshirish hamda targ‘ib qilish bo‘yicha kompleks chora-tadbirlar dasturi to‘g‘risida\"gi Qarori qachon qabul qilingan?",
            "options": [
                "2017 yil, 13 sentabrda.",
                "2017 yil, 10 sentabrda",
                "2018 yil, 13 sentabrda",
                "2019 yil, 12 sentabrda"
            ],
            "correct": 0
        },
        {
            "question": "Annotatsiya vazifasiga ko‘ra necha turga bo‘linadi?",
            "options": [
                "spravka, tavsiya annotatsiyasi",
                "tavsiya, analitik",
                "umumiy, guruhli",
                "umumiy, analitik annotatsiyalar."
            ],
            "correct": 0
        },
        {
            "question": "Mavzuni o‘rganishdan asosiy maqsad nima?",
            "options": [
                "Uning dolzarbligi, ijtimoiy ahamiyatini aniqlash",
                "Hujjatlarni bib-k xarakteristikalash uslubini aniqlash",
                "Qo`llanmaning chegarasini, masalalar doirasini, mavzuning bibliografik yoritilishini aniqlash",
                "Yuqoridagilarning hammasi."
            ],
            "correct": 0
        },
        {
            "question": "Ommaviy bibliografik axborot xizmatining xususiyati nimadan iborat?",
            "options": [
                "Aniq kitobxonlar guruxini BA bilan ta`minlash",
                "Mutaxassislarga ularning ixtisosligi bo`yicha axborot berish",
                "Mutaxassislarga eng yangi va yaxshi adabiyotlar haqida axborot berish",
                "Aniq kitobxonlar guruhini hisobga olmay, keng kitobxonlar ommasiga yangi nashrlar to`g`risida axborot berish."
            ],
            "correct": 3
        },    
        {
            "question": "Bibliografik faoliyatning sub`ekti bu......",
            "options": [
                "BA ni tashkil qilish, iste`molchiga yetkazish va foydalanishni ta`minlovchi bibliograf.",
                "BA ni yaratish jarayoni",
                "BA ni yaratish omili bo‘lgan hujjat",
                "Bibliograf ish natijasida kutayotgan maqsad va natija"
            ],
            "correct": 0
        },
        {
            "question": "Bibliografik qo‘llanmaga yig‘ilgan hujjatlar qaysi bosqichda gurppalanadi?",
            "options": [
                "Tayyorlov",
                "Sintetik",
                "Yakunlovchi",
                "Sintetik va yakunlovchi"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografik faoliyatning bevosita (to‘g‘ridan - to‘g‘ri) obyekti qaysilar?",
            "options": [
                "Hujjat (kitob, vaqtli nashrlar, audiovizual materiallar).",
                "«Hujjat – iste’molchi» tizimi",
                "BA ni iste’molchiga yetkazish ishi",
                "Iste’molchining talabi"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografik faoliyatning natijasi bu.....",
            "options": [
                "Bibliografik xizmat ko‘rsatish",
                "Bibliografiyalash",
                "Bibliografik mahsulot (bibliografik qo‘llanma)",
                "Bibliografik faoliyatning subyekti"
            ],
            "correct": 2
        },
        {
            "question": "Bibliografik axborotning qaysi vazifasini amalga oshishida alohida kitobxonlar guruhining talablari va axborot ta’sirchanligi maqsadiga mos holda hujjatlar tavsiya etiladi?",
            "options": [
                "Qidirish",
                "Xabar berish",
                "Spravka – ma`lumot",
                "Baholash"
            ],
            "correct": 3
        },
        {
            "question": "Davomli nashrlarda bosilgan bibliografik materiallar bibliografik qo‘llanmaning qaysi shakliga kiradi?",
            "options": [
                "Mustaqil bo‘lmagan shakli",
                "Vaqtli nashr",
                "Kartochkali shakli",
                "Yordamchi ko‘rsatkich"
            ],
            "correct": 0
        },
        {
            "question": "Bibliografik faoliyat qachon va qayerda vujudga kelgan?",
            "options": [
                "Eramizdan avvalgi V asrda Qadimgi Gretsiyada",
                "Eramizdan avvalgi 3 mingginchi yillarda Qadimgi Nippurda",
                "Eramizning II asrida Nippurda",
                "Eramizdan avvalgi YI asrda Ussuriyada"
            ],
            "correct": 0
        },
        {
            "question": "Hujjatda qayd etilgan bibliografik xabar quyidagilarning qay birini anglatadi?",
            "options": [
                "Bibliografik yozuv",
                "Bibliografik tasvir",
                "Klassifikatsiya indeksi",
                "Kitobning shifri"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografik xizmat ko‘rsatish nima?",
            "options": [
                "Bibliografik faoliyatning jarayoni",
                "Faoliyatning vositasi",
                "Bibliografik faoliyat obyekti",
                "Faoliyatning subyekti"
            ],
            "correct": 0
        },
        {
            "question": "O‘zbekiston Davlat bibliografiyasi bilan qaysi tashkilot shug‘ullanadi?",
            "options": [
                "A.Navoiy nomidagi O‘zbekiston milliy kutubxonasi",
                "O‘zbekiston Respublikasi FA asosiy kutubxonasi",
                "O‘zbekiston Davlat matbuot qo‘mitasi",
                "O‘zbekiston Respublikasi Milliy kitob palatasi"
            ],
            "correct": 3
        },
        {
            "question": "Ma’lum o‘tgan yirik xronologik davr ichida chiqqan hujjatlar to‘g‘risida ma’lumotni qaysi bibliografik manbadan olish mumkin?",
            "options": [
                "Soha bibliografiyasi",
                "Davlat bibliografiyasi",
                "Retrospektiv bibliografiya",
                "Bibliografiyaning bibliografiyasi"
            ],
            "correct": 2
        },
        {
            "question": "Bibliografiyani mustaqil bilim olishga yordam beruvchi turini ko‘rsating?",
            "options": [
                "Universal bibliografiya",
                "Tarmoq bibliografiyasi",
                "Repertuar bibliografiya",
                "Tavsiya bibliografiyasi"
            ],
            "correct": 3
        },
        {
            "question": "O‘zbekistonda kelgusi yilda chiqadigan kitoblar haqidagi axborotni bibliografiyaning qaysi turi beradi?",
            "options": [
                "Tavsiya bibliografiyasi",
                "Perspektiv bibliografiya",
                "Shaxs bibliografiyasi",
                "Ilmiy yordamchi bibliografiya"
            ],
            "correct": 1
        },
        {
            "question": "“Jurnal maqolalari solnomasi”da qanday maqolalar tasvirlanmaydi?",
            "options": [
                "Ilmiy",
                "Ishlab chiqarish tajribasi haqidagi",
                "Ommabop",
                "Tanqidiy, satirik maqolalar, reklamalar"
            ],
            "correct": 3
        },
        {
            "question": "Biror geografik joy haqida yozilgan kitobni qanday yordamchi ko‘rsatkich yordamida topish mumkin?",
            "options": [
                "Ismlar",
                "Sarlavhalar",
                "Seriyalar",
                "Geografik"
            ],
            "correct": 3
        },
        {
            "question": "Quyidagi bibliografik qo‘llanmalarning qaysi biri sodda tuzilishga ega?",
            "options": [
                "Ko‘rsatkich",
                "Bibliografik ro‘yxat",
                "Yo‘l ko‘rsatkichi",
                "Bibliografik obzor"
            ],
            "correct": 1
        },
        {
            "question": "Quyidagi ko‘rsatkichlarning qaysi biri ma’lum bir shaxs yoki shaxslarning asarlarini aks ettiradi?",
            "options": [
                "O‘lkashunoslik",
                "Biobibliografik",
                "Tarmoq",
                "Mavzuli"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografiyalash ishiga quyidagilarning qaysi biri kiradi?",
            "options": [
                "Bibliografik faoliyatning subyekti",
                "Bibliografik faoliyatning jarayonlari",
                "Bibliografik faoliyatning vositalari",
                "Bibliografik faoliyatning natijalari"
            ],
            "correct": 3
        },
        {
            "question": "Hujjatlarni umumiy bibliografik tahlil qilishdan maqsad?",
            "options": [
                "Hujjatning mazmuni va shakli bilan tanishish",
                "Kitobxonlik doirasini aniqlash",
                "Yordamchi ko‘rsatkichlarni tuzish",
                "Hujjatni tasvirlash"
            ],
            "correct": 3
        },
        {
            "question": "48-sahifagacha bo‘lgan matnli nashr qanday nomlanadi?",
            "options": [
                "Kitob",
                "Varaqa",
                "Risola",
                "Jurnal"
            ],
            "correct": 2
        },
        {
            "question": "Bibliografik qo‘llanmalarning nechta asosiy turi mavjud?",
            "options": [
                "Bibliografik ko‘rsatkich",
                "Bibliografik ro‘yxat",
                "Bibliografik sharh",
                "Yuqoridagi barcha javoblar to‘g‘ri"
            ],
            "correct": 3
        },
        {
            "question": "An`anaviy ma`lumot bibliografiya apparati qanday tarkibiy qismlardan iborat?",
            "options": [
                "Aynan shu kutubxona uchun mos va zarur kutubxona kataloglar tizimi.",
                "Kartotekalar tizimi.",
                "Ma`lumot bibliografiya fondi",
                "To‘g‘ri javob A, B, C"
            ],
            "correct": 3
        },
        {
            "question": "“Bibliografiya” so‘zining ma`nosini aniqlang?.",
            "options": [
                "Kitob ko‘chirish",
                "Kitob yozayapman",
                "Kitob qidirish",
                "Kitob tasvirlash"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografiya fani qachon va qayerda birinchi marotaba vujudga kelgan?",
            "options": [
                "Gretsiya er. oldingi III asr",
                "Angliya V asr",
                "Fransiya III asr",
                "Misr – er. oldingi V asr"
            ],
            "correct": 0
        },
        {
            "question": "XVI - XVIII asrlarda Buhoroda ikkita yirik saroy kutubhonalari mavjud bo'lgan. Bu kutubhonalardan biri",
            "options": [
                "SHayboniylar saroyi kutubhonasidir.",
                "Temur kutubxonasi",
                "Saroy kutubhonasi",
                "Barchasi to’g‘ri"
            ],
            "correct": 0
        },
        {
            "question": "200 shoir ijodidan namunalarni o'z ichiga olgan antalogiya tuzildi?",
            "options": [
                "1692 yil",
                "1690 yil",
                "1693 yil",
                "Barchasi to’g‘ri"
            ],
            "correct": 0
        },
        {
            "question": "Markaziy Osiyo mintaqasida dastlabki kutubxonalar qachon paydo bo‘lgan?",
            "options": [
                "IV-VI asr.",
                "Eramizdan avvalgi IV-VI asrlar.",
                "VIII asr.",
                "28"
            ],
            "correct": 0
        },
        {
            "question": "Abu Ali ibn Sino 17 yoshida qaysi kutubxonadan foydalangan?",
            "options": [
                "Xiva xoni kutubxonasida",
                "Buxoro amiri kutubxonasida",
                "Qo‘qon xoni kutubxonasida",
                "Amir Temur kutubxonasida"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxonashunoslikning ilmiy davrini rivojlanishi... bo‘linadi.?",
            "options": [
                "Ikki davrga",
                "Besh davrga",
                "Uch davrga",
                "Yetti davrga"
            ],
            "correct": 2
        },
        {
            "question": "Nechinchi asrlarda O'rta Osiyoning yirik davlatlarida shaxsiy kutubhonalar, madrasa va machitlar oldida kutubxonalar hamda kitob bozorlari ishi rivojlandi.?",
            "options": [
                "XV asrda;",
                "XVI asrda;",
                "X.VIII asrda;",
                "XVII asrda"
            ],
            "correct": 0
        },
        {
            "question": "Tarixchi, adabiyot shunos amir amaldorlaridan biri kutubhonaning ohirgi yillaridagi rahbar va jonkuyarlaridan bo’lgan inson kim edi.?",
            "options": [
                "Muhammad SHarif Sadr Ziyo:",
                "Ibn Sino;",
                "Amir;",
                "Barchasi to’g‘ri"
            ],
            "correct": 0
        },
        {
            "question": "Nechanchi asrlarda Hiva honligida ham madaniyat va fan ancha rivojlangan bo'lib, kitob yig’ish va kutubhonalarga e'tibor katta edi.?",
            "options": [
                "X - XI asrda;",
                "XV - XVI asrda;",
                "XVII - XVIII asrda;",
                "XVIII - XIX asrda"
            ],
            "correct": 3
        },
        {
            "question": "Nechanchi yillarda Muhammad Rahimhon II hukmronligi davrida saroy kutubhonasi fondi yanada kengayib boyigan?",
            "options": [
                "1865-1910;",
                "1865-1920;",
                "1860-1910;",
                "1860-1900;"
            ],
            "correct": 0
        },
        {
            "question": "Nechanchi asrlarda Hivada bosmahona tashkil etilgan.?",
            "options": [
                "X asrning 70 yillarida;",
                "XVIII asrning 70 yillarida;",
                "XV asrning 70 yillarida;",
                "XVII asrning 70 yillarida"
            ],
            "correct": 1
        },
        {
            "question": "Rejalashtirish nima?",
            "options": [
                "Bu rahbariyat harakatlarining yagona yo‘nalishini, tashkilot aʼzolarining umumiy maqsadlariga erishish yo‘lidagi harakat birligini taʼminlash vositalaridan biridir.",
                "Umumiy maqsadlariga erishish yo‘lidagi harakat birligini taʼminlash vositalaridan biridir.",
                "Yil davomida qilinishi zarur bo‘lgan ishlarni aniqlash.",
                "Harakatlarni yagona yo‘nalishga birlashtirish."
            ],
            "correct": 0
        },
        {
            "question": "Strategik rejalashtirish deganda nimani tushunasiz?",
            "options": [
                "Rahbariyat tomonidan qo‘llaniladigan va tashkilotni o‘z maqsadlariga erishishi uchun yordam beradigan o‘ziga mos strategiyani ishlab chiqishga olib keladigan harakatlar, tadbirlar, qarorlar to‘plami.",
                "Tashkilotni o‘z maqsadlariga erishishi uchun yordam beradigan o‘ziga mos strategiyani ishlab chiqishga olib keladigan harakatlar.",
                "Tashkilotni o‘z maqsadlariga erishishi uchun yordam beradigan o‘ziga mos strategiyani ishlab chiqishga olib keladigan tadbirlar.",
                "Tashkilotni o‘z maqsadlariga erishishi uchun yordam beradigan qarorlar."
            ],
            "correct": 0
        },
        {
            "question": "Kutubxona-axborot faoliyatini rejalashtirish qanday tamoyillarga asoslanadi?",
            "options": [
                "Ilmiylik va joriy ishlarni istiqbol ishlar bilan uyg‘unlashtirish.",
                "Rejani bajarilishi shartliligi",
                "Rejani muvofiqlashganligi va aniqligi.",
                "Barcha javoblar to‘g‘ri."
            ],
            "correct": 3
        },
        {
            "question": "Kutubxonalarda qaysi turdagi rejalar ishlatiladi?",
            "options": [
                "Yillik.",
                "Chorak (kvartal).",
                "Oylik",
                "Barcha javoblar to‘g‘ri"
            ],
            "correct": 3
        }
    ],














    "4": [
        {
            "question": "Nechanchi yillarda Hiva xoni kutubxonasi boshqa tildagi jurnal va kitoblar bilan yanada boyib ketdi?",
            "options": [
                "1870 yil may oyidan boshlab",
                "1871 yil may oyidan boshlab",
                "1872 yil may oyidan boshlab",
                "1873 yil may oyidan boshlab"
            ],
            "correct": 3
        },
        {
            "question": "Kutubhonaning bebaho nodir qo'lyozma asarlarining juda katta qismi qachon general K. P. Kaufman tomonidan Peterburg ommaviy kutubhonasiga sovg’a qilingan?",
            "options": [
                "1874 yil",
                "1870 yil",
                "1872 yil",
                "1871 yil"
            ],
            "correct": 0
        },
        {
            "question": "Nechanchi asrlarda O'rta Osiyo hududida Buhoro amirligi va Hiva honligidan keyin Qo'qon honligi yuzaga keldi?",
            "options": [
                "XV asrda",
                "XVI asrda",
                "XVIII asrda",
                "XVII asrda"
            ],
            "correct": 2
        },
        {
            "question": "Nechanchi yillarda shoir Yusuf Tunqator va hattot Yusuf Muhammad tomonidan «18 nafar shoirlarning to'plami» asarlari antalogiyasi ozroq nushada toshbosmada chiqarilgan?",
            "options": [
                "1822 yil",
                "1820 yil",
                "1821 yil",
                "1823 yil"
            ],
            "correct": 0
        },
        {
            "question": "Muhammad-Rahim o'zi kitob yig’ishga qiziqib, necha yil ichida u Hindiston, Afg’oniston va boshqa davlatlarga sayohat qilib, bebaho kitoblarni qidirgan va vataniga olib kelgan?",
            "options": [
                "25 yil",
                "26 yil",
                "27 yil",
                "28 yil"
            ],
            "correct": 2
        },
        {
            "question": "Nechanchi yil ruslarning Qo'qonga yurishidan so'ng hon kutubhonasidan 103 ta arab tilida yozilgan, asosan diniy harakterdagi qo'lyozma kitoblar tortib olingan.",
            "options": [
                "1874 yil",
                "1875 yil",
                "1876 yil",
                "1878 yil"
            ],
            "correct": 1
        },
        {
            "question": "Nechanchi asrlarda madrasalar qoshida kutubhonalar bo'lib, qo'lyozma kitoblarni to'plovchi kishilar soni ham ko'payib ketdi?",
            "options": [
                "XI asr ohiri va XII asr boshlarida",
                "XIV asr ohiri va XV asr boshlarida",
                "XIX asr ohiri va XX asr boshlarida",
                "XI asr ohiri va XIII asr boshlarida"
            ],
            "correct": 2
        },
        {
            "question": "Nechanchi asrlarda Qo'qon honligi katta shaharlarida va Toshkentda 20 ta yirik madrasalar bo'lib, unda talabalar uchun kutubhonalar ham bo'lgan?",
            "options": [
                "XIX asrning ikkinchi yarmida",
                "XVIII asrning ikkinchi yarmida",
                "XVII asrning ikkinchi yarmida",
                "XIII asrning ikkinchi yarmida"
            ],
            "correct": 0
        },
        {
            "question": "O'zbekiston hududida nechanchi asrlarda shaxsiy kutubhonalar ham yuzaga kelgan.",
            "options": [
                "XVIII asr ohiri XIX asr boshlarida",
                "XIX asr ohiri XXI asr boshlarida",
                "XIX asr ohiri XX asr boshlarida",
                "XVII asr ohiri XVIII asr boshlarida"
            ],
            "correct": 2
        },
        {
            "question": "Nechanchi yilda Xiva xoni Sayyid Muhammad Rahimxon II saroyida birinchi toshbosma bosmaxonasi ochildi?",
            "options": [
                "1874-yilda",
                "1875-yilda",
                "1873-yilda",
                "1872-yilda"
            ],
            "correct": 0
        },
        {
            "question": "Dastlabki kitob bosuvchi Xorazmda tug‘ilib o‘sgan yosh turkman yigiti kim?",
            "options": [
                "Hikmat Abdalov bo‘ldi",
                "Otajon Berdi bo‘ldi",
                "Otajon Abdalov bo‘ldi",
                "Barchasi to’g‘ri"
            ],
            "correct": 2
        },
        {
            "question": "Ibrohim tomonidan tuzilgan taqvim nechanchi yili o‘zbek tilida chop etilgan?",
            "options": [
                "1871-yil taqvimi",
                "1870-yil taqvimi",
                "1872-yil taqvimi",
                "1873-yil taqvimi"
            ],
            "correct": 0
        },
        {
            "question": "Xivadagi toshbosmada nechanchi yilda Alisher Navoiyning mashhur «Xamsa» asari chop etildi?",
            "options": [
                "1881-yilda",
                "1882-yilda",
                "1883-yilda",
                "1880-yilda"
            ],
            "correct": 3
        },
        {
            "question": "Nechanchi yilda sharqshunoslar jamiyatining Toshkent bo‘limi vujudga keldi va o‘zining kutubxonasiga ega bo‘ldi?",
            "options": [
                "1901-yilda",
                "1902-yilda",
                "1903-yilda",
                "Barchasi to’g‘ri"
            ],
            "correct": 0
        },
        {
            "question": "Markaziy Osiyo mintaqasida dastlabki kutubxonalar qachon paydo bo'lgan?",
            "options": [
                "V-VI asrlarda",
                "VI-VII asrlarda",
                "IV-VI asrlarda",
                "VII-VIII asrlarda"
            ],
            "correct": 2
        },
        {
            "question": "Markaziy Osiyo mintaqasida kutubhonalarni rivojlanishiga qachondan boshlab Samarqanda yuqori sifatli qog’oz ishlab chiqarish yo'lga qo'yildi?",
            "options": [
                "VIII asrdan",
                "VII asrdan",
                "IX asrdan",
                "Barchasi to’g‘ri"
            ],
            "correct": 0
        },
        {
            "question": "Jahonda kutubhonashunoslikni fan sifatida shakllanishiga asosiy shart-sharoitlar qachondan boshlab paydo bo'ldi?",
            "options": [
                "XV asrning oiri-XVI asrning boshlarida",
                "XVIII asrning oiri-XIX asrning boshlarida",
                "XVII asrda",
                "XVIII asrda"
            ],
            "correct": 1
        },
        {
            "question": "Vetnamdagi eng birinchi kutubxona?",
            "options": [
                "qaysi Dayxn omborxonasi hisoblanadi",
                "Xitoy",
                "Yaponiya",
                "Vetnam omborxonasi"
            ],
            "correct": 0
        },
        {
            "question": "Qachon Xanoyda adabiyotlar saroyi tashkil topdi?",
            "options": [
                "1071 yil",
                "1080 yil",
                "1070 yil",
                "1075 yil"
            ],
            "correct": 2
        },
        {
            "question": "Qachon mug’ul bosqinchilari Xitoy, Pagan va boshqa mamlakatlar kutubxonalari va madaniyatini supirib tashladi?",
            "options": [
                "XII asrda",
                "XIII asrda",
                "XI asrda",
                "X asrda"
            ],
            "correct": 0
        },
        {
            "question": "Kutubxonashunoslikni ilmiy va o‘quv predmeti sifatida paydo bo‘lishi va shakllanishi nechanchi asrga to’g’ri keladi?",
            "options": [
                "XIX asr",
                "XX asr",
                "XVIII asr",
                "XI asr"
            ],
            "correct": 0
        },
        {
            "question": "Birinchi bo‘lib “kutubxonashunoslik” atamasini aniq joriy etish lozim ekanligini anglab yetgan myunxenlik kutubxonachi ...",
            "options": [
                "A.Grezelning",
                "V.I.Sobolshikov",
                "N.A.Rubakin",
                "M. Shrettinger"
            ],
            "correct": 3
        },
        {
            "question": "Nechanchi yili M. Shrettinger “Kutubxonashunoslikka raxbarlik qilish” asari nashr etilgan?",
            "options": [
                "1884 yil",
                "1844 yil",
                "1834 yil",
                "1934 yil"
            ],
            "correct": 2
        },
        {
            "question": "Kutubxonashunoslik fanining amaliy fandan ilmiy fanga aylana boshlanishining dastlabki belgilari nechanchi asrlarda paydo bo‘la boshladi? va bu jarayonga xissasi katta bo‘lgan inson kim?",
            "options": [
                "Kutubxonashunos olim V.I.Sobolshikov XIX asrning oxirlariga",
                "Nemis kutubxonashunos olimi A.Grezelning XIX asrning oxirlariga",
                "Rus kutubxonashunos olimi N.A.Rubakin XIX asrning oxirlariga",
                "Nemis kutubxonashunos olimi A.Grezelning XX asrning oxirlariga"
            ],
            "correct": 1
        },
        {
            "question": "Dastlabki kutubxonachilikka oid jurnallar (“Serapeum”, Germaniyada 1840 yil; “Bibliotechniy jurnal” AQSH, 1876 yil;)",
            "options": [
                "“Serapeum”",
                "Bibliotechniy jurnal",
                "“Serapeum”, Germaniyada 1840 yil; “Bibliotechniy jurnal” AQSH, 1876 yil",
                "“Bibliotechniy jurnal” AQSH, 1876 yil"
            ],
            "correct": 2
        },
        {
            "question": "Rossiyada kutubxonashunoslik fanini rivojlantirishga katta xissa qo‘shdilar....",
            "options": [
                "V.I.Sobolshikov, N.A.Rubakin, A.A. Pokrovskiy, K.I.Rubinskiy, L.B.Xavkina va boshqalar",
                "M. Shrettinger, N.A.Rubakin, A.A. Pokrovskiy",
                "Y.Forstius, G.Leydinger, A.Predeyek, O.S.Chubaryan",
                "N.A.Rubakin, A.A. Pokrovskiy, A.Predeyek, O.S.Chubaryan"
            ],
            "correct": 0
        },
        {
            "question": "O‘zbekistonda “kutubxonashunoslik” atamasi ilk bor kimlarning asarlarida qo‘llanildi?",
            "options": [
                "M. Shrettinger, N.A.Rubakin, A.A. Pokrovskiy",
                "Y.Forstius, G.Leydinger, A.Predeyek, O.S.Chubaryan",
                "YE.K.Betger, A.V.Korshun, V.N.Smolin, N.A.Burov, O.V.Maslova",
                "Y.Forstius, G.Leydinger"
            ],
            "correct": 2
        },
        {
            "question": "Nechanchi asrda dastlabki kutubxonachilik maktablari va kurslari paydo bo‘ldi va u yerda kutubxonashunoslik o‘quv predmeti sifatida o‘qitila boshlandi?",
            "options": [
                "XX asrda u dunyo miqyosid yagona fan sifatida rivojlandi",
                "XIX asrda u dunyo miqyosid yagona fan sifatida rivojlandi",
                "XVIII asrda u dunyo miqyosid yagona fan sifatida rivojlandi",
                "XVII asrda u dunyo miqyosid yagona fan sifatida rivojlandi"
            ],
            "correct": 1
        },
        {
            "question": "O‘rta Osiyoda birinchi kutubxona xodimlarining ikki oylik malaka oshirish kurslari nechanchi yilda ochildi?",
            "options": [
                "1919 yil",
                "1918 yil",
                "1920 yil",
                "1917 yil"
            ],
            "correct": 0
        },
        {
            "question": "Vektarinalar mazmuniga ko'ra qanday turlarga ajratiladi?",
            "options": [
                "Muallif ijodiga bag'ishlangan savol javob o'yinlari.",
                "Muallif ijodiga bag'ishlangan savol javob o'yinlari, bir asarga bag'ishlangan savol javob o'yinlari, mavzuli vektorinalar, teatrlashtirilgan vektorinalar",
                "Bir asarga bag'ishlangan savol javob o'yinlari.",
                "Mavzuli vektorinalar, teatrlashtirilgan vektorinalar"
            ],
            "correct": 1
        },
        {
            "question": "Kitob ko'rgazmasi mazmuniga ko'ra qanday turlarga bo’linadi?",
            "options": [
                "Ko'rgazmali",
                "Universal, mavzuli",
                "Mavzuli",
                "Universal"
            ],
            "correct": 1
        },
        {
            "question": "Kitob ko'rgazmasi vaqtiga ko'ra –",
            "options": [
                "Doimiy, vaqtinchalik, uzoq muddatga mo'ljallangan",
                "Doimiy",
                "Vaqtinchalik",
                "Sanalarga bag’ishlab"
            ],
            "correct": 0
        },
        {
            "question": "Kitob ko'rgazmasini tayyorlashda birinchi nima tanlaymiz?",
            "options": [
                "Yangi adabiyotlar ko'rgazmasi",
                "Muhim mavzuni tanlab olamiz",
                "Joy tanlab olamiz",
                "Barchasi to’g’ri"
            ],
            "correct": 1
        },
        {
            "question": "Bibliografik sharh –",
            "options": [
                "Reklama qilish",
                "Axborotni etkazish",
                "Foydalanuvchiga axborotni etkazish, muayyan hujjatlarni targ'ibot va reklama qilishning keng tarqalgan va etarli darajada samarali hisoblangan vositasidir.",
                "Ma’lumot berish"
            ],
            "correct": 2
        },
        {
            "question": "Konferenciya so‘zining ma’nosi nima?",
            "options": [
                "Lот. conferentia–biror joyga to’playman",
                "Jamlayman",
                "Lот. conferentia–guruhni to’playman",
                "Barchasi to’g’ri"
            ],
            "correct": 0
        },
        {
            "question": "Konferenciyani tayyorlash uchun qancha vaqt ajratiladi.",
            "options": [
                "1,5 oy",
                "1 oy",
                "2 oy",
                "Barchasi to’g’ri"
            ],
            "correct": 1
        },
        {
            "question": "Markaziy Osiyo mintaqasida dastlabki kutubxonalar qachon paydo bo‘lgan?",
            "options": [
                "IV-VI asr",
                "Eramizdan avvalgi V-VI asrlar.",
                "VIII asr",
                "II asr"
            ],
            "correct": 0
        },
        {
            "question": "O‘zbekiston Respublikasi Prezidentining qabul qilingan \"Kitob mahsulotlarini nashr ettirish va tarqatish tizimini rivojlantirish, kitob mutolaasi va kitobxonlik madaniyatini oshirish hamda targ‘ib qilish bo‘yicha kompleks chora-tadbirlar dasturi to‘g‘risida\"gi Qarori qachon qabul qilingan?",
            "options": [
                "2017 yil, 13 sentabrda.",
                "2017 yil, 10 sentabrda",
                "2018 yil, 13 sentabrda",
                "2019 yil, 12 sentabrda"
            ],
            "correct": 0
        },
        {
            "question": "Motiv lotinchada qanday ma’noni bildiradi?",
            "options": [
                "O’rganaman",
                "“Harakatlantiraman”",
                "Izlanaman",
                "O’qiyman"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxonachilarning asosiy vazifalaridan biri nima?",
            "options": [
                "Kutubxona axborot xizmati jarayonini iloji boricha soddalashtirish va tushunarli tarzda tashkil etishga e’tibor berishdir.",
                "O’z ustida ishlash",
                "Kompyuterni bilish",
                "Shirinso’z bo’lish"
            ],
            "correct": 0
        },
        {
            "question": "Axborot madaniyati deganda nimani tushunasiz?",
            "options": [
                "Avvalo, axborotga bo‘lgan ehtiyojni his etish, uni topish, saralay bilish va baholash, tezkor tahlil qila bilish va samarali foydalanish uchun zarur bo‘lgan malakalar majmuasidir.",
                "Avvalo, axborotga bo‘lgan ehtiyojni his etish",
                "Tezkor tahlil qila bilish va samarali foydalanish",
                "Kutubxonachi foydalanuvchilarning bilim olishi yo‘lidagi doimiy xamroxi sifatida kerakli ma’lumotlarni osonlik bilan topish"
            ],
            "correct": 0
        },
        {
            "question": "Kutubxonachi qanday sifatlarga ega bo‘lishi talab qilinadi?",
            "options": [
                "Ma’lumotlar oqimidan kerakli axborotni ola bilishdan iborat",
                "Har qanday zaruriy ishga o‘z-o‘zini majbur qila olish ko‘nikmasi",
                "Tafakkur sifati, Diqqatlilik sifati, Iroda sifati, Kommunikativ sifati",
                "Tafakkur sifati"
            ],
            "correct": 2
        },
        {
            "question": "Nutq madaniyatining asosiy qoidalari nimalardan iborat?",
            "options": [
                "Nutq madaniyati ko‘nikmalarini hosil etish",
                "Nutq madaniyati ko‘nikmalarini hosil etish, nutq so‘zlashga bevosita tayyorgarlik ko‘rish; nutq so‘zlash vaqtida o‘zini tutish.",
                "Ifodali o’qish",
                "Nutq so‘zlashga bevosita tayyorgarlik"
            ],
            "correct": 1
        },
        {
            "question": "Zamonaviy ko‘rinishdagi ensiklopediyalarning ilk namunasi nechanchi asrda yaratilgan?",
            "options": [
                "XVIII asrda yaratilgan",
                "XV asrda yaratilgan",
                "XVI asrda yaratilgan",
                "XVII asrda yaratilgan"
            ],
            "correct": 0
        },
        {
            "question": "Kutubxona – axborot xizmati texnologiyasi o‘z ichki tizimiga ko‘ra nimalardan tashkil topadi?",
            "options": [
                "O‘rgatish",
                "Tushuntirish, tushunish, o‘rgatish, o‘rganish, o‘zlashtirish",
                "Yozish",
                "Internetdan foydalanish"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxonalararo abonoment –",
            "options": [
                "Nashr mahsulotlari yoki boshqa hujjatlardan muayyan vaqt davomida foydalanish",
                "Muayyan kutubxona fondida mavjud bo‘lmagan hollarda boshqa kutubxonalar fondidagi bosma nashrlar yoki hujjatlardan ma’lum muddatga olib foydalanish shaklidir",
                "Kutubxonada foydalanish",
                "Barchasi to’g’ri"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxonalararo abonoment tizimi birinchi bo‘lib qayirda qo‘llanila boshlagan?",
            "options": [
                "1892 yildan Germaniyada qo‘llanila boshlagan",
                "1892 yildan Fransiyada qo‘llanila boshlagan",
                "1890 yildan Rossiyada qo‘llanila boshlagan",
                "1892 yildan Amerikada qo‘llanila boshlagan"
            ],
            "correct": 0
        },
        {
            "question": "Kitoblarni saqlash tartibi deganda nimalarga amal qilish kerak?",
            "options": [
                "Tozalik",
                "Yorug’lik va issiqlik",
                "Ko’rgazmaga qo’yish",
                "Harorat, namlik, yorug’lik, sanitariya-gigiyenik"
            ],
            "correct": 3
        },
        {
            "question": "Tizim administratorining AIO'da bajariladigan asosiy vazifalar nimalardan iborat?",
            "options": [
                "Maxsus konstruktor yordamida ma'lumotlarni kiritish formasini (MARS formatlar oilasiga mansub) yaratish, kiritish, shakllni tanlash va o'rnatish.",
                "Ma'lumotlar bazalarini yaratish va kerak bo'lmaganlarini o'chirish.",
                "Tizmdan foydalanuvchilar (administrator, kutubxonachi, kitobxon va boshqalar) uchun tegishlistatuslar o'rnatish.",
                "Hamma javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "Elektron katalogning asosiy vazifalari necha qismdan iborat?",
            "options": [
                "5 ta",
                "4 ta",
                "6 ta",
                "7 ta"
            ],
            "correct": 2
        },
        {
            "question": "Elektron katalogning asosiy vazifalari qaysi javobda to'liq va aniq keltirilgan?",
            "options": [
                "Kutubxona fondi tarkibi va mazmunini har tomonlama ochib berish hamda kutubxona fondida mavjud hujjatlar shaklidagi axborotlarni ko'p qirrali tezkor qidiruvini ta'minlash;",
                "Kutubxona resurslarini Internet tarmog'i orqali jahon axborot zahiralari bilan integrasiyalashuvini ta'minlash va axborotlarni himoya qilish;",
                "Foydalanuvchilar uchun axborotlardan foydalanish uchun hamda axborotlardan foydalanish uchun qulay sharoitlar yaratish;",
                "Barchajavoblar"
            ],
            "correct": 3
        },
        {
            "question": "Kartochkali katalogdan elektron ko'rinishli katalogga o'tish yo'llari necha turda amalga oshiriladi?",
            "options": [
                "2",
                "3",
                "4",
                "5"
            ],
            "correct": 1
        },
        {
            "question": "Yig'ma EK yaratishning asosiy shartlari nima?",
            "options": [
                "Korporativ axborot tizimini yaratish",
                "Internet axborot tizimini yaratish",
                "Intranet axborot tizimini yaratish",
                "Hamma javoblar to'g'ri"
            ],
            "correct": 3
        },
        {
            "question": "ON LINE nima?",
            "options": [
                "Real vaqt rejimida Internetga kirish;",
                "Jamoatchilik tomonidan foydalaniladigan tezkor katalog;",
                "Bir kompyuterdan boshqasiga axborot jo'natish usuli jarayoni;",
                "Elektron kutubxona katalogidagi qidiruv tizimi"
            ],
            "correct": 0
        },
        {
            "question": "Skaner - bu",
            "options": [
                "Axborot va dasturiy resurslardan birgalikda foydalanish maqsadida o'zaro birlashtirilgan kompyuterlar majmuidir;",
                "Bu axborotlarni jo'natuvchi va qabul qiluvchi maxsus qurilma;",
                "Matnli va grafik axborotlarni kompyuter xotirasiga kirituvchi qurilma;",
                "Bu qurilma bir paytning o'zida bir necha SD-disklarni joylashtirish va turli manbalarga murojaat qilish imkoniyatini beradi"
            ],
            "correct": 2
        },
        {
            "question": "Maxsus dasturiy ta'minotning ta'rifi qaysi javobda to'g'ri keltirilgan?",
            "options": [
                "Bu biror predmet sohasi bilan bog'liq;",
                "Aniq amaliy masalalarni avtomatlashtirish uchun mo'ljallangan dastur yoki dasturlar majmui;",
                "A va V javoblar;",
                "Bu amaliy masalalar dasturi"
            ],
            "correct": 2
        },
        {
            "question": "Axborot resursi bu-?",
            "options": [
                "Matnli va ovozli ma’lumotlar",
                "Tasvirlar va video ma’lumotlar",
                "Matn ko‘rinishidagi materiallar, ovozli yozuvlar va tasvirlardir.",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Jahon axborot resurslari nima?",
            "options": [
                "Dunyo bo’yicha barcha ma’lumotlarning yig’indisi",
                "Jamiyat tomonidan tan olingan nashriyotlarning axborot resurslari",
                "Ma’lumotlar jamlanmasi",
                "Jahonning Ma’lumotlar massivi"
            ],
            "correct": 1
        },
        {
            "question": "Jahonning yetakchi nashriyotlari ko’rsatilgan qatorni ko’rsating.",
            "options": [
                "Cambridge University Press, Oxford University Press",
                "Wiley, EBSCO Information Services",
                "Bio One, Scopus, Web of Science",
                "Barchasi to’g’ri keltirilgan"
            ],
            "correct": 3
        },
        {
            "question": "Konsorsium so'zining ma’nosi qanday?",
            "options": [
                "Lotincha “ishtirok etish” degani",
                "Ingliz tilidan olingan bo’lib “ishtirok etish” degani",
                "Lotincha “shirkat” degan ma’noni anglatadi",
                "A va S javoblari to’g’ri"
            ],
            "correct": 3
        },
        {
            "question": "EBSCO Information Services bu -?",
            "options": [
                "Konsorsium",
                "Nashriyot",
                "Kutubxona markazi",
                "To’g’ri javob yo’q"
            ],
            "correct": 1
        },
        {
            "question": "Konsorsium nima?",
            "options": [
                "Bu ba’zi bir umumiy maqsadlarni amalga oshirish uchun tashkilotlarning birlashmasidir.",
                "Muammlolarni hal qiladigan tashkilot",
                "Yuqori sifatli xizmat ko’rsatuvchi agregator",
                "Ma’lumotlarni elektron tarzda foydalanuvchiga yetkazib beruvchi birlashma"
            ],
            "correct": 0
        },
        {
            "question": "EIFL.NET bu-?",
            "options": [
                "Milliy axborot qidiruv tizimi",
                "Konsorsium",
                "Nashriyot",
                "B va S javoblari to’g’ri"
            ],
            "correct": 1
        },
        {
            "question": "Konsorsiumlar birlashishining afzalliklari nimada?",
            "options": [
                "Bir birini himoya qilish",
                "Resurslardan birgalikda foydalanish",
                "Islohatlar o’tkazish, yig’ilishlarda ishtirok etish",
                "To’g’ri javob yo’q"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxona axborot resurslari bu?",
            "options": [
                "Kutubxonada saqlanayotgan hujjatlar",
                "Kutubxonaga oid hujjatlar",
                "Saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot",
                "B va S javoblar to’g’ri"
            ],
            "correct": 2
        },
        {
            "question": "Ilmiy-ta’limiy resurslar deb qanday resurslarga aytiladi?",
            "options": [
                "Litsenziyalangan resurslarga aytiladi",
                "Taqrizdan o’tgan resurslarga aytiladi",
                "Jahon bo’yicha qo’llaniluvchi resurslarga aytiladi",
                "A va B javoblar to’g’ri"
            ],
            "correct": 3
        }
    ],














    "5": [
         {
            "question": "Istiqbolni belgilash deganda nimani tushunasiz?",
            "options": [
                "Bu hayot taraqqiyoti qonuniyatlarini o‘rganish asosida u yoki bu hodisaning kelajagini oldindan ko‘rish.",
                "U yoki bu hodisaning kelajagini oldindan ko‘rish.",
                "Kelajakni idrok etish.",
                "Uzoq muddatli rejalar ishlab chiqish."
            ],
            "correct": 0
        },
        {
            "question": "Istiqbolni belgilashning qanday usullarini bilasiz?",
            "options": [
                "Ekstrapolyatsiya usuli",
                "Ekspertiza usuli",
                "Tahlili usuli",
                "Barcha javoblar to‘g‘ri."
            ],
            "correct": 3
        },
        {
            "question": "Uslubiy markazlar deganda nimani tushunasiz?",
            "options": [
                "Bu kutubxona va axborot tarmoqlariga ilmiy-uslubiy ishlarni va uslubiy ishlarni amalga oshiradigan markaziy kutubxonalar.",
                "Ilmiy-uslubiy ishlarni amalga oshiruvchi kutubxonalar.",
                "Ilmiy-uslubiy ishlarni amalga oshiruvchi bo‘limlar.",
                "Uslubiy ishlarni amalga oshiruvchi kutubxonalar."
            ],
            "correct": 0
        },
        {
            "question": "Uslubiy xizmatni tashkil etish tamoyillarini ko‘rsating?",
            "options": [
                "Ilmiylik, tavsiyaviylik, bosh mavzuni ajratish.",
                "Faollik, bevosita bog‘lanish.",
                "Tabaqalashtirish, tezkorlik, muntazamlilik va rejalilik.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "O‘zbekiston Respublikasi Prezidentining 'Respublika aholisini axborot-kutubxona bilan taʼminlashni tashkil etish to‘grisida'gi qaroriga muvofiq qaysi kutubxonalar ilmiy-uslubiy markazlar vazifasini bajaradilar?",
            "options": [
                "O‘zbekiston Milliy kutubxonasi-Respublika uslubiy markazi-idoralararo kengashning ishchi organi.",
                "Mirzo Ulug‘bek nomidagi Milliy universitetning ilmiy kutubxonasi-Oliy taʼlim muassasalari ARM lariga va O‘zbekiston Respublikasi Ilmiy pedagogika kutubxonasi-Xalq taʼlimi muassasalari ARM lariga uslubiy markaz.",
                "Qoraqalpog‘iston Respublikasi, viloyatlar va Toshkent shahar axborot-kutubxona markazlari - mintaqaviy uslubiy markaz.",
                "Barcha javoblar to‘gri."
            ],
            "correct": 3
        },
        {
            "question": "Uslubiy qo‘llanmalarning qanday asosiy turlarini bilasiz?",
            "options": [
                "Amaliy qo‘llanmalar, maslahatlar.",
                "Ilg‘or ish tajribalari, uslubiy-bibliografik",
                "Yo‘riqnoma-uslubiy xat, ilg‘or ish tajribalari.",
                "Amaliy, o‘quv-uslubiy, yo‘riqnoma-uslubiy."
            ],
            "correct": 3
        },
        {
            "question": "Uslubiy-bibliografik qo‘llanma deganda nimani tushunasiz?",
            "options": [
                "Uslubiy ishlanmalar.",
                "Ayrim tadbirlarni o‘tkazish uchun maslahatlar.",
                "Tavsiya nashrlar ro‘yxati.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Uslubiy materiallar deganda nimani tushunasiz?",
            "options": [
                "Uslubiy xatlarni va ilg‘or ish tajribalarini.",
                "Uslubiy tavsiyanomalarni.",
                "Yo‘riqnoma-uslubiy xatni",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Qanday uslubiy yordam shakllarini bilasiz?",
            "options": [
                "Og‘zaki shakllar-maslahatlar,maʼruzalar va obzorlar.",
                "Bosma shakllar- uslubiy qo‘llanmalar va ishlanmalar, axborot materiallari.",
                "Ko‘rgazmalari shakllari-plakatlar, kino va tele eshittirishlardan foydalanish va h.k.",
                "Barcha javoblar to‘gri"
            ],
            "correct": 3
        },
        {
            "question": "Boshqarish nima?",
            "options": [
                "Bu -mehnat taqsimoti ehtiyoji bilan hamda u bilan boglik kooperatsiya- umumiy maqsadga erishish uchun birgalikda kuch bilan vujudga keladigan faoliyatning maxsus turi.",
                "Bu -mehnat taqsimoti bilan bog‘lik kooperatsiya.",
                "Bu -umumiy maqsadga erishish uchun birgalikda kuch bilan vujudga keladigan faoliyatning maxsus turi.",
                "Bu- umumiy maqsadga erishish uchun odamlarni boshqarish."
            ],
            "correct": 0
        },
        {
            "question": "Ilmiy-ta’limiy resurslar to’g’ri ko’rsatilgan qatorni toping.",
            "options": [
                "Maqolalar, ilmiy nashrlar",
                "Faqat darsliklar",
                "Darsliklar, o’quv qo’llanmalar, monografiyalar, maqolalar, ilmiy tadqiqot ishlari",
                "Ilmiy tadqiqot ishlari"
            ],
            "correct": 2
        },
        {
            "question": "Erkin foydalanish bu-?",
            "options": [
                "Barcha ma’lumotlardan erkin foydalana olish jarayoni",
                "Barcha ma’lumotlarni yuklab olish, muallifning ruxsatisiz foydalanuvchilarga tarqatish",
                "Internet orqali kitobxonlarning bepul foydalanishi, o‘qish, yuklab olish, nusxa ko‘chirish, tarqatish va chop etish, qidirish, indekslash, qonun doirasida ma’lumot sifatida uzatish",
                "To’g’ri javob yo’q"
            ],
            "correct": 2
        },
        {
            "question": "Ma’lumot bazalari (data base) –?",
            "options": [
                "Resurslarni yetkazib beruvchi tashkilotlarning faoliyati",
                "Elektron resurslarning yig’indisi",
                "Ma’lumotlarning barchasi joylashtirilgan massiv",
                "Tasvirlash, saqlashning alohida qoidalar asosida tashkil etilgan amaliy dasturlar asosida tuzilgan ma’lumotlar yig‘indisidir."
            ],
            "correct": 3
        },
        {
            "question": "Plagiat nima?",
            "options": [
                "Ma’lumotlarni qayta ishlash jarayoni",
                "Resurslarni chop qiluvchi media kompaniya",
                "O‘zga muallif asarini atayin havolalarsiz, muallifga iqtiboslikni ko‘rsatmasdan shaxsiy asar sifatida ko‘rsatishga urinish",
                "A va S javoblari to'g'ri"
            ],
            "correct": 2
        },
        {
            "question": "Tashkilot (davlat, jamoat, kooperativ yoki xususiy) adabiyot, san’at, musiqa yoki fan sohasida faoliyat yuritib mahsulotlar yaratishi, ko‘paytirishi, tarqatishi mumkin bo‘lgan media-kompaniya- bu?",
            "options": [
                "Agregatorlar",
                "Hususiy tashkilotlar",
                "Nashriyotlar",
                "Mas’uliyati cheklangan jamiyat, korxonalar"
            ],
            "correct": 2
        },
        {
            "question": "Konsorsiumlarning maqsad va vazifalari to’g’ri keltirilgan qatorni belgilang",
            "options": [
                "Kutubxonalarning keyinchalik rivojlanishi va ularning to’planishi uchun axborot resurslarining birlashishini amalga oshirish",
                "Hamma kutubxonalar axborotiga taqsimlangan kirish huquqini ta’minlash, foydalanuvchilari uchun yagona axborot joyini yaratish",
                "Birlashish va kutubxona fondlaridan birgalikda foydalanish, resurslarni ayriboshlash, hujjatlarni elektron tarzda yuborish",
                "Barcha javoblar to’g’ri"
            ],
            "correct": 3
        },
        {
            "question": "O’zbekistonda konsorsiumlarga a’zo bo’lish qachondan boshlangan?",
            "options": [
                "2001 yildan",
                "2000 yildan",
                "O’zbekiston hech qanday konsorsiumga a’zo emas",
                "1999 yildan"
            ],
            "correct": 1
        },
       
    ],













    "6": [
        
        {
            "question": "Axborot resurslaridan foydalanishda asosiy e’tibor ….?",
            "options": [
                "Resurslarni ishlatishning huquqiy jihatiga qaratiladi",
                "Muallifning ismiga qaratiladi",
                "Resursning tarkibiga qaratiladi",
                "Hech narsaga e’tibor qaratmasdan resursdan hohlagancha foydalanish mumkin."
            ],
            "correct": 0
        },
        {
            "question": "Kutubxona-axborot resursiga to’g’ri ta’rif berilgan qatorni toping.",
            "options": [
                "Kutubxonada saqlanadigan resurslar",
                "Saqlash va foydalanishning alohida qoidalari asosida tashkil qilingan resurslar",
                "Kutubxonashunoslik sohasiga oid resurslar",
                "Identifikatsiyalash, saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot."
            ],
            "correct": 3
        },
        {
            "question": "Litsenziyalangan va taqrizdan o‘tgan ilmiy-ta’limiy axborotlar (jurnallar, maqola, kitoblar, multimedia va boshqalar).",
            "options": [
                "Ilmiy-ta’limiy resurslar.",
                "Saqlash va foydalanishning alohida qoidalari asosida tashkil qilingan resurslar",
                "Ta’limiy resurslar (o’quv qo’llanmalar, monografiyalar)",
                "Identifikatsiyalash, saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot."
            ],
            "correct": 0
        },
        {
            "question": "Mualliflik huquqi tushunchasi qachon paydo bo’ldi va nima maqsadda?",
            "options": [
                "XX asrda paydo bo’ldi va resurslarni himoya qilish maqsadida.",
                "XIX asrda paydo bo’ldi va intellectual mulkni himoya qilish uchun.",
                "XVIII asrning boshidayoq paydo bo’lgan, insonning intellektual faoliyatini himoya qilish va taqdirlash maqsadida.",
                "XVI asr va XVIII asrning boshidayoq paydo bo’lgan, insonning intellektual faoliyatini himoya qilish va taqdirlash maqsadida."
            ],
            "correct": 2
        },
        {
            "question": "O’zida mualliflik huquqini talab qilmaydigan ob’ektlar to’g’ri berilgan qatorni ko’rsating.",
            "options": [
                "Resurslardan foydalanganimizda foydalanilgan adabiyotlar ro’yhatini yozib qo’ysak, shu yetarli.",
                "Barcha resurslar o’zida mualliflik huquqini talab qiladi (kitoblar, jurnallar, maqolalar, ilmiy ishlar, tezislar, monografiyalar)",
                "Rasmiy hujjatlar (qonunlar, qarorlar va shu kabilar) hamda ularning tarjimalari mualliflik huquqi oby’ektlari hisoblanmaydilar; rasmiy belgilar va ramzlar (bayroqlar, gerblar, ordenlar, pul belgilar va shu kabilar); odatiy ommaviy axborot xususiyatiga ega kun yangiliklari to‘g‘risidagi yoki kundalik hodisalar to‘g‘risidagi xabarlar",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Muallif asardan har qanday shaklda va har qanday usul bilan foydalanish huquqiga ega. Nechanchi moddada berilgan?",
            "options": [
                "12-modda.",
                "19-modda.",
                "20-modda.",
                "4-modda."
            ],
            "correct": 1
        },
        {
            "question": "Fors-major holati to’g’ri ko’rsatilgan qatorni ko’rsating.",
            "options": [
                "Holatni o’rganish jarayoni.",
                "Shartnomani qayta tuzish jarayoni.",
                "Shartnomani bekor qilish.",
                "Favqulotda hodisalar ro’y berishi."
            ],
            "correct": 3
        },
        {
            "question": "O’zbekistonning jahonda tan olingan bazalari to’g’ri ko’rsatilgan qatorni belgilang.",
            "options": [
                "Multimediya ensiklopidiyalari, «Sharq miniatyurasi (XIV - XVII asrlar)»",
                "Trmiz 2500, Samarqand",
                "«Al-Farg‘oniy va Al-Buxoriy: tamaddun barpo etilishi»",
                "Barchasi"
            ],
            "correct": 2
        },
        {
            "question": "O‘zi noshirlik qilmagan holda elektron resurslarni yig‘uvchi kompaniyalar bu-?",
            "options": [
                "Ma’lumot bazalari",
                "Nashriyotlar",
                "Agregatorlar",
                "Barchasi"
            ],
            "correct": 2
        },
        {
            "question": "Korporatsiya so'zining ma’nosi qanday ma’noga ega?",
            "options": [
                "Inglizcha hamjamiyat degan ma’noni bildiradi",
                "Lotincha: corporatio — birlashma, uyushma, hamjamiyat",
                "Inglizcha, uyushma degan ma’noni bildiradi",
                "Lotincha tashkilot degan ma’noni bildiradi"
            ],
            "correct": 1
        }
    ],












    "7": [

        {
            "question": "Ohio Link bu nima?",
            "options": [
                "Amerikaning eng yirik nashriyoti",
                "Ogayo shtati orqali akademik kutubxonalarning konsorsiumi",
                "Buyuk Britaniyada tashkil qilingan nashriyot",
                "A va S javoblari to’g’ri"
            ],
            "correct": 1
        },
        {
            "question": "Turkiyada tashkil qilingan konsorsiumning nomini toping",
            "options": [
                "BIBSAM",
                "ELNET",
                "ANKOS",
                "EIFL.NET"
            ],
            "correct": 2
        },
        {
            "question": "Antaliyadagi kutubxonalar Universitet Konsorsiumi 39 ta Turkiya akademik kutubxonalarini o‘z ichiga oladi. Ushbu ta’rif konsorsiumga tegishli?",
            "options": [
                "Heal Link",
                "Ohio Link",
                "Ankos",
                "ELNET"
            ],
            "correct": 2
        },
        {
            "question": "Axborot resurslaridan foydalanishda asosiy e’tibor ….?",
            "options": [
                "Resurslarni ishlatishning huquqiy jihatiga qaratiladi",
                "Muallifning ismiga qaratiladi",
                "Resursning tarkibiga qaratiladi",
                "Hech narsaga e’tibor qaratmasdan resursdan hohlagancha foydalanish mumkin"
            ],
            "correct": 0
        },
        {
            "question": "Kutubxona-axborot resursiga to’g’ri ta’rif berilgan qatorni toping.",
            "options": [
                "Kutubxonada saqlanadigan resurslar",
                "Saqlash va foydalanishning alohida qoidalari asosida tashkil qilingan resurslar",
                "Kutubxonashunoslik sohasiga oid resurslar",
                "Identifikatsiyalash, saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot."
            ],
            "correct": 3
        },
        {
            "question": "Litsenziyalangan va taqrizdan o‘tgan ilmiy-ta’limiy axborotlar (jurnallar, maqola, kitoblar, multimedia va boshqalar).",
            "options": [
                "Ilmiy-ta’limiy resurslar.",
                "Saqlash va foydalanishning alohida qoidalari asosida tashkil qilingan resurslar",
                "Ta’limiy resurslar (o’quv qo’llanmalar, momografiyalar)",
                "Identifikatsiyalash, saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot."
            ],
            "correct": 0
        },
        {
            "question": "Mualliflik huquqi tushunchasi qachon paydo bo’ldi va nima maqsadda?",
            "options": [
                "XX asrda paydo bo’ldi va resurslarni himoya qilish maqsadida.",
                "XIX asrda paydo bo’ldi va intellectual mulkni himoya qilish uchun.",
                "XVIII asrning boshidayoq paydo bo’lgan, insonning intellektual faoliyatini himoya qilish va taqdirlash maqsadida.",
                "XVI asr va XVIII asrning boshidayoq paydo bo’lgan, insonning intellektual faoliyatini himoya qilish va taqdirlash maqsadida."
            ],
            "correct": 2
        },
        {
            "question": "O’zida mualliflik huquqini talab qilmaydigan ob’ektlar to’g’ri berilgan qatorni ko’rsating.",
            "options": [
                "Resurslardan foydalanganimizda foydalanilgan adabiyotlar ro’yhatini yozib qo’ysak, shu yetarli.",
                "Barcha resurslar o’zida mualliflik huquqini talab qiladi (kitoblar, jurnallar, maqolalar, ilmiy ishlar, tezislar, monografiyalar)",
                "Rasmiy hujjatlar (qonunlar, qarorlar va shu kabilar) hamda ularning tarjimalari mualliflik huquqi oby’ektlari hisoblanmaydilar; rasmiy belgilar va ramzlar (bayroqlar, gerblar, ordenlar, pul belgilar va shu kabilar); odatiy ommaviy axborot xususiyatiga ega kun yangiliklari to‘g‘risidagi yoki kundalik hodisalar to‘g‘risidagi xabarlar",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Muallif asardan har qanday shaklda va har qanday usul bilan foydalanish huquqiga ega. Nechanchi moddada berilgan?",
            "options": [
                "12-modda.",
                "19-modda.",
                "20-modda.",
                "4-modda."
            ],
            "correct": 1
        },
        {
            "question": "Fors-major holati to’g’ri ko’rsatilgan qatorni ko’rsating.",
            "options": [
                "Holatni o’rganish jarayoni.",
                "Shartnomani qayta tuzish jarayoni.",
                "Shartnomani bekor qilish.",
                "Favqulotda hodisalar ro’y berishi."
            ],
            "correct": 3
        },
        {
            "question": "O’zbekistonning jahonda tan olingan bazalari to’g’ri ko’rsatilgan qatorni belgilang.",
            "options": [
                "Multimediya ensiklopidiyalari, «Sharq miniatyurasi (XIV - XVII asrlar)»",
                "Trmiz 2500, Samarqand",
                "«Al-Farg‘oniy va Al-Buxoriy: tamaddun barpo etilishi»",
                "Barchasi"
            ],
            "correct": 2
        },
        {
            "question": "O‘zi noshirlik qilmagan holda elektron resurslarni yig‘uvchi kompaniyalar bu-?",
            "options": [
                "Ma’lumot bazalari",
                "Nashriyotlar",
                "Agregatorlar",
                "Barchasi"
            ],
            "correct": 2
        },
        
        {
            "question": "Oʻzbekistonda birinchi korporatsiyalar qachon paydo bo’lgan?",
            "options": [
                "XIX-asrning 90-yillaridan",
                "IX-asrning 60-yillaridan",
                "XX-asrning 70-yillaridan",
                "X-asrning 90-yillaridan"
            ],
            "correct": 0
        },
        {
            "question": "-- bu korporatsiya tizimida ishlatiladigan turli xil ilovalar o'rtasida ma'lumot uzatishni ta'minlaydigan tizim.",
            "options": [
                "Axborotlarni tarmoq orqali uzatish",
                "Tizimli tarmoq",
                "Bulutli texnologiya",
                "Korporativ tarmoq"
            ],
            "correct": 3
        },
        {
            "question": "Korporativ tarmoqning asosiy vazifasi?",
            "options": [
                "Axborotlarni tarmoq orqali uzatish ishlarini amalga oshirish va foydalanuvchilarga sifatli xizmatni taqdim etish",
                "Geografik jihatdan taqsimlanadi, ya'ni bir -biridan ancha uzoq masofada joylashgan ofislar, bo'linmalar tashkilotlar, hususan, AKM lar va boshqa tuzilmalarni birlashtirishdir",
                "Bulutli texnologiya asosida ishlash",
                "To’g’ri javob yo’q"
            ],
            "correct": 1
        },
        {
            "question": "Axborot-kutubxona muassasalarining korporativ tarmog‘i bu-?",
            "options": [
                "Axborotlarni tarmoq orqali uzatish ishlarini amalga oshirish va foydalanuvchilarga sifatli xizmatni taqdim etish",
                "Tizimli tarmoq",
                "AKMlarining foydalanuvchilarga axborot kutubxona xizmati ko‘rsatishda sifat va son jihatdan yangi xizmat turlarini joriy etishdagi birlashuvidir",
                "Korporativ tarmoq"
            ],
            "correct": 2
        },
        {
            "question": "Korporativ kataloglashtirish nima?",
            "options": [
                "Axborotlarni tarmoq orqali uzatish ishlarini amalga oshirish va foydalanuvchilarga sifatli xizmatni taqdim etish",
                "Tizimli tarmoq",
                "AKMlarining foydalanuvchilarga axborot kutubxona xizmati ko‘rsatishda sifat va son jihatdan yangi xizmat turlarini joriy etishdagi birlashuvidir",
                "Bu bir qancha tashkilotlarga (kutubxona, ARM, AKM) kelayotgan yangi hujjatlarning elektron kataloglarini shakllantirish va ulardan foydalanishni amalga oshirishdagi tashkilotlarning birga olib borayotgan ish faoliyatidir"
            ],
            "correct": 3
        },
        {
            "question": "Dunydagi eng qadimiy nashriyot qaysi qatorda berilgan?",
            "options": [
                "Cambridge University Press",
                "Oxford University Press",
                "Springer, Wiley",
                "Pro Quest"
            ],
            "correct": 0
        },
        {
            "question": "1478-yildan beri ish yuritadi. Bu qaysi nashriyotga tegishi ta’rif?",
            "options": [
                "Cambridge University Press",
                "Oxford University Press",
                "Springer, Wiley",
                "Pro Quest"
            ],
            "correct": 1
        },
        {
            "question": "Wiley qaysi davlatda tashkil qilingan?",
            "options": [
                "AQSH",
                "Afrika",
                "Rossiya",
                "Buyuk Britaniya"
            ],
            "correct": 0
        },
        {
            "question": "Ilmiy jurnallarni chop qiluvchi nashriyotni belgilang.",
            "options": [
                "Springer",
                "Cambridge University Press",
                "Nature Publishing Group",
                "Pro Quest, Oxford University Press"
            ],
            "correct": 2
        },
        {
            "question": "IOP – nima?",
            "options": [
                "AQSHning biologiya fanlariga ixtisoslashtirilgan nashriyoti",
                "Italiyaning Fizika Instituti",
                "Nature Publishing Group",
                "AQSHning Fizika instituti (Institute of Physics)"
            ],
            "correct": 3
        },
        {
            "question": "Bulutli texnologiya nima?",
            "options": [
                "Zamonaviy texnologiya bo’lib, ma’lumotlar bazasi",
                "Barcha kompyuterlarni bir tarmoqda faoliyat yuritish jarayoni",
                "Bulutli texnologiya - o’zida barcha ma’lumotlarni mujassamlashtirgan kompyuter",
                "Ma’lumotlar yig’indisini ifodalovchi so’z."
            ],
            "correct": 2
        },
        {
            "question": "Kommutator so’zining ma’nosi qanday?",
            "options": [
                "Zamonaviy qurilma degani",
                "(lot. commuto — almashtiraman, oʻzgartiraman)",
                "Inglizcha, uzataman degan ma’noni anglatadi",
                "Ma’lumotlar yig’indisini ifodalovchi so’z."
            ],
            "correct": 1
        }
    ],










    "8":[
        {
            "question": "Avtomatlashtirilgan kutubxona tizimlari o'z ichiga qaysi AIJlarini oladi?",
            "options": [
                "«Kitob beruvchi», «Ma'mur», «Kutubxona fondini butlovchi»;",
                "«Kitobxon», «Kitob beruvchi», «Kataloglashtiruvchi», «Kutubxona fondini butlovchi» va «Ma'mur»;",
                "«Kitobxon», «Ma'mur», «Kutubxona fondini butlovchi»;",
                "«Kitobxon», «Kitob beruvchi», «Kataloglashtiruvchi», «Ma'mur»."
            ],
            "correct": 1
        },
        {
            "question": "Doimiy ravishda qarzdorlar bilan kim ishlaydi?",
            "options": [
                "Kitob berish va qaytarib olish bilan shug’illanuvchi xodim;",
                "Administrator;",
                "Kataloglashtiruvchi;",
                "To’g’ri javob yo’q."
            ],
            "correct": 0
        },
        {
            "question": "«MARC» abbreviaturasi nima ma'noni anglatadi?",
            "options": [
                "Mashina o'qiy oladigan katalog;",
                "Mashina o'qiy oladigan kartochka;",
                "Kataloglashtirishning mashina o'qiydigan texnik ta’minoti;",
                "Kataloglashtirishning mashina o'qiydigan ko'rinishi."
            ],
            "correct": 0
        },
        {
            "question": "O'zbekiston Respublikasi Fanlar Akademiyasining Asosiy kutubxonasida elektron katalogni shakllantirish nechanchi yildan boshlangan?",
            "options": [
                "1995 y;",
                "1994 y;",
                "1998 y;",
                "1991 y."
            ],
            "correct": 0
        },
        {
            "question": "Avtomatlashtirilgan tizimning dasturiy ta'minoti nimalardan iborat?",
            "options": [
                "Texnikalar va ularda sifatli ishlay olish jarayonidan iborat;",
                "AKM va ARM larda barcha turdagi xizmatlarni tashkil qila olish va dasturlarning jamlanmasidan iborat;",
                "ARM va AKMlarda maxsus dasturlar va bazaviy dasturiy ta’minotlarning yig’indisidan iborat;",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Elektron kutubxona ta'rifi qaysi javobda to'g'ri keltirilgan?",
            "options": [
                "Elektron kutubxona kataloglari va axborotlarni tasnif etish ya’ni axborot-kutubxona muassasasi fondining elektron shakli;",
                "Kodlashtirishning yagona tizimi bilan bog'langan annotasiyali matnlar to'plami ya’ni axborot-kutubxona muassasasi fondining elektron shakli;",
                "Elektron kutubxona kataloglari va axborotlarni tasnif etish hamda kodlashtirishning yagona tizimi bilan bog'langan annotasiyali va to'liq matnli ma'lumotlar majmui ya’ni axborot-kutubxona muassasasi fondining elektron shakli;",
                "To’g’ri javob yo’q"
            ],
            "correct": 2
        },
        {
            "question": "Katalog nima?",
            "options": [
                "Kutubxona fondidagi barcha kitoblar ro'yxati.",
                "Kutubxona fondidagi barcha hujjatlar ro'yxati;",
                "Kartotekalarning yig’indisi;",
                "Avtomatlashtirilgan tizimda bibliografik ma'lumotlar."
            ],
            "correct": 1
        },
        {
            "question": "Bibliografik ma'lumotlar bazasi nima?",
            "options": [
                "Kutubxonada saqlanayotgan kitoblar, jurnallar va boshqa hujjatlar tasnifi;",
                "Kutubxonada saqlanayotgan kitoblar, jurnallar va boshqa hujjatlar tasnifi aks ettirgan bibliografik yozuvlardan iborat ma'lumotlar bazasi;",
                "Yozuvlardan iborat ma'lumotlar bazasi;",
                "Kutubxonada saqlanayotgan kitoblar va jurnallar tasnifi."
            ],
            "correct": 1
        },
        {
            "question": "«UZMARC» xalqaro kommunikativ formati qaysi davlatga tegishli?",
            "options": [
                "Rossiya;",
                "O’zbekiston;",
                "Kanada;",
                "Angliya."
            ],
            "correct": 1
        },
        {
            "question": "Elektron katalog nima?",
            "options": [
                "Elektron hujjatlarning to’liq matnli ma’lumotlar bazasi;",
                "Axborot-kutubxona muassasalari hujjatlari ro’yhatining elektron shakli;",
                "Axborot-kutubxona muassasalari hujjatlarining to’liq ko’rinishi.",
                "Elektron ma’lumotlar bazasi."
            ],
            "correct": 1
        },
        {
            "question": "Elektron kutubxonalar yaratish bosqichlari to’g’ri ko’rsatilgan qatorni belgilang.",
            "options": [
                "2 ta bosqich: Kataloglashtirish va Elektron kutubxona;",
                "3 ta bosqich: Kataloglashtirish, Virtual kutubxona, Elektron kutubxona;",
                "4 ta bosqich: Kompyuterlashtirilgan kutubxona, Avtomatlashtirilgan kutubxona, Elektron (raqamli) kutubxona, Virtual kutubxona;",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Elеktron kutubxona….",
            "options": [
                "(electronic library) – avtomatlashtirilgan kutubxonaning mahsuli bo`lib, u klassifikatsiyalash va axborotlarni kodlashtirishning yagona tizimiga asoslangan bo`lib, kutubxonaning elektron katalogi, annotatsiyalar va to`liq matnli ma`lumotlar bazalari majmuidan iborat bo`ladi.",
                "(electronic library) – Kutubxonada saqlanayotgan kitoblar, jurnallar va boshqa hujjatlar tasnifi;",
                "(electronic library) – Kataloglashtirish, Virtual kutubxona, Elektron kutubxona;",
                "(electronic library) – Virtual kutubxona"
            ],
            "correct": 0
        },
        {
            "question": "Elektron resurslardan foydalanishning huquqiy jihatlari.",
            "options": [
                "Elektron resursdan faqat hujjatning muallifi orqali foydalanish mumkin;",
                "Tegishli bazalardan ruxsat olish yo’li bilan foydalaniladi;",
                "Tegishli tashkilotlardan ruxsat olish yo’li bilan foydalanish mumkin;",
                "Mualliflik huquqiga e’tibor qaratib, bilimni oshirish maqsadida va muallif ismi ko’rsatilgan holda foydalanish."
            ],
            "correct": 3
        },
        {
            "question": "Elеktron katalog–elеktron kutubxonaning asosiy elеmеnti hisoblanadi.",
            "options": [
                "To’g’ri fikr;",
                "Noto’g’ri fikr;",
                "Faqat online foydalanish mumkin;",
                "B va S javoblar."
            ],
            "correct": 0
        },
        {
            "question": "Hujjatlarni kataloglashtirish bo’yicha «Parij tamoyili» qachon ma’qullangan.",
            "options": [
                "1980-yilda;",
                "1961-yilda;",
                "1987-yilda;",
                "1966-yilda."
            ],
            "correct": 1
        },
        {
            "question": "Elektron katalogni shakllantirish qaysi avtomatlshtirilgan ish joyida amalga oshiriladi?",
            "options": [
                "Administrator;",
                "Butlovchi;",
                "Kataloglashtiruvchi;",
                "Kutubxonachi va kataloglashtiruvchi."
            ],
            "correct": 2
        },
        {
            "question": "Integrallashgan axborot-kutubxona tizimi qaysi dastur yordamida yaratiladi?",
            "options": [
                "KARMAT;",
                "IRBIS;",
                "AKBT;",
                "ARMAT"
            ],
            "correct": 1
        },
        {
            "question": "Barcha mavjud resurslarining tasviri mualliflarning familiyalari yoki sarlavhalarning alfaviti bo‘yicha joylashtiriladi.",
            "options": [
                "Sistemali katalogda;",
                "Pridmetli katalogda;",
                "Elektron katalogda;",
                "Alfavitli katalogda."
            ],
            "correct": 3
        },
        {
            "question": "Korporativ kataloglashtirish texnologiyasining mavjudligi tayyor bibliografik yozuvlardan foydalanib tezda va sifatli o‘z EK bazasini shakllantirish imkoniyatini yaratadi. Qaysi dasturga tegishli ta’rif.",
            "options": [
                "ARMAT;",
                "KARMAT;",
                "IRBIS;",
                "ARMAT va KARMAT."
            ],
            "correct": 3
        },
        {
            "question": "Yaratilayotgan dasturlarning maqsadi nimaga qaratilgan?",
            "options": [
                "AKMlardagi asosiy ish jarayonlarini avtomatlashtirish, zamonaviy xizmat ko’rsatishni ta’minlash;",
                "Xodimlarni ish bilan ta’minlash;",
                "AKMlarda zamonaviy texnologiyalarni qo’llash;",
                "B va S javoblari to’g’ri."
            ],
            "correct": 0
        },
        {
            "question": "Ma’lumotlar bazasi ustida amallar bajaruvchi va uni doimo ishga tayyor holda bo’lishini ta’minlovchi mutaxassisning ish joyi to’g’ri ko’rsatilgan qatorni belgilang.",
            "options": [
                "Kataloglashtiruvchi;",
                "Kitobxon;",
                "Administrator;",
                "Butlovchi va Kutubxonachi."
            ],
            "correct": 2
        },
        {
            "question": "Turli ko’rinishdagi nashrlar, audio va video materiallar, kompyuter fayllari, kartografik materiallar, notalar va boshqa ko’plab turdagi hujjatlarni qaysi dasturda elektron katalogini shakllantirsa bo’ladi?",
            "options": [
                "ARMAT;",
                "IRBIS;",
                "KARMAT;",
                "KARMAT va IRBIS."
            ],
            "correct": 1
        },
        {
            "question": "Kutubxona fondiga kelib tushayotgan adabiyotlarga bibliografik ishlov berish va kitobxonlarning elektron formulyari yaratiladi. Qaysi avtomatlashtirilgan ish o’rnida amalga oshiriladi?",
            "options": [
                "Kataloglashtiruvchi va Kutubxonachi;",
                "Administrator;",
                "Kutubxonachi;",
                "Kataloglashtiruvchi."
            ],
            "correct": 3
        },
        {
            "question": "“Login” maydoniga “bibl”, “Parol” maydoniga “11” qiymatlarini qaysi ish joyiga tegishli?",
            "options": [
                "Kutubxonachi;",
                "Kitobxon;",
                "Butlovchi;",
                "Kataloglashtiruvchi."
            ],
            "correct": 0
        },
        {
            "question": "“Statistika“ tugmasini bosish va kerakli statistik ma’lumotlarni tanlash imkoniyati qaysi ish o’rnida mavjud?",
            "options": [
                "Administrator;",
                "Kataloglashtiruvchi;",
                "Kutubxonachi;",
                "To’g’ri javob yo’q."
            ],
            "correct": 2
        },
        {
            "question": "Kataloglashtiruvchining AIO‘ asosan uch funksiyani bajaradi. Ushbu ta’rif qaysi dasturga tegishli?",
            "options": [
                "KARMAT;",
                "IRBIS;",
                "ARMAT;",
                "AKBT."
            ],
            "correct": 2
        },
        {
            "question": "IRBIS dasturida foydalanuvchilar qanday ro’yhatga olinadi?",
            "options": [
                "Katalogizator tomonidan;",
                "Kitobxon tomonidan;",
                "Administrator tomonidan;",
                "Komplektator tomonidan."
            ],
            "correct": 1
        }
    ],



     "9": [
    {
            "question": "U faoliyatini 1960 yilda boshlagan. Resurslarining tarkibi, ilmiy tadqiqot ishlari va tezislardan iborat. Qaysi nashriyotga tegishli ta’rif?",
            "options": [
                "Pro Quest",
                "Cambridge University Press",
                "Nature Publishing Group",
                "Oxford University Press"
            ],
            "correct": 0
        },
        {
            "question": "Maktab darsliklarini nashr qiluvchi nashriyot qaysi qatorda berilgan?",
            "options": [
                "EBSCO Information Services",
                "Cambridge University Press",
                "Nature Publishing Group",
                "Oxford University Press"
            ],
            "correct": 1
        },
        {
            "question": "Dunyo bo’yicha 40 dan ortiq kompaniyalar bilan hamkorlik qiladi-?",
            "options": [
                "EBSCO Information Services",
                "Cambridge University Press",
                "Nature Publishing Group",
                "Springer"
            ],
            "correct": 3
        },
        {
            "question": "Nashriyot va agregator vazifasini bajaruvchi kompaniya?",
            "options": [
                "EBSCO Information Services",
                "Cambridge University Press",
                "Nature Publishing Group",
                "Springer"
            ],
            "correct": 0
        },
        {
            "question": "O‘zga muallif asarini atayin havolalarsiz, muallifga iqtiboslikni ko‘rsatmasdan shaxsiy asar sifatida ko‘rsatishga urinish nima?",
            "options": [
                "Resursdan noto’g’ri foydalanish",
                "Muallifga hurmatsizlik",
                "Plagiat",
                "Ko’chirib olish"
            ],
            "correct": 2
        },
        {
            "question": "Matn ko‘rinishidagi materiallar, ovozli yozuvlar va tasvirlardir. Bu nima?",
            "options": [
                "Jahon axborot resursi va kutubxona axborot resursi",
                "Axborot resursi",
                "Kutubxona axborot resursi",
                "Jahon axborot resursi"
            ],
            "correct": 1
        },
        {
            "question": "“Mualliflik huquqi va turdosh huquqlar to’g’risida” gi qonunning 35-moddasida nima deyilgan?",
            "options": [
                "Hammualliflardan har biri mustaqil ahamiyatga ega bo‘lgan o‘zi yaratgan asarning bir qismidan foydalanish huquqiga ega",
                "Muallif asardan har qanday shaklda va har qanday usul bilan foydalanish huquqiga ega",
                "Mualliflik huquqi muallifning butun hayoti davomida va uning vafotidan keyin ellik yil davomida amal qiladi",
                "Asarning asl nusxasi yoki nusxasida muallif sifatida ko‘rsatilgan shaxs muallif hisoblanadi"
            ],
            "correct": 2
        },
        {
            "question": "Fondni aylanish formulasini toping?",
            "options": [
                "Fondni “F” kitobxonlar soniga “KX” nisbati.",
                "Kitob berilishining “KB”, fondga “F” nisbati.",
                "Katnovni “KT” ish kunlari “I” mikdoriga nisbati.",
                "Kitob berilishining “KB” kitobxonlar soniga “KX” nisbati."
            ],
            "correct": 1
        },
        {
            "question": "O’rtacha kitob o‘qilishi nima?",
            "options": [
                "Kutubxonaning xar bir kitobxoniga bir yilda tugri keladigan urtacha mikdor.",
                "Bir yilda o’qilgan kitoblar.",
                "Bitta kitobxon bir yilda o’qigan kitoblar mikdori.",
                "Yil davomida o’qilgan kitoblar."
            ],
            "correct": 0
        },
        {
            "question": "O‘rtacha Qatnovga ta’rif bering?",
            "options": [
                "Qatnashlarni bitta kitobxonga bir yilda tug‘ri keladigan o’rtacha miqdori.",
                "Yil davomidagi qatnov.",
                "Bitta kitobxonni yil davomidagi kutubxonaga qatnashi",
                "Barcha javoblar to’g’ri"
            ],
            "correct": 0
        },
        {
            "question": "Kitob bilan ta’minlanganlik qanday aniqlanadi?",
            "options": [
                "Kitob fondini kitobxonlarga nisbati bo’yicha.",
                "Berilgan adabiyotlarni fondga nisbati bo’yicha.",
                "Kitobxonlar sonini fondga nisbati bo’yicha",
                "Barcha javoblar to’g’ri."
            ],
            "correct": 0
        },
        {
            "question": "Ish yuklamasi ko'rsatkichlari qanday xisoblanadi?",
            "options": [
                "Ish hajmi, kutubxona xodimlari soniga bo‘linadi.",
                "Kutubxona xodimlari soni ish hajmiga bo‘linadi.",
                "Kutubxona fondi kutubxona xodimlari soniga bo‘linadi.",
                "Kitob berilishi kutubxona xodimlariga bo‘linadi."
            ],
            "correct": 0
        },
        {
            "question": "Avtomatlashtirilgan kutubxona ta'rifi qaysi javobda to'g'ri keltirilgan?",
            "options": [
                "Avtomatlashtirilgan kutubxona – o’zaro bag’langan kompyuterlashgan avtomatik tizim bo’lib, uning funksiyasi ayniqsa kutubxona axborot xizmati asosan avtomatlashtirish (kompyuterlar, serverlar, tashkiliy texnika vositalari, dasturiy komplekslar) va telekommunikasiya vositalari yordamida amalga oshiriladi;",
                "Avtomatlashtirilgan kutubxona – bu shunday kutubxonaki, uning funksiyasi ya'ni kutubxona axborot xizmati kompyuterlar va printerlar yordamida amalga oshiriladi;",
                "Avtomatlashtirilgan kutubxona – bu shunday kutubxonaki, uning funksiyasi ya'ni kutubxona axborot xizmati kompyuterlar yordamida amalga oshiriladi;",
                "A va B javoblar."
            ],
            "correct": 0
        },
        {
            "question": "«MARC1» loyihasi qaysi mamlakatda ishlab chiqilgan?",
            "options": [
                "AQShda",
                "Angliyada",
                "Germaniyada",
                "Kanadada"
            ],
            "correct": 0
        }



       
    ],




    "10": [
    

{
            "question": "Nashriyot – bu?",
            "options": [
                "O‘zi noshirlik qilmagan holda elektron resurslarni yig‘uvchi kompaniyalar hisoblanib, iste’molchilarni ularning so‘rovlari, obunalari asosida resurslarga bo‘lgan ehtiyojlarini aniqlab, kerakli axborotlar bilan ta’minlash maqsadida marketing faoliyatini olib boradi.",
                "O‘zga muallif asarini atayin havolalarsiz, muallifga iqtiboslikni ko‘rsatmasdan shaxsiy asar sifatida ko‘rsatishga urinish.",
                "Tashkilot (davlat, jamoat, kooperativ yoki xususiy) adabiyot, san’at, musiqa yoki fan sohasida faoliyat yuritib mahsulotlar yaratishi, ko‘paytirishi, tarqatishi mumkin bo‘lgan media-kompaniya.",
                "Tasvirlash, saqlashning alohida qoidalar asosida tashkil etilgan amaliy dasturlar asosida tuzilgan ma’lumotlar yig‘indisidir."
            ],
            "correct": 2
        },
        {
            "question": "Jahon axborot resurslari nima?",
            "options": [
                "Dunyo bo’yicha barcha ma’lumotlarning yig’indisi",
                "Jamiyat tomonidan tan olingan nashriyotlarning axborot resurslari",
                "Ma’lumotlar jamlanmasi",
                "Jahonning Ma’lumotlar massivi"
            ],
            "correct": 1
        },
        {
            "question": "Jahonning yetakchi nashriyotlari ko’rsatilgan qatorni ko’rsating.",
            "options": [
                "Cambridge University Press, Oxford University Press",
                "Wiley, EBSCO Information Services",
                "Bio One, Scopus, Web of Science",
                "Barchasi to’g’ri keltirilgan"
            ],
            "correct": 3
        },
        {
            "question": "EBSCO Information Services bu -?",
            "options": [
                "Konsorsium",
                "Nashriyot",
                "Kutubxona markazi",
                "To’g’ri javob yo’q"
            ],
            "correct": 1
        },
        {
            "question": "Kutubxona axborot resurslari bu?",
            "options": [
                "Kutubxonada saqlanayotgan hujjatlar",
                "Kutubxonaga oid hujjatlar",
                "Saqlash va foydalanishni ta’minlash uchun rekvizitlarga ega bo‘lgan axborot",
                "B va S javoblar to’g’ri"
            ],
            "correct": 2
        },
        {
            "question": "Ilmiy-ta’limiy resurslar deb qanday resurslarga aytiladi?",
            "options": [
                "Litsenziyalangan resurslarga aytiladi",
                "Taqrizdan o’tgan resurslarga aytiladi",
                "Jahon bo’yicha qo’llaniluvchi resurslarga aytiladi",
                "A va B javoblar to’g’ri"
            ],
            "correct": 3
        },
        {
            "question": "Ilmiy-ta’limiy resurslar to’g’ri ko’rsatilgan qatorni toping.",
            "options": [
                "Maqolalar, ilmiy nashrlar",
                "Faqat darsliklar",
                "Darsliklar, o’quv qo’llanmalar, monografiyalar, maqolalar, ilmiy tadqiqot ishlari",
                "Ilmiy tadqiqot ishlari"
            ],
            "correct": 2
        },
        {
            "question": "Erkin foydalanish bu-?",
            "options": [
                "Barcha ma’lumotlardan erkin foydalana olish jarayoni",
                "Barcha ma’lumotlarni yuklab olish, muallifning ruxsatisiz foydalanuvchilarga tarqatish",
                "Internet orqali kitobxonlarning bepul foydalanishi, o‘qish, yuklab olish, nusxa ko‘chirish, tarqatish va chop etish, qidirish, indekslash, qonun doirasida ma’lumot sifatida uzatish",
                "To’g’ri javob yo’q"
            ],
            "correct": 2
        },
        {
            "question": "Ma’lumot bazalari (data base) –?",
            "options": [
                "Resurslarni yetkazib beruvchi tashkilotlarning faoliyati",
                "Elektron resurslarning yig’indisi",
                "Ma’lumotlarning barchasi joylashtirilgan massiv",
                "Tasvirlash, saqlashning alohida qoidalar asosida tashkil etilgan amaliy dasturlar asosida tuzilgan ma’lumotlar yig‘indisidir."
            ],
            "correct": 3
        },
        {
            "question": "Plagiat nima?",
            "options": [
                "Ma’lumotlarni qayta ishlash jarayoni",
                "Resurslarni chop qiluvchi media kompaniya",
                "O‘zga muallif asarini atayin havolalarsiz, muallifga iqtiboslikni ko‘rsatmasdan shaxsiy asar sifatida ko‘rsatishga urinish",
                "A va S javoblari to’g’ri berilgan"
            ],
            "correct": 2
        },
        {
            "question": "Tashkilot (davlat, jamoat, kooperativ yoki xususiy) adabiyot, san’at, musiqa yoki fan sohasida faoliyat yuritib mahsulotlar yaratishi, ko‘paytirishi, tarqatishi mumkin bo‘lgan media-kompaniya- bu?",
            "options": [
                "Agregatorlar",
                "Hususiy tashkilotlar",
                "Nashriyotlar",
                "Mas’uliyati cheklangan jamiyat, korxonalar"
            ],
            "correct": 2
        }

       
    ]
}

@dp.message(Command("start"))
async def start(message: types.Message):
    """Start komandasi uchun handler"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2")],
            [KeyboardButton(text="3"), KeyboardButton(text="4")],
            [KeyboardButton(text="5"), KeyboardButton(text="6")],
            [KeyboardButton(text="7"), KeyboardButton(text="8")],
            [KeyboardButton(text="9"), KeyboardButton(text="10")],
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Test tanlang (1-10 raqamlaridan birini bosing):",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text in quizzes.keys())
async def start_test(message: types.Message):
    """Testni boshlash"""
    test_number = message.text
    user_id = message.from_user.id

    await send_all_questions(user_id, test_number)

async def send_all_questions(user_id, test_number):
    """Foydalanuvchiga barcha savollarni ketma-ket yuborish"""
    if test_number not in quizzes:
        await bot.send_message(user_id, "Xatolik: Test topilmadi.")
        return

    questions = quizzes[test_number]

    for question_index, question in enumerate(questions):
        options = question.get("options", [])
        correct_index = question.get("correct")

        if not options or not isinstance(correct_index, int) or correct_index >= len(options):
            await bot.send_message(user_id, f"{question_index + 1}-savolda xatolik: noto‘g‘ri format.")
            continue

        correct_answer = options[correct_index]
        random.shuffle(options)
        new_correct_index = options.index(correct_answer)

        try:
            await bot.send_poll(
                chat_id=user_id,
                question=f"{test_number}-test: {question['question']}",
                options=options,
                type="quiz",
                correct_option_id=new_correct_index,
                is_anonymous=False,
                explanation=f"To'g'ri javob: {correct_answer}",
                open_period=30
            )
            await asyncio.sleep(5)
        except Exception as e:
            print(f"{question_index + 1}-savolni yuborishda xato: {e}")
            await bot.send_message(user_id, f"{question_index + 1}-savolni yuborishda xatolik yuz berdi.")

async def main():
    """Dasturni ishga tushirish"""
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
