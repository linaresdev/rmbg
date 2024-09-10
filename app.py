import os
from PIL import Image
from rembg import remove
import streamlit as st

def save_upload_file(upload_file):
    upload_dir = "uploads"
    
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, upload_file.name)

    with open(file_path, "wb") as f:
        f.write(upload_file.getbuffer())
    
    return file_path

def run_background_remover(input_img_file):
    input_img_path = save_upload_file(input_img_file)
    output_img_path = input_img_path.replace('.', '_rmbg.').replace('jpg','png').replace('jpeg', 'png')
    try:
        image = Image.open(input_img_file)
        output = remove(image)
        output.save(output_img_path, "PNG")

        col1, col2 = st.columns(2)
    
        with col1:
            st.header("Antes")
            st.image(input_img_path, caption="Imagen Original")

            with open(input_img_path, "rb") as img_file:
                st.download_button(
                    label="Descargar Imagen Original",
                    data=img_file,
                    file_name=os.path.basename(input_img_path),
                    mime="image/jpeg"
                )

        with col2:
            st.header("Despues")
            st.image(output_img_path, caption="Imagen confondo removido")

            with open(output_img_path, "rb") as img_file:
                st.download_button(
                    label="Descargar Imagen Procesada",
                    data=img_file,
                    file_name=os.path.basename(output_img_path),
                    mime="image/png"
                )
        st.success("Fondo removido exitosamente!")
    except Exception as e:
        st.error(f"Ocurrio un error: {e}")

def main():
    st.title("Removedor de fondos")
    upload_file = st.file_uploader("Elige un archivo de imagem", type=["jpg", "jpeg", "png"])
    if upload_file is not None:
        run_background_remover(upload_file)

if __name__ == "__main__":
    main()





