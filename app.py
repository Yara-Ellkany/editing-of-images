import streamlit as st
from PIL import Image

st.title("🎨 دمج الصور للأطفال")

st.write("ارفع صورتين وسنقوم بدمجهم معًا!")

# رفع الصور
img1_file = st.file_uploader("اختر الصورة الأولى", type=["png", "jpg"])
img2_file = st.file_uploader("اختر الصورة الثانية", type=["png", "jpg"])

if img1_file and img2_file:
    img1 = Image.open(img1_file)
    img2 = Image.open(img2_file)

    # تغيير الحجم ليكونوا نفس الحجم
    img2 = img2.resize(img1.size)

    st.subheader("الصور الأصلية")
    col1, col2 = st.columns(2)
    col1.image(img1, caption="الصورة الأولى")
    col2.image(img2, caption="الصورة الثانية")

    # اختيار نسبة الدمج
    alpha = st.slider("درجة الدمج", 0.0, 1.0, 0.5)

    # دمج الصور
    blended = Image.blend(img1, img2, alpha)

    st.subheader("✨ الصورة الناتجة")
    st.image(blended)

    # تحميل الصورة
    blended.save("merged.png")
    with open("merged.png", "rb") as file:
        st.download_button("تحميل الصورة", file, file_name="merged.png")
