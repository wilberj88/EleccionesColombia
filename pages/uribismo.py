import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('Mando PreCampaña')
st.text('Alcaldía de Bogotá: históricos, tendencias y proyecciones 2023')

# Create file uploader object
upload_file = st.file_uploader('Upload a E14 or E24 or E26')

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)
    tables = camelot.read_pdf(upload_file)
    st.write("Total tables extracted:", tables.n)
    st.write(tables)
    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())

    # Create a section for matplotlib figure
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)
