# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title="Credit default prediction", page_icon="🧊", layout="wide")
def load_model():
    filename= 'finalized_default_model.csv'
    loaded_model=pickle.load(open(filename, 'rb'))
    return loaded_model
st.cache_data
def load_data():
    data = pd.read_csv('prosper_data_app.csv')
    return (data.dropna())

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    st.write("Hello Louisdfvertgv")
    data = load_data()
    #model = load_model()
    st.title('Credit default prediction')
    st.markdown('This application is a streamlit dashboard used to predict credit default.😊')
    #define section 1 of the app
    st.header('1. Data Exploration')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Choose your data")
        value = st.slider(
            'Select a value',
            min_value=0.0,
            max_value=100.0,
            value=25.0,
        )
        st.write(value)
        selection = st.selectbox("Select a value", data.columns)
        st.write(selection)

    with col2:
        st.header("Data")
        filtered_data = data
        st.write(filtered_data)

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    row_1 = st.markdown('This section is used to explore the dataset')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
