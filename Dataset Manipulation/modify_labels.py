#!/usr/bin/python

import os
import sys

"""
    Modifies label classes annotations in the "annotations_folder" according to the provided mapping and
    removes the line if the class number is not present in the mapping.
"""
def modify_labels(annotations_folder, mapping):
    
    for filename in os.listdir(annotations_folder):
        if filename.endswith(".txt"):  
            file_path = os.path.join(annotations_folder, filename)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()    # Read file content

            modified_lines = []
            for line in lines:
                s_line = line.strip().split()
                
                if len(s_line) > 0 and s_line[0] in mapping:
                   
                    s_line[0] = mapping[s_line[0]]      # Replace the label with the mapped value
                    modified_lines.append(" ".join(s_line))

            # Write the modified lines back to the original file
            with open(file_path, 'w') as file:
                file.write("\n".join(modified_lines) + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Insert the mapping to use.")
        sys.exit(1)

    annotations_folder = "labels"
    mapping_choice = sys.argv[1]

    # Define mappings
    mappings = {
        'og_to_n': {'2': '5', '4': '0', '0': '3', '9': '7'},  
        # Add mappings
    }

    if mapping_choice not in mappings:
        print(f"Invalid mapping choice.")
        sys.exit(1)

    selected_mapping = mappings[mapping_choice]
    modify_labels(annotations_folder, selected_mapping)
    print("Finished.")


