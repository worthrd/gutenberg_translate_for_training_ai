import json
import os
import glob
import re

def numerical_sort(value):
    """
    Extracts the number from the filename for proper numerical sorting.
    e.g. chunk_2.json comes before chunk_10.json
    """
    numbers = re.findall(r'\d+', value)
    return int(numbers[0]) if numbers else value

def combine_json_to_jsonl(input_dir, output_file):
    # Get all json files in the directory
    json_files = glob.glob(os.path.join(input_dir, "*.json"))
    
    # Sort files numerically to respect chunk order
    try:
        json_files.sort(key=numerical_sort)
    except Exception as e:
        print(f"Warning: Could not sort numerically, falling back to lexicographical sort. Error: {e}")
        json_files.sort()

    print(f"Found {len(json_files)} JSON files in {input_dir}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in json_files:
            try:
                with open(filename, 'r', encoding='utf-8') as infile:
                    data = json.load(infile)
                    # Write the JSON object as a single line
                    json.dump(data, outfile, ensure_ascii=False)
                    outfile.write('\n')
            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"Successfully created {output_file} with {len(json_files)} lines.")

if __name__ == "__main__":
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(base_dir, "output")
    output_jsonl = os.path.join(input_folder, "merged.jsonl")

    # Ensure output directory exists (it should if we are reading from it)
    if not os.path.exists(input_folder):
        print(f"Error: Output directory '{input_folder}' does not exist.")
    else:
        combine_json_to_jsonl(input_folder, output_jsonl)
