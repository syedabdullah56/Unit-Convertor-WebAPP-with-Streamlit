import streamlit as st

st.set_page_config(page_title="👑Pro Unit Converter",layout="centered")

st.title("👑Pro Unit Converter")

st.write("😊You can convert Length,Mass,Time and Temperature in its different units?😎")

#Selector for different physical quantities
physical_quantities=['Length','Mass','Time','Temperature']
selected_physical_quantity= st.selectbox(
    "🙂Select the physical quantity?",
    physical_quantities,
)

# Checking Which Quantity is selected and making logic according to this
mass_units={
    'Kilogram(kg)':1,    #base unit
    'Gram(g)':1000,
    'Milligram(mg)':1000000,
    'Pound(lb)':2.20462,
    'Ton(ton)':0.00110231,
}
length_units={
    'Kilometer(km)':1,   #base unit
    'Meter(m)':1000,
    'Centimeter(cm)':100000,
    'Millimeter(mm)':1000000,
}
time_units={
    'Second(s)':1,      #base unit
    'Millisecond(ms)':1000,
    'Microsecond(μs)':1000000,
}


# Handling length
if selected_physical_quantity == 'Length':
    len_units_arr=['Kilometer(km)','Meter(m)','Centimeter(cm)','Millimeter(mm)']
    len_from= st.selectbox(
    "🙄Select the unit of length you want to be converted?",
    len_units_arr,
)
    number = st.number_input("Insert Value:") 

    len_to= st.selectbox(
    "🙄Select the unit of length you want to be converted in?",
    len_units_arr,
)
    
    from_unit=length_units[len_from]
    to_unit=length_units[len_to]
    base_unit=number/from_unit
    converted_unit=base_unit*to_unit
    if len_from and number and len_to:
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {len_from} is equal to {converted_unit} {len_to}😎')

#Handling Mass
if selected_physical_quantity == 'Mass':
    mass_units_arr=['Kilogram(kg)','Gram(g)','Milligram(mg)','Pound(lb)','Ton(ton)']
    mass_from= st.selectbox(
    "🙄Select the unit of mass you want to be converted?",
    mass_units_arr,

)
    number = st.number_input("Insert Value:") 

    mass_to= st.selectbox(
    "🙄Select the unit of mass you want to be converted in?",
    mass_units_arr,
)
    from_unit=mass_units[mass_from]
    to_unit=mass_units[mass_to]
    base_unit=number/from_unit
    converted_unit=base_unit*to_unit
    if mass_from and number and mass_to:
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {mass_from} is equal to {converted_unit} {mass_to}😎')
    
# Handling Time
if selected_physical_quantity == 'Time':
    time_units_arr=['Second(s)','Millisecond(ms)','Microsecond(μs)']
    time_from= st.selectbox(
    "🙄Select the unit of time you want to be converted?",
    time_units_arr,
)
    number = st.number_input("Insert Value:") 

    time_to= st.selectbox(
    "🙄Select the unit of time you want to be converted in?",
    time_units_arr,
)
    from_unit=time_units[time_from]
    to_unit=time_units[time_to]
    base_unit=number/from_unit
    converted_unit=base_unit*to_unit
    if time_from and number and time_to:
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {time_from} is equal to {converted_unit} {time_to}😎')

# Handling Temperature
if selected_physical_quantity == 'Temperature':
    temp_units_arr=['Kelvin(k)','Centigrate(C)','Fahrenheit(F)']
    temp_from= st.selectbox(
    "🙄Select the unit of temperature you want to be converted?",
    temp_units_arr,
)
    number = st.number_input("Insert Value:") 

    temp_to= st.selectbox(
    "🙄Select the unit of temperature you want to be converted in?",
    temp_units_arr,
)   
    
    if temp_from == 'Kelvin(k)' and temp_to == 'Centigrate(C)':
        converted_unit=number-273.15
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    elif temp_from == 'Kelvin(k)' and temp_to == 'Fahrenheit(F)':
        converted_unit=(number-273.15)*1.8+32
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    elif temp_from == 'Centigrate(C)' and temp_to == 'Kelvin(k)':
        converted_unit=number+273.15
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    elif temp_from == 'Centigrate(C)' and temp_to == 'Fahrenheit(F)':
        converted_unit=number*1.8+32
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    elif temp_from == 'Fahrenheit(F)' and temp_to == 'Kelvin(k)':
        converted_unit=(number-32)/1.8+273.15
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    elif temp_from == 'Fahrenheit(F)' and temp_to == 'Centigrate(C)':
        converted_unit=(number-32)/1.8
        button=st.button("⏩Convert")
        if button:
           st.write(f'{number} {temp_from} is equal to {converted_unit} {temp_to}😎')

    else:
        st.write("😊Please select valid units😎")
        


