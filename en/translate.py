import os
import glob

replacements = {
    'lang="ar" dir="rtl"': 'lang="en" dir="ltr"',
    'تحميل تيك توك بدون علامة مائية': 'Download Videos Without Watermark',
    'حمّل فيديوهات تيك توك بدون علامة مائية': 'Download Videos Without Watermark',
    'أفضل تطبيق لتحميل فيديوهات تيك توك بجودة عالية بدون علامة مائية. حمّل الآن مجاناً لأجهزة Android.': 'Best app to download social media videos in high quality without watermark. Download now for free on Android.',
    'المميزات': 'Features',
    'المدونة': 'Blog',
    'اتصل بنا': 'Contact Us',
    'تحميل مجاني': 'Free Download',
    'تحميل الآن': 'Download Now',
    'الأسرع والأخف على Android': 'Fastest & Lightest on Android',
    'الإصدار 1.0 — آخر تحديث: مايو 2025': 'Version 1.0 — Last Updated: May 2025',
    'حمّل فيديوهات': 'Download Videos',
    'تيك توك': 'Videos',
    'بدون علامة مائية': 'Without Watermark',
    'أسرع وأسهل طريقة لتحميل فيديوهات وصوتيات تيك توك بجودة عالية مجاناً لأجهزة Android': 'The fastest and easiest way to download social media videos and audio in high quality for free on Android.',
    'تحميل مجاني — APK مباشر': 'Free Download — Direct APK',
    'اكتشف المميزات': 'Discover Features',
    'الصق رابط تيك توك هنا...': 'Paste Video Link here...',
    'فحص الرابط': 'Check Link',
    'حمّل فيديوهات': 'Download Videos',
    'مواقع التواصل': 'Social Media',
    'فيديو': 'Video',
    'الفيديوهات': 'Videos',
    'الرابط': 'Link',
    'لصق': 'Paste',
    'نسخ': 'Copy',
    'بدون علامة': 'No Watermark',
    'الرئيسية': 'Home',
    'المفضلة': 'Favorites',
    'السجل': 'History',
    'مجاني بالكامل': '100% Free',
    'جودة عالية': 'High Quality',
    'متوافق مع الأجهزة': 'Device Compatible',
    'كل ما تحتاجه في تطبيق واحد': 'Everything You Need in One App',
    'تحميل فوري بنقرة واحدة': 'Instant 1-Click Download',
    'استخراج الصوت MP3': 'Extract MP3 Audio',
    'مكتبة ذكية': 'Smart Library',
    'وضع داكن True Black': 'True Black Dark Mode',
    'عربي وإنجليزي': 'Arabic & English',
    'كيف يعمل': 'How It Works',
    'ثلاث خطوات فقط': 'Just 3 Steps',
    'انسخ الرابط': 'Copy Link',
    'افتح HubSave': 'Open HubSave',
    'اختر وحمّل': 'Select & Download',
    'أحدث المقالات التقنية': 'Latest Tech Articles',
    'تصفح كل المقالات': 'Browse All Articles',
    'جاهز للبدء؟': 'Ready to Start?',
    'شروط الاستخدام': 'Terms of Service',
    'سياسة الخصوصية': 'Privacy Policy',
    'جميع الحقوق محفوظة': 'All Rights Reserved',
    'سياسة الخصوصية والاستخدام': 'Privacy & Terms of Use',
    'أداة للاستخدام الشخصي': 'Personal Utility Tool',
    'حقوق الطبع والنشر': 'Copyrights',
    'إخلاء المسؤولية': 'Disclaimer',
    # Adjusting font
    'Tajawal': 'Inter'
}

for filepath in glob.glob("*.html"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for ar, en in replacements.items():
        content = content.replace(ar, en)
        
    # Add Language Switcher
    if '<nav>' in content:
        # We need to insert a language switcher
        switcher = '<a href="../index.html" style="margin-left:auto; margin-right:1rem; border:1px solid #fe2c55; padding:0.3rem 0.8rem; border-radius:8px; color:#fff; text-decoration:none;">العربية</a>'
        content = content.replace('<div class="nav-links">', switcher + '\n    <div class="nav-links">')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Translation completed.")
