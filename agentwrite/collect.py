#!/usr/bin/env python3
import json

# Load the write.jsonl file
file_path = 'write.jsonl'

with open(file_path, 'r', encoding='utf-8') as f:
    # Read the first line (assuming you want the first document)
    line = f.readline()
    data = json.loads(line)

# Extract the 'write' content
write_sections = data.get('write', [])

# Concatenate all sections with double newlines between them
full_text = "\n\n".join(write_sections)

# Write to a new file
output_file = 'final_output.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Final text has been written to {output_file}")