import streamlit as st 


# st.header("Hello World!")
# st.title("Re-execution Demo")

# name = st.text_input("Enter your name")

# if name:
#   st.write(f"Hello, {name}")

# else:
#   st.write("Please Type your name above")
  
# print("Script Executed")

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Markdown** _is_ supported! [visit Streamlit] (https://streamlit.io)")
st.text("This is plain text")
st.write("`st.write()` can be handle *mixed content*, like **bold**, _italic_, and numbers:",123)

st.markdown("### Code Block Example")
st.code(
  
)