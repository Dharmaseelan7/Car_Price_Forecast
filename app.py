import streamlit as st
import pickle

file = open("car_model.pkl", "rb")
car_model = pickle.load(file)


st.markdown(
    "<h1 style='text-align: center; font-size:35px;'>Discover Your Car's Market Value</h1>",
    unsafe_allow_html=True,
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    original_price = st.number_input("Original Price(in Lakhs)", max_value=75.0)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
    transmission_type = st.selectbox("Transmission Type", ["Automatic", "Manual"])
    year_of_purchase = st.slider(
        "Year of Purchase", min_value=2000, max_value=2020, value=2010
    )
with col2:
    kilometers_driven = st.number_input("Kilometers Driven", max_value=100000)
    no_of_owners = st.selectbox("No of Previous Owners", [0, 1, 2])
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])
predict = st.button("Get Selling Price")

inputs = [
    year_of_purchase,
    original_price,
    kilometers_driven,
    fuel_type,
    seller_type,
    transmission_type,
    no_of_owners,
]


def encode_inputs(fuel_type, seller_type, transmission_type):
    if fuel_type == "Petrol":
        inputs[3] = 0
    elif fuel_type == "Diesel":
        inputs[3] = 1
    if seller_type == "Individual":
        inputs[4] = 1
    elif seller_type == "Dealer":
        inputs[4] = 0
    if transmission_type == "Automatic":
        inputs[5] = 1
    elif transmission_type == "Manual":
        inputs[5] = 0


encode_inputs(fuel_type, seller_type, transmission_type)

if predict:
    selling_price = car_model.predict([inputs])
    write = """Estimated Selling Price : {:.2f}Lakhs""".format(selling_price[0])
    st.success(write)
