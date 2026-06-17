import os
import sys
import time
import telebot
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# 1. قراءة المفاتيح السرية من التطبيق
BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8925807273:AAGbyGODECF9rcSuu8vesdamMW_K-WfsTM8"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or "AQ.Ab8RN6L6KP0W40dQz0slF5AnecuCyR-tyGHU5vUQci-1UGBlMQ"

# تهيئة البوت بنظام الخيوط المتعددة عشان يستحمل ضغط كذا مستخدم سوا
bot = telebot.TeleBot(BOT_TOKEN, threaded=True)

# تهيئة جيميناي بالمكتبة المتوافقة مع بايثون 3.9
genai.configure(api_key=GEMINI_API_KEY)

# الـ System Prompt السوداني المستفز كامل بدون أي فواصل أو اقتباسات
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

# كسر فلاتر الأمان تماماً لضمان توليد طرق الحظر والفك بدون حرج من جوجل
LOW_SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config={
        "temperature": 0.85,
        "max_output_tokens": 1500
    },
    safety_settings=LOW_SAFETY_SETTINGS,
    system_instruction=SYSTEM_PROMPT
)

# معالج الرسائل الذكي والمحمي تماماً من الانهيار والتهنيج
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        
        if response and response.text:
            reply_text = response.text
            # تنظيف الفواصل والاقتباسات برمجياً قبل الإرسال للمستخدم
            for char in ["'", '"', '`', '“', '”', '‘', '’']:
                reply_text = reply_text.replace(char, '')
            bot.reply_to(message, reply_text)
        else:
            bot.reply_to(message, "BY || @deramadol_VIP")
    except Exception as error:
        print(f"⚠️ خطأ معزول تم تخطيه: {error}")
        try:
            bot.reply_to(message, "تحت الصيانة ⚠️")
        except:
            pass

# تشغيل البوت بنظام حلقة الربط اللانهائية المقاومة لقطع الشبكة
if __name__ == "__main__":
    print("✅ d-GPT-1-3 Active and protected against crashes on Python 3.9... 😎")
    while True:
        try:
            # حذفنا non_stop=True لأن الدالة بتفعلها تلقائياً من جوة المكتبة
            bot.infinity_polling(timeout=90, long_polling_timeout=90)
        except Exception as e:
            print(f"❌ انقطع الاتصال، جاري إعادة التشغيل تلقائياً: {e}")
            time.sleep(5)
