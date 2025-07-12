import streamlit as st
from backend import check_plagiarism_rapidapi

st.set_page_config(page_title="CopyDetect", layout="centered")
st.title("CopyDetect - Plagiarism Checker")

text_input = st.text_area("Enter text to check:", height=300)

if st.button("Check Plagiarism"):
    if text_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("🔍 Scanning for plagiarism..."):
            result = check_plagiarism_rapidapi(text_input)


        if "error" in result:
            st.error(f"API Error: {result['error']}")
        elif result.get("percentPlagiarism") == 0:
            st.success("No plagiarism detected!")
        else:
            percent = result.get("percentPlagiarism", 0)
            st.warning(f"{percent}% Plagiarism Detected!")

            sources = result.get("sources", [])
            if sources:
                st.markdown("### 🔗 Sources Found:")
                for i, url in enumerate(sources, 1):
                    st.markdown(f"{i}. [Source Link]({url})")
