import streamlit as st

st.set_page_config(page_title="Home",
                layout="wide",
                page_icon="./Images/home.png")

st.title('YOLOv5 Object Detection')
st.caption('This Web Application Demonstrates Object Detection')


#Content/Body
st.markdown("""
#### This App Detects Objects From Images and Real Time Videos
- Automatically Detects 20 Objects
- [Click Here To Try](/YOLOv5/)
            """)
st.markdown("""
These are the list of Objects this model can detected         
1. person         
2. car 
3. chair 
4. bottle
5. pottedplant
6. bird
7. dog
8. sofa
9. bicycle
10. horse
11. boat
12. motorbike
13. cat
14. tvmonitor
15. cow
16. sheep
17. aeroplane
18. train
19. diningtable
20. bus          
""")

