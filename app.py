import streamlit as st
from backend import check_plagiarism

st.set_page_config(page_title="CopyDetect", layout="centered")
st.title("CopyDetect - Plagiarism Checker")

text_input = st.text_area("Enter text to check:", height=300)

if st.button("Check Plagiarism"):
    if text_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Scanning for plagiarism..."):
            print("hi")
            result = check_plagiarism(text_input)
            print(result)
        if "error" in result:
            st.exception(result["error"])
        elif not result["matches"]:
            st.success("No plagiarism detected!")
        else:
            st.success(f"Plagiarism found in {len(result['matches'])} source(s):")

            for i, match in enumerate(result["matches"], 1):
                st.markdown(f"""
                ### {i}. [Source Link]({match['url']})
                - 🔢 **Match Score:** {match['score']}%
                - 📄 **Matched Words:** {match['word_count']}
                """)
