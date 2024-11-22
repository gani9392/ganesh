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

st.title("2205A21068 - S6")

# Create a container for the input parameters and output results
with st.container():
    st.header("Transformer Parameters")

    # Create two columns: one for inputs and one for outputs
    input_col, output_col = st.columns(2)

    with input_col:
        VA = st.number_input("Transformer Rating (VA)", min_value=0.0, value=10000.0, step=100.0)
        CL = st.number_input("Core Losses (CL) in watts", min_value=0.0, value=100.0, step=10.0)
        FCL = st.number_input("Full Load Copper Losses (FCL) in watts", min_value=0.0, value=200.0, step=10.0)
        
        # Change K and PF to number inputs
        K = st.number_input("Loading on Transformer (K) as a fraction (0 to 1)", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
        PF = st.number_input("Power Factor (PF) (0 to 1)", min_value=0.0, max_value=1.0, value=0.9, step=0.01)

        if st.button("Calculate"):
            if K < 0 or K > 1:
                st.error("Loading on Transformer (K) must be between 0 and 1.")
            elif PF < 0 or PF > 1:
                st.error("Power Factor (PF) must be between 0 and 1.")
            else:
                Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)
                # Display results in the output column
                output_col.write(f"### Transformer Efficiency: {Eff:.2f}%")
                output_col.write(f"### Copper Losses: {CUL:.2f} W")
