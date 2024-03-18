import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd

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

# Display scatter plot for different times
st.header('Graphical Comparison')

max_length = max(len(js_function_data), len(py_function_data))
js_times = list(js_function_data['Time']) + [None] * (max_length - len(js_function_data))
py_times = list(py_function_data['Time']) + [None] * (max_length - len(py_function_data))


# Create a DataFrame for the scatter plot
scatter_data = pd.DataFrame({
    'Run': range(1, max_length + 1),
    'JavaScript': js_times,
    'Python': py_times
})

# Create a scatter plot using matplotlib
fig, ax = plt.subplots()
ax.scatter(scatter_data['Run'], scatter_data['JavaScript'], color='b', label='JavaScript')
ax.scatter(scatter_data['Run'], scatter_data['Python'], color='r', label='Python')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel(f'{function} run')
ax.set_ylabel('Time (s)')
ax.set_title('Time by function and language')
ax.set_yscale('log')
ax.legend()

st.pyplot(fig)

st.header('Demonstration of the visualisation')
st.video('https://www.youtube.com/watch?v=oK0CTj7sJvo')