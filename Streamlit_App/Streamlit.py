import streamlit as st

#To print  anything
st.write("Hello World")

#Text Formating
st.header("This is a Header")
st.subheader("This is a Subheader")
st.caption("This is a caption")
st.text("This is a plain text")

# go to www.streamlit.io for th documentation and search more

#markdown
st.markdown("""
# this is title
## this is Header
### this is subheader
#### this is a subheader 2
this is **Bold Text** and this is *italic text*
""")
# Go and check markdown cheatsheet from markdown website



# Styling the text
# For that we use status elements
# there are three types of status elements
# 1.success 
st.success("This is shown in green color")
# 2.warning 
st.warning("This is shown in yellow color")
# 3.error
st.error("This is shown in red color")


# How to display images and videos
st.subheader("This is an Image")
st.image("./assets/about.png" ,
         caption="this is my image generated from ideoram.ai",
         width = 1000)

st.subheader("Display a Video")
st.video("../Predictions_with_yolo/video.mp4")

