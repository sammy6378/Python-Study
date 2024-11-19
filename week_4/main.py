# File Read & Write Program
try:
    # Ask the user for the input file name
    input_filename = input("Enter the input file name: ")
    
    # Open the input file in read mode
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
    
    # Modify the content
    modified_content = content.upper()
    
    # Ask for the output file name
    output_filename = input("Enter the output file name: ")
    
    # Write the modified content to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)
    
    print(f"Modified content has been written to {output_filename}.")
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError:
    print(f"Error: Could not read or write to the file.")
