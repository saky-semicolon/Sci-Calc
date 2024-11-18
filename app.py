import streamlit as st
import math
import cmath

# App title
st.title("🧮 Advanced Scientific Calculator")

# Input for basic operations
st.header("Basic Operations")
num1 = st.number_input("Enter the first number:", key="num1_basic", step=1.0)
num2 = st.number_input("Enter the second number:", key="num2_basic", step=1.0)
operation = st.selectbox("Select an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

if st.button("Calculate Basic Operation"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for trigonometric functions
st.header("Trigonometric Functions")
angle = st.number_input("Enter the angle in degrees:", key="angle_trig", step=1.0)
trig_operation = st.selectbox("Select a trigonometric function:", ["sin", "cos", "tan"])

if st.button("Calculate Trigonometric Function"):
    try:
        radians = math.radians(angle)
        if trig_operation == "sin":
            result = math.sin(radians)
        elif trig_operation == "cos":
            result = math.cos(radians)
        elif trig_operation == "tan":
            result = math.tan(radians)
        st.success(f"{trig_operation}({angle}) = {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for exponential and logarithmic functions
st.header("Exponential and Logarithmic Functions")
exp_log_choice = st.radio("Select a function:", ["Exponential (e^x)", "Natural Log (ln)", "Logarithm (log base 10)"])
num_exp_log = st.number_input("Enter the number:", key="num_exp_log", step=1.0)

if st.button("Calculate Exponential/Logarithm"):
    try:
        if exp_log_choice == "Exponential (e^x)":
            result = math.exp(num_exp_log)
        elif exp_log_choice == "Natural Log (ln)":
            if num_exp_log > 0:
                result = math.log(num_exp_log)
            else:
                result = "Error: Logarithm undefined for non-positive numbers."
        elif exp_log_choice == "Logarithm (log base 10)":
            if num_exp_log > 0:
                result = math.log10(num_exp_log)
            else:
                result = "Error: Logarithm undefined for non-positive numbers."
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for factorial calculation
st.header("Factorial Calculation")
num_factorial = st.number_input("Enter a non-negative integer:", key="num_factorial", step=1.0, min_value=0.0)

if st.button("Calculate Factorial"):
    try:
        if num_factorial.is_integer() and num_factorial >= 0:
            result = math.factorial(int(num_factorial))
            st.success(f"{int(num_factorial)}! = {result}")
        else:
            st.error("Factorial is only defined for non-negative integers.")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for complex number operations
st.header("Complex Number Operations")
real1 = st.number_input("Enter the real part of the first complex number:", key="real1", step=1.0)
imag1 = st.number_input("Enter the imaginary part of the first complex number:", key="imag1", step=1.0)
real2 = st.number_input("Enter the real part of the second complex number:", key="real2", step=1.0)
imag2 = st.number_input("Enter the imaginary part of the second complex number:", key="imag2", step=1.0)
complex_operation = st.selectbox("Select an operation for complex numbers:", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate Complex Operation"):
    try:
        complex1 = complex(real1, imag1)
        complex2 = complex(real2, imag2)
        if complex_operation == "Addition":
            result = complex1 + complex2
        elif complex_operation == "Subtraction":
            result = complex1 - complex2
        elif complex_operation == "Multiplication":
            result = complex1 * complex2
        elif complex_operation == "Division":
            if complex2 != 0:
                result = complex1 / complex2
            else:
                result = "Error: Division by zero!"
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Section for GCD and LCM
st.header("GCD and LCM")
num_gcd_lcm1 = st.number_input("Enter the first number:", key="num_gcd_lcm1", step=1.0)
num_gcd_lcm2 = st.number_input("Enter the second number:", key="num_gcd_lcm2", step=1.0)
gcd_lcm_choice = st.radio("Select a function:", ["GCD", "LCM"])

if st.button("Calculate GCD/LCM"):
    try:
        a, b = int(num_gcd_lcm1), int(num_gcd_lcm2)
        if gcd_lcm_choice == "GCD":
            result = math.gcd(a, b)
        elif gcd_lcm_choice == "LCM":
            gcd = math.gcd(a, b)
            result = abs(a * b) // gcd
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
