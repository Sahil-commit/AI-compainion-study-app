import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="📱")

st.title("📱 QR Code Generator")

data = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):
    if data:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer, caption="Generated QR Code")

        st.download_button(
            label="⬇ Download PNG",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some text or a URL.")
        import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)

img.save("qrcode.png")

print("QR Code saved as qrcode.png")
