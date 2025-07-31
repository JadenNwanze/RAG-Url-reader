import streamlit as st
import requests

st.title("Article Summary Tool")
st.sidebar.title("Articles URL")

raw_urls = []
for i in range(3):
    url = st.sidebar.text_input(f"Url {i+1}")
    raw_urls.append(url)

urls = [url.strip() for url in raw_urls if url.strip()]

# Embed button
embed_clicked = st.sidebar.button("Load & Embed URLs")

# Display loading log for embed
if embed_clicked:
    if not urls:
        st.warning("Please enter at least one valid URL.")
    else:
        with st.spinner("Loading, embedding, and saving to vector database...This may take a few"):
            response = requests.post(
                "http://localhost:8000/embed",
                json={"urls": urls},
                headers={"Content-Type": "application/json"}
            )
        if response.status_code == 200:
            st.success("Documents embedded and saved successfully!")
        else:
            st.error(f"Error during embedding: {response.status_code}")
            st.write(response.text)

# Question asking UI
main_placeholder = st.empty()
query = main_placeholder.text_input("Question: ")
ask_clicked = st.button("Ask question")

if ask_clicked:
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Retrieving answer...This may take a few"):
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": query},
                headers={"Content-Type": "application/json"}
            )

        if response.status_code == 200:
            data = response.json()
            st.success("Answer:")
            st.write(data["answer"])
            st.subheader("Sources:")
            unique_sources = list(set(data["sources"]))  # Remove duplicates
            for src in unique_sources:
                st.write(f"- {src}")
        else:
            st.error(f"Error from server: {response.status_code}")
            st.write(response.text)
