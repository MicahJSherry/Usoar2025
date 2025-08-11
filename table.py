import subprocess
import os
import shutil

# 1. Define the full LaTeX document with your table.
#    Note: This is a full document, not just the tabular environment.
latex_document = r'''
\documentclass[preview]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{array}
\usepackage{booktabs}
\usepackage{caption}

\begin{document}
\begin{tabular}{|l|l|l|}
\hline
n & $f_n(x)$ & Factorizations \\
\hline
2 & $x^2 + x + 1$ & $(x + 1)^2$ \\
\hline
3 & $x^3 + x^2 + x + 1$ & $(x + 1)^3$ \\
& & $(x + 1)(x^2 + 1)$ \\
\hline
4 & $x^4 + x^3 + x^2 + x + 1$ & $(x + 1)^4$ \\
& & $(x + 1)^2(x^2 + 1)$ \\
& & $(x^3 + x + 1)(x + 1)$ \\
& & $(x + 1)(x^3 + x^2 + 1)$ \\
\hline
5 & $x^5 + x^4 + x^3 + x^2 + x + 1$ & $(x + 1)^5$ \\
& & $(x + 1)^3(x^2 + 1)$ \\
& & $(x^3 + x + 1)(x + 1)^2$ \\
& & $(x + 1)^2(x^3 + x^2 + 1)$ \\
& & $(x + 1)(x^2 + 1)^2$ \\
& & $(x + 1)(x^4 + x^2 + x + 1)$ \\
& & $(x^3 + 1)(x + 1)^2$ \\
& & $(x + 1)(x^4 + x^3 + x^2 + 1)$ \\
\hline
\end{tabular}
\end{document}
'''

# 2. Write the LaTeX document to a temporary file
with open('temp_table.tex', 'w') as f:
    f.write(latex_document)

# 3. Compile the .tex file to a PDF using pdflatex
#    -nonstopmode prevents pdflatex from stopping on errors
#    -output-directory tells pdflatex where to save the output files
try:
    subprocess.run(
        ['pdflatex', '-nonstopmode', 'temp_table.tex'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print("PDF compilation successful.")
except subprocess.CalledProcessError as e:
    print("LaTeX compilation failed.")
    print("STDOUT:", e.stdout.decode())
    print("STDERR:", e.stderr.decode())
    exit()

# 4. Convert the PDF to a high-resolution PNG
try:
    # Use convert from ImageMagick to convert the PDF to a high-resolution PNG
    subprocess.run(
        ['convert', '-density', '300', 'temp_table.pdf', 'high_resolution_table.png'],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print("PDF to PNG conversion successful.")
except subprocess.CalledProcessError as e:
    print("Conversion failed. Make sure ImageMagick is installed.")
    print("STDOUT:", e.stdout.decode())
    print("STDERR:", e.stderr.decode())
    exit()

# 5. Clean up temporary files
temp_files = ['temp_table.tex', 'temp_table.pdf', 'temp_table.log', 'temp_table.aux']
for file in temp_files:
    if os.path.exists(file):
        os.remove(file)

print("Generated high_resolution_table.png successfully!")