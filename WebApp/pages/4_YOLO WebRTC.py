import streamlit as sc
from streamlit_webrtc import webrtc_streamer
import av
from yolo_predictions import YOLO_Pred

# Load Model
yolo  = YOLO_Pred('./Model/best.onnx','./Model/data.yaml')



def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    #Any operation you can do here like Fliping
    #flipped = img[::-1,:,:]
    pred_img = yolo.predictions(img)

    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback ,media_stream_constraints={"video":True , "audio":False} )