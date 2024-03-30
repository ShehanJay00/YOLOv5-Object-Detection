import streamlit as st
import os

st.title("Widgets")



#Buton 
st.button("This is a Button")

button = st.button('Press Me')
if button:
    st.error('You touched my ulaala')




#Checkbox
st.header('This is Checkbox')
checkbox = st.checkbox('Do you want to Agree?')
if checkbox:
    st.warning('You checked')
else:
    st.success('You Uncheked')




#RadioButton
#Select one item from list
st.header('This is my RadioButton')

options = ('Sri-Lanka','India','Ausi','Swiss')
radio_button = st.radio('What is the fav country of you?' , options)
st.write('Your fav country is',radio_button)   




#selectbox
st.header('This is my SelectBox')
options = ('Email','Phone','Wapp' , 'Linkedin')
select_box = st.selectbox('How do you like to cantact me?',options,index=1)  #set default shown value for index 1 , Phone
st.write('My Fav is',select_box)




#Slider
st.header('This is Slider')
slider_range = st.slider("How Old Are You ?", min_value=10 ,max_value=100,step=1,value=20)
st.write('Your Age is ',slider_range)




#Text Inputs
st.header('This is a Text Input')
name = st.text_input("Enter your name Here")
st.write('Your name is' ,name)

age = st.number_input('Enter your age', min_value=1, max_value=100, step=1, value=25)
st.write('Your age is', age)




# Upload a File

st.header('File Uploader')
uploaded_file = st.file_uploader('Choose a File and upload')
if uploaded_file :
    st.success('File updated Successfully')
    details = {
        'filename':uploaded_file.name,
        'filetype':uploaded_file.type,
        'filesize(bytes)':uploaded_file.size,
    }
    st.json(details)



    #Save the File
    st.header('Save the file we Uploaded')
    #save the file in any folder we want
    path =os.path.join('./Uploads',uploaded_file.name)
    with open(path,mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File Saved Succcessfully')




