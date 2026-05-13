# # import streamlit as st 

# # st.title(":green-background[My first streamlit web apps] ",anchor=False)

# # st.header("Content 1",divider=True,anchor=False)
# # st.subheader("Content 1 subheader",anchor=False)
# # st.text("Hello World")

# # st.markdown(":red-background[:red[**Hello**] :orange[*World*]] :innocent:")

# # variable1 = 1999
# # variable2 = 2000

# # st.write(f":red-background[:yellow[**{variable1}**], [*{variable2}*]]")

# # import streamlit as st 

# # st.title(":world_map: Input your Information",anchor=False)
# # st.divider()

# # name = st.text_input("Enter your name:",placeholder="Your name...")

# # st.write(f"Your name is: {name}")

# # st.divider()

# # age = st.number_input("Enter your age",value=None,placeholder="Type your age...")

# # st.write(f"Your age is: {age}")

# # st.divider()


# # selected = st.selectbox("Choose your profession",("Student","Employee","Teacher"),index=None,accept_new_options=True)

# # st.divider()

# # password = st.text_input("Enter your password here",placeholder="Your password...",type="password")

# # st.write(f"Your password is: {password}")

# # pressed = st.button("Enter to confirm",type="primary")

# # if pressed:
# #   st.markdown(f":red-background[Your name is [**{name}**] and your age is [**{age}**] and your profession is [*{selected}*]]")


# import streamlit as st

# # Page config
# st.set_page_config(page_title="User Info App", page_icon="🌍", layout="centered")

# # Title
# st.title("🌍 User Information Form")
# st.caption("Fill in your details below")

# st.divider()

# # Form (important for better UX)
# with st.form("user_form"):
    
#     col1, col2 = st.columns(2)

#     # Name
#     with col1:
#         name = st.text_input("👤 Name", placeholder="Your name...")

#     # Age
#     with col2:
#         age = st.number_input("🎂 Age", min_value=0, step=1, placeholder="Your age...")

#     # Profession
#     profession = st.selectbox(
#         "💼 Profession",
#         ("Student", "Employee", "Teacher"),
#         index=None,
#         placeholder="Select your profession..."
#     )

#     # Password
#     password = st.text_input(
#         "🔒 Password",
#         placeholder="Enter password...",
#         type="password"
#     )

#     # Submit button
#     submitted = st.form_submit_button("✅ Submit")

# # Output Section
# if submitted:
#     if not name or age is None or not profession:
#         st.warning("⚠️ Please fill all required fields")
#     else:
#         st.success("🎉 Information Submitted Successfully!")

#         st.divider()

#         st.markdown("### 📋 Your Information")
#         st.write(f"**Name:** {name}")
#         st.write(f"**Age:** {age}")
#         st.write(f"**Profession:** {profession}")
#         st.write(f"**Password:** {'*' * len(password)}")  # Hide password

import streamlit as st 
st.title("Input your files", anchor=False)
st.divider()

images = st.file_uploader("Enter image",
                 type=['jpg','jpeg','png'],
                 accept_multiple_files=True)


if images:
   col = st.columns(3)
   
   for i, image in enumerate(images):
     with col[i % 3]:
       st.image(image)
       
st.divider()

st.image("G:/Picture/Camera Roll/WIN_20241103_14_26_01_Pro.jpg")

st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6")