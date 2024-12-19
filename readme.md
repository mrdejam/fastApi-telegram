# FastAPI Telegram Relay 🚀

![Author](https://img.shields.io/badge/Author-MrDejam-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-green)

## توضیحات پروژه 📝

این پروژه یک API واسط برای ارسال پیام به کانال تلگرام است. با استفاده از این API، می‌توانید:
- پیام‌های متنی را به کانال تلگرام ارسال کنید
- تصاویر را همراه با توضیحات به کانال ارسال کنید
- از طریق API Key، امنیت درخواست‌ها را تضمین کنید

هدف اصلی این پروژه، ایجاد یک واسط ساده و امن برای اتوماسیون ارسال پیام به کانال تلگرام است.

## ویژگی‌ها ✨

- 🔒 احراز هویت با API Key
- 📝 ارسال پیام متنی
- 🖼️ ارسال تصویر + کپشن
- 🚀 پیاده‌سازی با FastAPI (سریع و مدرن)
- 📚 مستندات Swagger/OpenAPI
- 🔍 لاگینگ و مدیریت خطا
- ⚡️ غیرهمزمان (Async)

## پیش‌نیازها 📋

- Python 3.12+
- pip
- یک بات تلگرام (از @BotFather)
- یک کانال تلگرام

## نصب و راه‌اندازی 🛠️

1. کلون پروژه:
```bash
git clone https://github.com/mrdejam/fastapi-telegram.git
cd fastapi-telegram
```

2. ساخت محیط مجازی و نصب وابستگی‌ها:
```bash
python -m venv venv
source venv/bin/activate  # در لینوکس
# یا
venv\Scripts\activate  # در ویندوز

pip install -r requirements.txt
```

3. ساخت فایل `.env`:
```bash
cp .env.example .env
```

4. ویرایش فایل `.env` و تنظیم مقادیر:
```env
API_KEY=your_api_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=your_channel_id_here
ENVIRONMENT=development
DEBUG=True
```

5. اجرای برنامه:
```bash
uvicorn app.main:app --reload
```

## راه‌اندازی روی سرور 🌐

برای راه‌اندازی روی سرور Ubuntu:

1. نصب نیازمندی‌ها:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx -y
```

2. نصب و تنظیم Gunicorn و Nginx (به فایل deployment.md مراجعه کنید)

3. تنظیم SSL با Certbot (توصیه می‌شود)

## نحوه استفاده 📱

### ارسال پیام متنی:
```bash
curl -X POST "http://your-domain/api/v1/messages/send" \
     -H "X-API-Key: your_api_key" \
     -H "Content-Type: application/json" \
     -d '{"message": "تست پیام"}'
```

### ارسال تصویر با کپشن:
```bash
curl -X POST "http://your-domain/api/v1/messages/send" \
     -H "X-API-Key: your_api_key" \
     -H "Content-Type: application/json" \
     -d '{"message": "توضیحات تصویر", "photo_url": "https://example.com/image.jpg"}'
```

## توسعه و مشارکت 🤝

1. پروژه را fork کنید
2. یک branch جدید بسازید (`git checkout -b feature/awesome`)
3. تغییرات خود را commit کنید (`git commit -m 'Add something awesome'`)
4. به branch اصلی push کنید (`git push origin feature/awesome`)
5. یک Pull Request ایجاد کنید

## لایسنس 📄

این پروژه تحت لایسنس MIT منتشر شده است. برای اطلاعات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

---
ساخته شده با ❤️ توسط [MrDejam](https://github.com/mrdejam)# fastApi-telegram
