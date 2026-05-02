# خطوات رفع الموقع على GitHub Pages (مجاني 100%)

## الخطوات:

### 1. إنشاء حساب GitHub
- اذهب إلى: https://github.com
- اضغط "Sign up" وأنشئ حساباً مجانياً

### 2. إنشاء Repository جديد
- اضغط "+" ثم "New repository"
- اسم الـ Repository: `HubSave-pro` (مهم!)
- اضغط "Public"
- اضغط "Create repository"

### 3. رفع ملفات الموقع
افتح PowerShell في مجلد الموقع وشغّل:

```powershell
cd "C:\Users\ابو اسد\OneDrive\Desktop\HubSave-website"
git init
git add .
git commit -m "Initial website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/HubSave-pro.git
git push -u origin main
```
(استبدل YOUR_USERNAME باسم حسابك على GitHub)

### 4. تفعيل GitHub Pages
- في الـ Repository، اذهب إلى Settings
- اضغط "Pages" من القائمة الجانبية
- في "Branch" اختر "main" ثم اضغط Save
- انتظر دقيقة وسيصبح الموقع متاحاً على:
  https://YOUR_USERNAME.github.io/HubSave-pro/

### 5. تحديث رابط سياسة الخصوصية في التطبيق
بعد معرفة رابطك، غيّر هذا السطر في SettingsActivity.kt:
```kotlin
val url = "https://YOUR_USERNAME.github.io/HubSave-pro/privacy.html"
```
إلى الرابط الحقيقي الخاص بك.



