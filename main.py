import streamlit as st

# Function to calculate Bacterial Meningitis Score
def calculate_bacterial_meningitis_score(seizure, csf_neutrophils, csf_protein, anc, gram_stain):
    score = 0
    
    # Seizure (1 point)
    if seizure:
        score += 1
        
    # CSF neutrophils ≥1000 cells/μL (1 point)
    if csf_neutrophils >= 1000:
        score += 1
        
    # CSF protein ≥80 mg/dL (1 point)
    if csf_protein >= 80:
        score += 1
    
    # Peripheral ANC ≥10,000 cells/μL (1 point)
    if anc >= 10000:
        score += 1
    
    # CSF Gram stain with bacteria present (2 points)
    if gram_stain:
        score += 2
    
    return score

# Streamlit app
st.title('Bacterial Meningitis Score for Children')

st.write("""
This app calculates the Bacterial Meningitis Score, which estimates the probability of bacterial meningitis in children. 
The score is based on five clinical factors: seizure presence, CSF neutrophil count, CSF protein, peripheral ANC, and CSF Gram stain results.
""")

# User inputs
seizure = st.checkbox('Seizure Present?')
csf_neutrophils = st.number_input('CSF Neutrophils (cells/μL)', min_value=0)
csf_protein = st.number_input('CSF Protein (mg/dL)', min_value=0.0)
anc = st.number_input('Peripheral ANC (cells/μL)', min_value=0)
gram_stain = st.checkbox('CSF Gram Stain Positive for Bacteria?')

# Calculate the score
if st.button('Calculate Bacterial Meningitis Score'):
    score = calculate_bacterial_meningitis_score(seizure, csf_neutrophils, csf_protein, anc, gram_stain)
    
    st.write(f'**Bacterial Meningitis Score:** {score}')
    
    # Interpretation of the score
    if score >= 2:
        st.warning('High risk for bacterial meningitis. Further clinical evaluation needed.')
    else:
        st.success('Low risk for bacterial meningitis.')
