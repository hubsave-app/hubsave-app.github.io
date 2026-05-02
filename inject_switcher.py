import os
import glob

for filepath in glob.glob("*.html"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<nav>' in content and 'en/index.html' not in content:
        switcher = '<a href="en/index.html" style="margin-left:auto; margin-right:1rem; border:1px solid #fe2c55; padding:0.3rem 0.8rem; border-radius:8px; color:#fff; text-decoration:none;">English</a>'
        content = content.replace('<div class="nav-links">', switcher + '\n    <div class="nav-links">')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Arabic language switcher injection completed.")
