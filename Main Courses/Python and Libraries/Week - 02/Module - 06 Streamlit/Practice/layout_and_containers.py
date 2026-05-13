import streamlit as st 

# col1, col2 = st.columns(2)

# file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"])
# file1 = st.file_uploader("Upload your video",type=["mp4"])

# with col1:
#   st.write("Left Side")
#   if file is not None:
#     st.image(file)
  
# with col2:
#   st.write("Right Side")
#   if file1 is not None:
#     st.video(file1)

# col1, col2, col3 = st.columns(3)

# container = st.container()

# with container:
#   st.write("Inside container...")

# with st.expander("See details"):
#   st.write("Hidden content")
  
# st.sidebar.title("Menu")
# option = st.sidebar.selectbox("Choose",["Home","About"])

# st.title("ECG Dashboard")

# col1, col2 = st.columns(2)

# with col1:
#   st.metric("Heart Rate","75 BPM")

# with col2:
#   st.metric("Status","Normal")

# with st.expander("Show Raw Data"):
#   st.write("ECG data here")

# st.sidebar.title("Navigation")


# Side menu
with st.sidebar:
    st.title("Menu")
    page = st.selectbox("Page", ["Home", "ECG", "Report"])

# পাশাপাশি 2টা column
col1, col2 = st.columns(2)

with col1:
    st.metric("Heart Rate", "72 BPM", "+2")

with col2:
    st.metric("SpO2", "98%", "-1%")

# Expandable section
with st.expander("বিস্তারিত দেখো"):
    st.write("ECG analysis details...")