import streamlit as st
import joblib

st.set_page_config(layout="wide")
model = joblib.load("regression.joblib")
st.number_input("Size (in sqft)", min_value=100, max_value=10000, value=200, step=50, key="size")
st.number_input("Number of rooms", min_value=1, max_value=20, value=3, step=1, key="nb_rooms")
st.checkbox("Garden", value=False, key="garden")

if st.button("Predict the price"):
	garden = 1 if st.session_state.garden else 0
	X_new = [[st.session_state.size, st.session_state.nb_rooms, garden]]
	price = model.predict(X_new)[0]
	st.write(f"Le prix est de {price:,.2f} €")