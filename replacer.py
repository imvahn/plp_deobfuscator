import re
import sys

# Function to convert a list of strings containing hexadecimal escape sequences to text
def escape_hex_to_text(hex_escape_codes, output_file):
    def replace_hex(match):
        """Replaces a match with the actual ASCII character."""
        hex_value = match.group(1)
        return chr(int(hex_value, 16))

    # Regular expression pattern to match hexadecimal escape sequences
    hex_pattern = re.compile(r'\\x([0-9A-Fa-f]{2})')

    text_list = []
    for hex_escape in hex_escape_codes:
        try:
            # Replace all hexadecimal escape sequences using the pattern
            decoded_string = hex_pattern.sub(replace_hex, hex_escape)
            text_list.append(decoded_string)
        except Exception as e:
            print(f"Error processing {hex_escape}: {e}")
            text_list.append("")

    # Write the modified script to a text file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(text_list))

    return text_list

def replace_references(script, variables, output_file):
    # Regular expression pattern to match _[index], ignoring references inside double quotes
    # Using negative lookahead and lookbehind to ignore if it is inside double quotes
    pattern = re.compile(r'(?<!")_\[(\d+)\](?!")')

    # Function to replace _[index] with the corresponding value from the `variables` list
    def replace_match(match):
        index = int(match.group(1))
        if index < len(variables):
            replacement = re.escape(variables[index])
            return replacement
        return match.group(0)  # If index is out of bounds, return original string

    # Replace all occurrences of the pattern with the corresponding variable
    replaced_script = pattern.sub(replace_match, script)

    # Write the modified script to a text file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(replaced_script)


if __name__=='__main__':

    # List of variables to replace
    hex_escape_codes_list = [] # Insert list here

    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} <input_file_path> <output_file_path> <list_output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    list_output_file_path = sys.argv[3]
                                
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            script_content = input_file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {input_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    converted_texts = escape_hex_to_text(hex_escape_codes_list, list_output_file_path)

    replace_references(script_content, hex_escape_codes_list, output_file_path)
   
    print(f"Modified list has been saved to {list_output_file_path}")
    print(f"Modified script has been saved to {output_file_path}")