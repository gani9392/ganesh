import streamlit as st


def Tran_Eff(Ratin, CL, FCL, K, PF):
    Eff = (K * Ratin * PF) / (K * Ratin * PF + CL + (K**2) * FCL)
    CUL = (K**2) * FCL
    return Eff, CUL

st.title("Transformer Efficiency Calculator - Roll No. - PS No.")

st.subheader("Input Transformer Parameters")


Ratin = st.number_input("Rating of Transformer (VA):", min_value=0.0, step=100.0)
CL = st.number_input("Core Losses (CL) in Watts:", min_value=0.0, step=1.0)
FCL = st.number_input("Full Load Copper Losses (FCL) in Watts:", min_value=0.0, step=1.0)
K = st.number_input("Loading on Transformer (K):", min_value=0.0, step=0.1)
PF = st.number_input("Power Factor (PF):", min_value=0.0, max_value=1.0, step=0.01)

if st.button("Calculate Efficiency"):
    if K > 0:  
        Eff, CUL = Tran_Eff(Ratin, CL, FCL, K, PF)
        st.success(f"Efficiency of the Transformer: {Eff:.2%}")
        st.success(f"Copper Losses (CUL): {CUL:.2f} Watts")
    else:
        st.error("Loading on Transformer (K) must be greater than zero.")