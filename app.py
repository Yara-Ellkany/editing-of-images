import streamlit as st
from PIL import Image
from rembg import remove
import io
 
st.title(" ضع نفسك في أي مكان!")
 
person_file = st.file_uploader("اختر صورة الشخص", type=["png", "jpg"])
bg_file = st.file_uploader("اختر صورة المكان (تركيا، باريس...)", type=["png", "jpg"])
 
if person_file and bg_file:
    person_img = Image.open(person_file).convert("RGBA")
    bg_img = Image.open(bg_file).convert("RGBA")
 
    st.subheader("الصور الأصلية")
    col1, col2 = st.columns(2)
    col1.image(person_img, caption="الشخص")
    col2.image(bg_img, caption="المكان")
 
    with st.spinner(" جاري إزالة الخلفية..."):
        person_no_bg = remove(person_img)
 
    st.subheader(" ضبط الحجم والموضع")
    scale = st.slider("حجم الشخص", 10, 100, 50)
    pos_x = st.slider("الموضع أفقي", 0, 100, 50)
    pos_y = st.slider("الموضع عمودي", 0, 100, 70)
 
    # تغيير حجم الشخص بناءً على الخلفية
    bg_w, bg_h = bg_img.size
    new_h = int(bg_h * scale / 100)
    ratio = new_h / person_no_bg.size[1]
    new_w = int(person_no_bg.size[0] * ratio)
    person_resized = person_no_bg.resize((new_w, new_h), Image.LANCZOS)
 
    # حساب الموضع
    x = int((bg_w - new_w) * pos_x / 100)
    y = int((bg_h - new_h) * pos_y / 100)
 
    # دمج الصورتين
    result = bg_img.copy()
    result.paste(person_resized, (x, y), person_resized)
 
    st.subheader("الصورة الناتجة")
    st.image(result)
 
    # تحميل الصورة
    buf = io.BytesIO()
    result.convert("RGB").save(buf, format="PNG")
    buf.seek(0)
    st.download_button("⬇️ تحميل الصورة", buf, file_name="result.png", mime="image/png")
