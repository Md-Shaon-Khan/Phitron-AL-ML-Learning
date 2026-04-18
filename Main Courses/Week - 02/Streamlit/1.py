import streamlit as st 

st.title("This is title")
st.header("This is a header")
st.subheader("This is a subheader")


st.markdown("**Markdown** _is_ supported! [Visit Streamlit](https://streamlit.io)")
st.text("This is plain text")
st.write("`st.write()` can handle *mixed content*, like **bold**, _italic_, and numbers:", 123)

st.markdown("### Code Block Example")
st.code("""
# Python example
def greet(name):
    return f"Hello, {name}!"
print(greet("Streamlit"))
""", language="python")

st.markdown("#### Inline LaTeX: $a^2 + b^2 = c^2$")
st.latex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")

st.success("This is a success message.")
st.warning("Be careful! This is a warning.")
st.error("Oops! Something went wrong.")
st.info("This is some information.")

st.markdown("> **Tip:** Use feedback messages to guide the user.")