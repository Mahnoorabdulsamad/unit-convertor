import streamlit as st

st.title("Unit Convertor App")
st.markdown("### Convert units of length, time, and weight")
st.write("Welcome to the unit convertor app. You can convert units of length, temperature, and weight using this app. Please select the type of conversion you want to perform from the sidebar.")

Category = st.selectbox("Select the type of conversion", ["Length", "Time", "Weight"])

def convert_unit(Category , value , unit):
    if Category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif Category == "weight":
        if unit == "Kilometers to Pounds":

            return value * 2.20462
        elif unit == "Pounds to Kilometers":
            return value / 2.20462
        
    elif Category == "Time":

        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        return 0
        
if Category == "Lenth":
     unit = st.selectbox("Select the unit", ["Miles to Kilometers" , "Kilometers to Miles"])
elif Category == "Weight":
     unit = st.selectbox("Select the unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif Category == "Time":
     unit = st.selectbox("Select the unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert")
if st.button("Convert"):
    result = convert_unit(Category, value, unit)
    st.success(f"The result is {result:2f}")




            
        
        
    

         
    
    
