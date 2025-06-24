import streamlit as st

st.set_page_config(page_title="CalcPy", layout="centered")

st.title("🧮 CalcPy - La Calculadora de Python")

st.markdown("Introduce dos números y elige la operación que deseas realizar.")

# Entradas de números
digito1 = st.number_input("Introduce el primer número", format="%.2f", step=1.0)
digito2 = st.number_input("Introduce el segundo número", format="%.2f", step=1.0)

# Selección de operación
operacion = st.selectbox("Selecciona una operación", ["Suma", "Resta", "Multiplicación", "División"])

# Calcular cuando el usuario presione el botón
if st.button("Calcular"):
    if operacion == "Suma":
        resultado = digito1 + digito2
        st.success(f"El resultado de la suma es: {resultado:.2f}")

    elif operacion == "Resta":
        resultado = digito1 - digito2
        st.success(f"El resultado de la resta es: {resultado:.2f}")

    elif operacion == "Multiplicación":
        resultado = digito1 * digito2
        st.success(f"El resultado de la multiplicación es: {resultado:.2f}")

    elif operacion == "División":
        if digito2 == 0 or digito1 == 0:
            st.error("⚠️ Error: No se puede dividir por cero.")
        else:
            resultado = digito1 / digito2
            st.success(f"El resultado de la división es: {resultado:.2f}")
