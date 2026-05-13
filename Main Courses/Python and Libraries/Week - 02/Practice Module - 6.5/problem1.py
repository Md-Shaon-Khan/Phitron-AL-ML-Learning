import streamlit as st 

number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)
operation = st.selectbox("Select the operation", ("",'+', '-', '*', '/'), index=0)

if st.button('Answer', type="primary"):
    if operation == '+':
        result = number1 + number2
        st.success(f"Result is {result}")
    elif operation == '-':
        result = number1 - number2
        st.success(f"Result is {result}")
    elif operation == '*':
        result = number1 * number2
        st.success(f"Result is {result}")
    elif operation == '/':
        if number2 == 0:
            st.error("Number 2 can't be 0.")
        else:
            result = number1 / number2
            st.success(f"Result is {result}")
    else:
      st.error("Select a operation.")