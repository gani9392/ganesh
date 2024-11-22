import streamlit as st

def Tran_Eff(VA, CL, FCL, K, PF):
    """
    Calculate Transformer Efficiency and Copper Losses.

    Parameters:
        VA (float): Rating of the transformer in VA
        CL (float): Core losses in watts
        FCL (float): Full Load Copper losses in watts
        K (float): Loading on transformer (as a fraction, e.g., 0.5 for 50%)
        PF (float): Power factor (0 to 1)
    
    Returns:
        tuple: Efficiency (Eff) and Copper losses (CUL)
    """
    CUL = K**2 * FCL  # Equation 2
    Eff = (K * VA * PF) / ((K * VA * PF) + CL + CUL) * 100  # Equation 1
    return Eff, CUL

# Set up the web app title
st.title("Roll No. - Problem Statement No.")

# Collect user inputs
st.sidebar.header("Transformer Parameters")
VA = st.sidebar.number_input("Transformer Rating (VA)", min_value=0.0, value=10000.0, step=100.0)
CL = st.sidebar.number_input("Core Losses (CL) in watts", min_value=0.0, value=100.0, step=10.0)
FCL = st.sidebar.number_input("Full Load Copper Losses (FCL) in watts", min_value=0.0, value=200.0, step=10.0)
K = st.sidebar.slider("Loading on Transformer (K)", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
PF = st.sidebar.slider("Power Factor (PF)", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

# Calculate efficiency and copper losses
if st.button("Calculate"):
    Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)
    st.write(f"### Transformer Efficiency: {Eff:.2f}%")
    st.write(f"### Copper Losses: {CUL:.2f} W")
