import streamlit as st
import pandas as pd
from processor import process_cutoff_data

st.title("📊 CET Cutoff Analyzer (Last 3 Years)")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully ✅")
    st.dataframe(df.head())

    if st.button("Process Data 🚀"):

        results = process_cutoff_data(df)

        st.subheader("📊 Processed Data")

        # Show and download each category
        for category, data in results.items():

            st.write(f"### Category: {category}")
            st.dataframe(data)

            csv = data.to_csv(index=False).encode('utf-8')

            st.download_button(
                label=f"⬇ Download {category} CSV",
                data=csv,
                file_name=f"{category}_cutoff.csv",
                mime="text/csv"
            )
