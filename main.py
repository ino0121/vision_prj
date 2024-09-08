import streamlit as st  
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

# 이미지를 변환하는 함수 선언
def convert_to_grayscale(input_path, output_path=None):
    with Image.open(input_path) as img:
        # 흑백으로 변환
        grayscale_img = img.convert('L')

        # 이미지 저장
        if output_path:
            grayscale_img.save(output_path)

        # 변환된 이미지를 리턴
        return grayscale_img


# 이미지를 보여줄 함수 선언
def display_img(image_path):
    plt.figure()
    plt.imshow(image_path, cmap="gray")
    plt.show()



# 페이지 세팅
st.set_page_config(
    page_title="Image Converter(to grayscale)",
    initial_sidebar_state = 'auto',
)


file = st.file_uploader("Upload a Photo", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    grayscale_img = convert_to_grayscale(file)
    st.write("Converted image")
    st.image(grayscale_img)
    st.write("Original image")
    st.image(file)
