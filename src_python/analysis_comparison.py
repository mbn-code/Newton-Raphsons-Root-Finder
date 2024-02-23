import difflib

# Assuming benchmark_data_javascript and benchmark_data_python are lists of strings
benchmark_data_javascript = [...]  # Your JavaScript data
benchmark_data_python = [...]  # Your Python data

# Convert the lists to strings
javascript_str = '\n'.join(benchmark_data_javascript)
python_str = '\n'.join(benchmark_data_python)

# Compare the strings
differ = difflib.Differ()
diff = differ.compare(javascript_str.splitlines(), python_str.splitlines())

# Print the differences
for line in diff:
    print(line)