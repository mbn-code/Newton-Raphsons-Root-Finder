import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Benchmark Data Analysis')

st.image('polynomium_of_third_degree.png', use_column_width=True)

# Text
st.write("This application allows you to analyze and compare benchmark data.")

# Load data
js_data = pd.read_excel('src_python/benchmark_data_python.xlsx')
py_data = pd.read_excel('src_python/benchmark_data_javascript.xlsx')

# Display data
st.header('JavaScript Benchmark Data')
st.dataframe(js_data, use_container_width=True)

st.header('Python Benchmark Data')
st.dataframe(py_data, use_container_width=True)

# Analysis
st.header('Analysis')
st.image('newton-raphson-algoritme-hastighed-javascript.png')
st.write("Here you can analyze and compare the benchmark data.")

# Select function to compare
function = st.selectbox('Select a function to compare', js_data['Function'].unique())

# Filter data
js_function_data = js_data[js_data['Function'] == function]
py_function_data = py_data[py_data['Function'] == function]

# Display comparison
st.header('Comparison')
st.write(f"Average time for {function} in JavaScript: {js_function_data['Time'].mean()} seconds")
st.write(f"Average time for {function} in Python: {py_function_data['Time'].mean()} seconds")

js_times = js_function_data['Time'].values
py_times = py_function_data['Time'].values
max_length = max(len(js_times), len(py_times))

# Display scatter plot for different times
st.header('Graphical Comparison')

scatter_data = pd.DataFrame({
    'JavaScript Time': np.log(js_times),
    'Python Time': np.log(py_times),
}, index=range(1, max_length + 1))

st.line_chart(scatter_data)

st.header('Demonstration of the visualisation')
st.video('https://www.youtube.com/watch?v=oK0CTj7sJvo')