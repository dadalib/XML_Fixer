#python fix_angles.py
import sys  # Imported for potential future use (e.g., CLI arguments)

# Define the input and output XML file paths
input_file = "input.xml"
output_file = "fixed.xml"

# Open the input XML file in read mode using UTF-8 encoding
# Read the entire file content into a string
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace escaped versions of HTML entities where the backslash
# was added before the entity (e.g. \&amp;lt; becomes &amp;lt;)
content = content.replace(r"\&amp;lt;", "&amp;lt;")
content = content.replace(r"\&amp;gt;", "&amp;gt;")

# Write the corrected XML content to the output file
# The file will be created or overwritten if it already exists
with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)