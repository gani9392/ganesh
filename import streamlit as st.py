import streamlit as st
import numpy as np

def Tran_Eff(VA, CL, FCL, K, PF):
    """Calculates transformer efficiency and copper losses.

    Args:
        VA: Transformer rating in VA
        CL: Core losses in watts
        FCL: Full load copper losses in watts
        K: Loading on transformer (0-1)
        PF: Power factor

    Returns:
        Eff: Efficiency
        CUL: Copper losses
    """

    Eff = (K * VA * PF) / (K * VA * PF + CL + K**2 * FCL)
    CUL = K**2 * FCL

    return Eff, CUL

def main():
    st.title("02341A0259-PS6: Transformer Efficiency Calculator")

    # Input parameters
    VA = st.number_input("Transformer Rating (VA)", min_value=1, step=1)
    CL = st.number_input("Core Losses (Watts)", min_value=0, step=1)
    FCL = st.number_input("Full Load Copper Losses (Watts)", min_value=0, step=1)
    K = st.slider("Loading (K)", 0.0, 1.0, 0.5, 0.1)
    PF = st.slider("Power Factor (PF)", 0.0, 1.0, 0.8, 0.1)

    # Calculate efficiency and copper losses
    Eff, CUL = Tran_Eff(VA, CL, FCL, K, PF)

    # Display results
    st.write(f"Efficiency: {Eff:.2f}%")
    st.write(f"Copper Losses: {CUL:.2f} Watts")

if __name__ == "__main__":
    main()