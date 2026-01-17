import streamlit as st
from pdf_utils import extract_text_from_pdf
from claim_extractor import extract_claims
from verifier import verify_claim

st.set_page_config(page_title="Fact Checker AI")

st.title("📄 AI Fact-Checking Web App")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)

    st.success("Text extracted")

    with st.spinner("Finding claims..."):
        claims = extract_claims(text)

    st.subheader("🔍 Extracted Claims")

    for claim in claims:
        if claim.strip():
            st.markdown(f"**{claim}**")
            with st.spinner("Verifying..."):
                result = verify_claim(claim)
            st.info(result)
