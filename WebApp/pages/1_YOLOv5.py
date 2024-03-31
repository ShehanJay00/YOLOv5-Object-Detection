import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

st.set_page_config(page_title="YOLOv5",
                layout='wide',
                page_icon='./Images/object.png')

st.title("Welcome to YOLO")
st.write("Please Upload Image for get Predictions")


#This takes some time for Loading, so we put that in below
with st.spinner('Pleas wait untill the Model Loading'):
    yolo = YOLO_Pred(onnx_model=("./Model/best.onnx"),
                data_yaml="./Model/data.yaml")
    #st.balloons()



#Image Upload Section
def upload_image():
    image_file = st.file_uploader(label=('Upload Image Here'))
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        file_details = {'FileName': image_file.name,
                    "FileType": image_file.type,
                    "FileSize": "{:,.2f} MB".format(size_mb)}
        #st.json(file_details)

        #Validate the File
        if file_details["FileType"] in ('image/png','image/jpeg'):
            st.success('Valid Image Uploaded(png or Jpeg)')
            return {"file":image_file, 
                    "details":file_details}
        else:
            st.error('Invalid Format Uploaded')
            st.warning('Upload only png , jpg or jpeg')
            return None
        


def main ():
    object = upload_image()

    if object:
        prediction =False

        image_obj = Image.open(object['file'])
        
        col1,col2 = st.columns(2)

        with col1:
            st.info('Preview of Image')
            st.image(image_obj)

        with col2:
            st.subheader('Check Below for file Details')
            st.json(object['details'])
            button  = st.button('Get Detections from YOLO')
            if button:
                with st.spinner("""
                Getting Objects from Image, Please wait
                                """):
                    #Convert Image object into Array
                    image_array = np.array(image_obj)
                    pred_img = yolo.predictions(image_array)
                    pred_img_obj = Image.fromarray(pred_img)
                    prediction = True
        

        if prediction:
            st.subheader("Predcited Image")
            st.caption('Object Detection From YOLOv5 Model')
            st.image(pred_img_obj)

                
if __name__ == "__main__":
    main()


    


#$ pip install -U streamlit-webrtc for Real Ttime Communication
# Go to the Github repository appears in the top