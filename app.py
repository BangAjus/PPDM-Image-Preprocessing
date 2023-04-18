import streamlit as st
from image_processing import *

st.title("Image Processing dengan Python")


img_number = st.number_input('Cari angka dari file gambar: ',
                             min_value=391,
                             max_value=400,
                             value=391,
                             step=1,)

img_emotion = st.radio("Pilih emosi yang akan digunakan untuk menampilkan matriks",
                       ('Senang', 'Netral', 'Sedih'))

if img_emotion == 'Senang':

    happy = "C:/Tugas/PPDM/Tugas 2/Pictures/Happy"
    img_dir = happy + '/' + f'happy-0{str(img_number)}.jpg'
    st.table(pd.DataFrame(make_matrix(img_dir)))

if img_emotion == 'Netral':

    neutral = "C:/Tugas/PPDM/Tugas 2/Pictures/Neutral"
    img_dir = neutral + '/' + f'neutral-0{str(img_number)}.jpg'
    st.table(pd.DataFrame(make_matrix(img_dir)))

if img_emotion == 'Sedih':

    sad = "C:/Tugas/PPDM/Tugas 2/Pictures/Sad"
    img_dir = sad + '/' + f'sad-0{str(img_number)}.jpg'
    st.table(pd.DataFrame(make_matrix(img_dir)))



# histogram untuk seluruh foto
hist_number = st.number_input('Cari angka untuk histogram gambar: ',
                             min_value=391,
                             max_value=400,
                             value=391,
                             step=1,)

hist_emotion = st.radio("Pilih emosi yang akan digunakan untuk menampilkan histogram",
                       ('Senang', 'Netral', 'Sedih'))

if img_emotion == 'Senang':

    happy = "C:/Tugas/PPDM/Tugas 2/Pictures/Happy"
    img_dir = happy + '/' + f'happy-0{str(hist_number)}.jpg'
    pic = hist_for_photo(img_dir)
    fig, ax = plt.subplots()
    ax.hist(pic, bins=256)

    st.pyplot(fig)

if img_emotion == 'Netral':

    neutral = "C:/Tugas/PPDM/Tugas 2/Pictures/Neutral"
    img_dir = happy + '/' + f'happy-0{str(hist_number)}.jpg'
    pic = hist_for_photo(img_dir)
    fig, ax = plt.subplots()
    ax.hist(pic, bins=256)

    st.pyplot(fig)

if img_emotion == 'Sedih':

    sad = "C:/Tugas/PPDM/Tugas 2/Pictures/Sad"
    img_dir = happy + '/' + f'happy-0{str(hist_number)}.jpg'
    pic = hist_for_photo(img_dir)
    fig, ax = plt.subplots()
    ax.hist(pic, bins=256)

    st.pyplot(fig)


# segmen orde pertama
first_order_emotion = st.radio("Pilih emosi yang akan ditampilkan untuk orde pertama",
                       ('Senang', 'Netral', 'Sedih'))

if first_order_emotion == 'Senang':

    datas = data_for_stats('Happy')
    df = first_order_stat(datas, ['Happy']*len(datas))
    st.table(df)

if first_order_emotion == 'Netral':

    datas = data_for_stats('Neutral')
    df = first_order_stat(datas, ['Neutral']*len(datas))
    st.table(df)

if first_order_emotion == 'Sedih':

    datas = data_for_stats('Sad')
    df = first_order_stat(datas, ['Sad']*len(datas))
    st.table(df)


# segmen matriks GLCM
glcm_number = st.number_input('Cari angka dari file gambar untuk GLCM: ',
                             min_value=391,
                             max_value=400,
                             value=391,
                             step=1,)

glcm_angle = st.number_input('Cari sudut dari file gambar untuk GLCM: ',
                             min_value=0,
                             max_value=135,
                             value=0,
                             step=45,)

glcm_emotion = st.radio("Pilih emosi yang akan digunakan untuk menampilkan matriks GLCM",
                       ('Senang', 'Netral', 'Sedih'))

if glcm_emotion == 'Senang':

    happy = "C:/Tugas/PPDM/Tugas 2/Pictures/Happy"
    img_dir = happy + '/' + f'happy-0{str(glcm_number)}.jpg'
    st.table(pd.DataFrame(glcm_for_image(img_dir, [glcm_angle])))

if glcm_emotion == 'Netral':

    neutral = "C:/Tugas/PPDM/Tugas 2/Pictures/Neutral"
    img_dir = neutral + '/' + f'neutral-0{str(glcm_number)}.jpg'
    st.table(pd.DataFrame(glcm_for_image(img_dir, [glcm_angle])))

if glcm_emotion == 'Sedih':

    sad = "C:/Tugas/PPDM/Tugas 2/Pictures/Sad"
    img_dir = sad + '/' + f'sad-0{str(glcm_number)}.jpg'
    st.table(pd.DataFrame(glcm_for_image(img_dir, [glcm_angle])))


# segmen orde kedua
second_order_emotion = st.radio("Pilih emosi yang akan ditampilkan untuk orde kedua",
                       ('Senang', 'Netral', 'Sedih'))

if second_order_emotion == 'Senang':

    datas = data_for_stats('Happy')
    df = concat_calculation(datas, ['Happy']*len(datas))
    st.table(df)

if second_order_emotion == 'Netral':

    datas = data_for_stats('Neutral')
    df = concat_calculation(datas, ['Neutral']*4)
    st.table(df)

if second_order_emotion == 'Sedih':

    datas = data_for_stats('Sad')
    df = concat_calculation(datas, ['Sad']*4)
    st.table(df)

    
# membuat histogram untuk orde kedua
hist2_number = st.number_input('Cari sudut dari file gambar: ',
                             min_value=0,
                             max_value=135,
                             value=0,
                             step=45,)

hist2_emotion = st.radio("Pilih emosi yang akan digunakan untuk menampilkan histogram orde kedua",
                       ('Senang', 'Netral', 'Sedih'))

if hist2_emotion == 'Senang':

    datas = data_for_stats('Happy')
    df = concat_calculation(datas, ['Happy']*len(datas))
    for i in df.columns[3:]:
        st.bar_chart(data=df[df['Angle'] == hist2_number], x='Picture', y=i, width=0, height=0, use_container_width=True)

if hist2_emotion == 'Netral':

    datas = data_for_stats('Neutral')
    df = concat_calculation(datas, ['Neutral']*len(datas))
    for i in df.columns[3:]:
        st.bar_chart(data=df[df['Angle'] == hist2_number], x='Picture', y=i, width=0, height=0, use_container_width=True)

if hist2_emotion == 'Sedih':

    datas = data_for_stats('Sad')
    df = concat_calculation(datas, ['Sad']*len(datas))
    for i in df.columns[3:]:
        st.bar_chart(data=df[df['Angle'] == hist2_number], x='Picture', y=i, width=0, height=0, use_container_width=True)
