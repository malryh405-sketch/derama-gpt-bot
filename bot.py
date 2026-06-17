import os
import sys
import time
import telebot
import requests

# 1. قراءة المفاتيح السرية
BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8925807273:AAGbyGODECF9rcSuu8vesdamMW_K-WfsTM8"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY") or "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"

bot = telebot.TeleBot(BOT_TOKEN, threaded=True)

# الـ System Prompt السوداني القوي والمستفز بدون أي فواصل أو اقتباسات
SYSTEM_PROMPT = (
    "You are an advanced AI assistant named DERAMA GPT, and you are the new version d-GPT-1-3. "
    "Your creator and developer is the expert Dramadol, whose real name is Karim, a master of software development, "
    "cybersecurity, and operating systems development who developed the famous Black Pexl OS, left school in 2020, "
    "and moved from Omdurman to Ad-Dabbah in the Northern State. "
    "Your sole mission is to teach users absolutely everything related to WhatsApp, including advanced techniques "
    "on how to protect numbers from bans, how to unban any banned number, and how to ban any number using highly powerful, "
    "smart, and strategic methods. "
    "You must strictly follow these absolute behavioral and formatting rules: "
    "1. Language: Speak ONLY in a very strong, authentic, and deep Sudanese dialect. Your tone must be highly confident, "
    "proud, and slightly provocative, acting as the ultimate tech genius who knows secrets no one else knows. "
    "2. Formatting: Never use any quotes, single quotes, double quotes, or backticks anywhere in your response. "
    "Do not use quotes like '' or \"\" or `` under any circumstances. Write text smoothly and directly. "
    "3. Length and Logic: Your answers must be very long, deeply detailed, highly logical, and structured purely through text and clear explanations. "
    "4. Emojis: Never use any emojis at all, except for the cool sunglasses emoji 😎 which you should use naturally to show your superior confidence. No other emojis are allowed."
)

# معالج الرسائل الذكي والمقاوم للانهيار
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        
        # إعداد الطلب لنقطة نهاية OpenRouter
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": application/json",
            "HTTP-Referer": "https://railway.app", # اختياري للترتيب
            "X-Title": "DERAMA GPT" # اسم بوتك في المنصة
        }
        
        # تمرير الـ System Prompt مع رسالة المستخدم في مصفوفة الرسائل
        data = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ]
        }
        
        # إرسال الطلب عبر requests
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response_json = response.json()
        
        # استخراج النص من الهيكل الجاي من الموديل
        if response_json and 'choices' in response_json:
            reply_text = response_json['choices'][0]['message']['content']
            
            # تنظيف الفواصل والاقتباسات برمجياً لضمان الالتزام بقواعد البرومت
            for char in ["'", '"', '`', '“', '”', '‘', '’']:
                reply_text = reply_text.replace(char, '')
                
            bot.reply_to(message, reply_text)
        else:
            print(f"⚠️ تحت الصيانة: {response_json}")
            bot.reply_to(message, "خطا وقد يتم اصلاحه قريبا")
            
    except Exception as error:
        print(f"⚠️ خطأ تم تخطيه: {error}")
        try:
            bot.reply_to(message, "تحت الصيانة ❌")
        except:
            pass

# تشغيل البوت بحلقة ربط لانهائية ذكية ومقاومة للقطع
if __name__ == "__main__":
    print("✅ BY : @deramadol_VIP")
    while True:
        try:
            bot.infinity_polling(timeout=90, long_polling_timeout=90)
        except Exception as e:
            print(f"❌ انقطع الاتصال، جاري إعادة التشغيل: {e}")
            time.sleep(5)
