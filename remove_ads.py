import os
import re

directories = ['.', 'en']
target_script = r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-6047567977712893" crossorigin="anonymous"></script>'

# regex for the div block containing adsbygoogle
# it looks like: <div class="ad-space">...<ins class="adsbygoogle"...>...</ins>...</div>
# or <div class="ad">...</div>
# We can find <div class="ad-space" ... </div> or <div class="ad" ... </div> 
# that contains adsbygoogle.
ad_div_regex = r'<div class="(ad|ad-space)">.*?adsbygoogle.*?</div>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(target_script, '', content)
    # the div might be multiline, so re.DOTALL
    new_content = re.sub(ad_div_regex, '', new_content, flags=re.DOTALL)
    
    if new_content != content:
        # Also clean up empty lines left behind
        new_content = re.sub(r'\n\s*\n', '\n\n', new_content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed ads from {filepath}")

for directory in directories:
    if not os.path.exists(directory):
        continue
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            process_file(filepath)

print("Done processing HTML files.")
