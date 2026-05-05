def rect(x, y, w, h, rx=0, fill=""):
    if rx == 0:
        d = f"M {x},{y} H {x+w} V {y+h} H {x} Z"
    else:
        d = f"M {x+rx},{y} H {x+w-rx} Q {x+w},{y} {x+w},{y+rx} V {y+h-rx} Q {x+w},{y+h} {x+w-rx},{y+h} H {x+rx} Q {x},{y+h} {x},{y+h-rx} V {y+rx} Q {x},{y} {x+rx},{y} Z"
    return f'    <path android:fillColor="{fill}" android:pathData="{d}" />\n'

def circle(cx, cy, r, fill="", opacity="1.0"):
    d = f"M {cx},{cy-r} A {r},{r} 0 1,1 {cx},{cy+r} A {r},{r} 0 1,1 {cx},{cy-r} Z"
    op_attr = f' android:fillAlpha="{opacity}"' if opacity != "1.0" else ""
    return f'    <path android:fillColor="{fill}"{op_attr} android:pathData="{d}" />\n'

def path(d, fill="", stroke="", stroke_width="0"):
    attrs = []
    if fill: attrs.append(f'android:fillColor="{fill}"')
    if stroke: 
        attrs.append(f'android:strokeColor="{stroke}"')
        attrs.append(f'android:strokeWidth="{stroke_width}"')
    return f'    <path {" ".join(attrs)} android:pathData="{d}" />\n'

def build_vd(content):
    return f"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="200dp"
    android:height="400dp"
    android:viewportWidth="400"
    android:viewportHeight="800">
{content}
</vector>"""

vd_copy = build_vd(
    rect(0, 0, 400, 800, 20, "#111111") +
    rect(0, 0, 400, 800, 20, "#222222") +
    circle(350, 400, 22, "#333333", "0.8") +
    circle(350, 470, 22, "#333333", "0.8") +
    circle(350, 540, 22, "#333333", "0.8") +
    circle(350, 610, 22, "#25f4ee", "0.9") +
    path("M 342,605 H 354 V 609 H 346 V 617 H 342 Z M 356,615 H 344 V 611 H 352 V 603 H 356 Z", fill="#ffffff") +
    rect(0, 500, 400, 300, 20, "#1e1e1e") +
    rect(175, 515, 50, 5, 2.5, "#444444") +
    circle(60, 610, 28, "#333333") + circle(153, 610, 28, "#333333") + circle(246, 610, 28, "#333333") + circle(340, 610, 28, "#333333") +
    circle(60, 710, 25, "#333333") +
    circle(153, 710, 25, "#25f4ee") +
    path("M 145,705 A 5,5 0 0,0 145,715 H 149 V 713 H 145 A 3,3 0 0,1 145,707 H 149 V 705 Z M 157,705 H 153 V 707 H 157 A 3,3 0 0,1 157,713 H 153 V 715 H 157 A 5,5 0 0,0 157,705 Z M 148,709 H 158 V 711 H 148 Z", fill="#ffffff") +
    circle(246, 710, 25, "#333333") + circle(340, 710, 25, "#333333")
)

vd_paste = build_vd(
    rect(0, 0, 400, 800, 20, "#0a0a0a") +
    rect(0, 0, 400, 220, 20, "#25f4ee") +
    circle(50, 90, 12, "#ffffff", "0.9") +
    rect(20, 160, 360, 240, 20, "#111111") +
    rect(40, 210, 320, 80, 12, "#1a1a1a") +
    path("M 60,235 H 78 V 261 H 60 Z", stroke="#888888", stroke_width="2") +
    rect(64, 230, 10, 6, 1, "#888888") +
    rect(40, 320, 320, 60, 15, "#fe2c55")
)

vd_download = build_vd(
    rect(0, 0, 400, 800, 20, "#0a0a0a") +
    rect(0, 0, 400, 220, 20, "#fe2c55") +
    rect(20, 140, 360, 80, 20, "#111111") +
    rect(40, 155, 320, 50, 10, "#1a1a1a") +
    rect(20, 240, 360, 360, 20, "#111111") +
    rect(240, 270, 100, 120, 12, "#333333") +
    circle(290, 330, 18, "#ffffff", "0.8") +
    path("M 285,320 V 340 L 300,330 Z", fill="#333333") +
    rect(40, 420, 320, 65, 15, "#fe2c55") +
    rect(40, 505, 320, 65, 15, "#25f4ee")
)

with open('app/src/main/res/drawable/illus_step1_copy.xml', 'w') as f: f.write(vd_copy)
with open('app/src/main/res/drawable/illus_step2_paste.xml', 'w') as f: f.write(vd_paste)
with open('app/src/main/res/drawable/illus_step3_download.xml', 'w') as f: f.write(vd_download)
print("VectorDrawables created.")
