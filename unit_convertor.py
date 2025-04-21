import streamlit as st

st.title("Unit Convertor")
st.write("Welcome to my first python project, built using Streamlit.")

conversion_type = st.selectbox("Choose a conversion type:", ['length', 'mass', 'temperature', 'time', 'volume'])

# Length values
length_unit_values = {
    'kilometre': 1000,
    'metre': 1,
    'centimetre': 0.01,
    'millimetre': 0.001,
    'micrometre': 1e-6,
    'nanometre': 1e-9,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
    'nautical mile': 1852
    }

# Mass values
mass_unit_values = {
  'tonne': 1000,
  'kilogram': 1,
  'gram': 0.001,
  'milligram': 1e-6,
  'microgram': 1e-9,
  'imperial ton': 1016.05,
  'US ton': 907.18474,
  'stone': 6.35029,
  'pound': 0.453592,
  'ounce': 0.0283495,
  }

# Time values
time_unit_values = {
  'nanosecond': 1e-9,
  'microsecond': 1e-6,
  'millisecond': 1e-3,
  'second': 1,
  'minute': 60,
  'hour': 3600
  }

# Volume values
volume_unit_values = {
  'US liquid gallon': 3.78541,
  'US liquid quart': 0.94635,
  'US liquid pint': 0.473176,
  'US legal cup': 0.24,
  'US fluid ounce': 0.0295735, 
  'US tablespoon': 0.0147867, 
  'US teaspoon': 0.0049289, 
  'cubic meter': 1000, 
  'liter': 1,
  'milliliter': 0.001,
  'imperial gallon': 4.546, 
  'imperial quart': 1.137 ,
  'imperial pint': 0.568181, 
  'imperial cup': 0.284131 ,
  'imperial fluid ounce': 0.0284131,
  'imperial tablespoon': 0.017758 ,
  'imperial teaspoon': 0.00591939, 
  'cubic foot': 28.317, 
  'cubic inch':  0.0163870758

}   


value = st.number_input("Enter a value:")

def convert_length(val, from_unit, to_unit):
 return val * length_unit_values[from_unit] / length_unit_values[to_unit]
 
def convert_mass(val, from_unit, to_unit):
 return val * mass_unit_values[from_unit] / mass_unit_values[to_unit]

def convert_temperature(val, from_unit, to_unit):
    if from_unit == 'degree celsius':
      val_in_celsius = val
    elif from_unit == 'fahrenheit':
      val_in_celsius = (val - 32) * 5/9
    else: 
      val_in_celsius = val - 273.15

    if to_unit == 'degree celsius':
     return val_in_celsius
    elif to_unit == 'fahrenheit':
     return (val_in_celsius * 9/5) + 32
    else:
     return val_in_celsius + 273.15
 
def convert_time(val, from_unit, to_unit):
 return val * time_unit_values[from_unit] / time_unit_values[to_unit]

def convert_volume(val, from_unit, to_unit):
  return val * volume_unit_values[from_unit] / volume_unit_values[to_unit]
     
if conversion_type == "length":
     conversion_units = st.selectbox("Choose a conversion unit (from):", ['kilometre', 'metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile', 'yard', 'foot', 'inch', 'nautical mile'], key='length_unit') 
     
     conversion_unit = st.selectbox("Choose a conversion unit (to):", ['kilometre','metre', 'centimetre', 'millimetre', 'micrometre', 'nanometre', 'mile', 'yard', 'foot', 'inch', 'nautical mile'], key='length_unit2')
     
     
elif conversion_type == "mass":
     conversion_units = st.selectbox ("Choose a conversion unit (from):", ['tonne','kilogram', 'gram', 'milligram', 'microgram', 'imperial ton', 'US ton', 'stone', 'pound', 'ounce'], key='mass_unit')

     conversion_unit = st.selectbox("Choose a conversion unit (to):", ['tonne',
     'kilogram', 'gram', 'milligram', 'microgram', 'imperial ton', 'US ton', 'stone', 'pound', 'ounce'], key='mass_unit2')
     

elif conversion_type == "temperature":
    conversion_units = st.selectbox ("Choose a conversion unit (from):", ['degree celsius','fahrenheit', 'kelvin'], key='temperature_unit')

    conversion_unit = st.selectbox ("Choose a conversion unit (to):", ['degree celsius','fahrenheit', 'kelvin'], key='temperature_unit2')

     
elif conversion_type == 'time':
    conversion_units = st.selectbox ("Choose a conversion unit (from):", ['nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour'], key='time_unit')  
    conversion_unit = st.selectbox ("Choose a conversion unit (to):", ['nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour'], key='time_unit2')  

else:
    conversion_units = st.selectbox("Choose a conversion unit (from):", ['US liquid gallon', 'US liquid quart', 'US liquid pint', 'US legal cup', 'US fluid ounce', 'US tablespoon', 'US teaspoon', 'cubic meter', 'liter', 'milliliter', 'imperial gallon', 'imperial quart', 'imperial pint', 'imperial cup', 'imperial fluid ounce', 'imperial tablespoon', 'imperial teaspoon', 'cubic foot', 'cubic inch'], key='volume_unit')

    conversion_unit = st.selectbox("Choose a conversion unit (to):", ['US liquid gallon', 'US liquid quart', 'US liquid pint', 'US legal cup', 'US fluid ounce', 'US tablespoon', 'US teaspoon', 'cubic meter', 'liter', 'milliliter', 'imperial gallon', 'imperial quart', 'imperial pint', 'imperial cup', 'imperial fluid ounce', 'imperial tablespoon', 'imperial teaspoon', 'cubic foot', 'cubic inch'], key='volume_unit2')


 # Display result dynamically when value is entered
if value !=0:  
    if conversion_type == 'length':
     answer = convert_length(value, conversion_units, conversion_unit)
     st.success(f"Your answer: {answer:.4f} {conversion_unit}")

    elif conversion_type == 'mass':
     answer = convert_mass(value, conversion_units, conversion_unit)
     st.success(f"Your answer: {answer:.4f} {conversion_unit}")        
    
    elif conversion_type == 'temperature':
      answer = convert_temperature(value, conversion_units, conversion_unit)
      st.success(f"Your answer: {answer:.2f} {conversion_unit}")

    elif conversion_type == 'time':
      answer = convert_time(value, conversion_units, conversion_unit)
      st.success(f"Your answer: {answer:.4f} {conversion_unit}")

    else:
      answer = convert_volume(value, conversion_units, conversion_unit)
      st.success(f"Your answer: {answer:.4f} {conversion_unit}")  
    
    if st.button("Convert"):
      conversion_units, conversion_unit = conversion_unit, conversion_units

