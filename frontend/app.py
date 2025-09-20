import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="auto",
)

# Set the theme colors
st.markdown(
    """
    <style>
    :root {
        --primary-color: #B21F33;
        --background-color: #002b36;
        --secondary-background-color: #586e75;
        --text-color: #fafafa;
        --font: sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# loading the saved models

model = pickle.load(open("rf.pkl", 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Predictive Maintenance System',
                          
                          ['Transformer Maintenance System'],
                          icons=['kanban'],
                          default_index=0)


if(selected=="Transformer Maintenance System"):
    # page title
    st.title('Transformer Maintenance Predictive System')
    
    
    # getting the input data from the user
    col1, col2= st.columns(2)
    

    
    with col1:
        Location = st.selectbox( 'Location: 1 FOR URBAN, 0 FOR RURAL',
          ('0', '1'))
    
    with col2:
       Power=st.number_input( 'Enter the power in Kwh')
    
    with col1:
        Self_Protection = st.selectbox('Self-Protection: 1 for self-protected , 0 for not', ('0', '1'))
    
    with col2:
        AverageEarthDischargeDensity  =  st.number_input('Average Earth Discharge Density (Rays/km^2-year)')
    
    with col1:
        MaximumGroundDischargeDensity = st.number_input('Maximum Ground Discharge Density (Rays/km^2-year)')
    
    with col2:
        BurningRate = st.number_input('Burning Rate (Failures/year)')
    
    with col1:
        CriticalityAccordingToPreviousStudyForCeramicsLevel  = st.selectbox('Criticality according to previous study for ceramics level: 1 for high risk, 0 for not', ('0', '1', '2'))
    
    with col2:
        RemovableConnectors  = st.selectbox('Removable Connectors: 1 if removeable, 0 if not', ('0', '1'))
    with col1:
        NumberOfUsers =st.number_input('Number of Users')
            
    
    with col2:
        ElectricPowerNotSupplied = st.number_input('Electric Power Not Supplied (EENS kWh)')
    
    with col2:
        TypeOfInstallation   = st.selectbox('Type of Installation: MACRO WITHOUT ANTI-FRAUD NET:0 , POLE:1, POLE WITH ANTI-FRAUD NET:2,EN H:3,PAD MOUNTED:4,TORRE METALICA:5,OTROS:6,CABINA:7',
          ('0', '1','2','3','4','5','6','7'))
    
    with col1:
        AirNetwork  =  st.selectbox('Air Network: 1 if Air network, 0 if not', ('0', '1'))
    
    with col2:
        kmOfNetworkLT  = st.number_input('Km of Network LT')
    
    
    
    # code for Prediction
    pred = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        prediction = model.predict([[Location,Power,Self_Protection,AverageEarthDischargeDensity,MaximumGroundDischargeDensity,BurningRate,CriticalityAccordingToPreviousStudyForCeramicsLevel,RemovableConnectors,NumberOfUsers,ElectricPowerNotSupplied,TypeOfInstallation,AirNetwork,kmOfNetworkLT]])
        
        if (prediction[0] == 1):
          st.error('Burn')
        else:
          st.success('No Burn')
        
    
