# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:52:22 2024

@author: Acer
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('heart_decision_model.sav', 'rb'))

parkinson_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# create sidebar
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'], 
                           icons=['activity', 'heart', 'person'],
                           default_index = 0)
    

if selected == 'Diabetes Prediction':
    
    st.title('Diabetes Prediction using ML')
    
    
    # taking data from user 
    # arrange the text area colwise
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies	= st.text_input('No. of Pregnancies')
        
    with col2:        
        Glucose	= st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin	= st.text_input('Insulin value')
        
    with col3:
        BMI	= st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the person')
    
    
    diab_diagonosis = ''
    
    # predictive function
    if st.button('Diabetes Prediction Result'):
         
        diab_pred = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                           Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_pred[0] == 0):
            diab_diagonosis = 'The person is not diabetic'
        else:
          diab_diagonosis = 'The person is diabetic'
          
          
    st.success(diab_diagonosis)
        

if selected == 'Heart Disease Prediction':
    
    st.title('Heart Disease Prediction using ML')
    
    # taking the input
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age value')
        
    with col2:
        sex	= st.text_input('Sex')
        
    with col3:
        cp	= st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestorol in mg/dl')
        
    with col3:
        fbs	= st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg	= st.text_input('Resting Electrocardiographic Result')
        
    with col2:
        thalach	= st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang	= st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak	= st.text_input('ST depression induced by Exercise')
        
    with col2:
        slope	= st.text_input('Slope of the Peak Exercise ST segment')
        
    with col3:
        ca	= st.text_input('Major vessel colored by flourosopy')
    
    with col1:
        thal= st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    hrt_diagonosis = ''
    
    # predictive function
  
    if st.button('Heart Disease Result'):
        
        hrt_pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, 
                                              thalach, exang, oldpeak, slope, ca, thal]])
        if (hrt_pred[0] == 0):
          hrt_diagonosis = 'The Pearson does not have heart disease'
        else: hrt_diagonosis = 'The Pearson has heart disease'
        
    st.success(hrt_diagonosis)
    
    

if selected == 'Parkinson Prediction':
    
    st.title('Parkinson Prediction using ML') 
    # taking input
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    with col1:
        Fo	= st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        Fhi = st.text_input('MDVP: Fhi(Hz)')	
        
    with col3:
        Flo = st.text_input('MDVP: Flo(Hz)')	
        
    with col4:
        Jitter = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_abs = st.text_input('MDVP: Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        JDDP = st.text_input('Jitter: DDP')

    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')	
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(db)')
        
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')

    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spr = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
    
    prk_diagonosis = ''
    
    # predictive function
    
    if st.button('Parkinsons Result'):
        
        prk_pred = parkinson_model.predict([[Fo, Fhi, Flo, Jitter, Jitter_abs, RAP, PPQ, JDDP, Shimmer,
                                     Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, 
                                     spr, spread2, D2, PPE]])
        if (prk_pred[0] == 0):
          prk_diagonosis = "The Person does not have Parkinsons Disease"
        
        else:
          prk_diagonosis = "The Person has Parkinsons"
        
    st.success(prk_diagonosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

