def read_and_count_words(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the number of words
        word_count = len(content.split())

        # Write the result to the output file
        with open(output_file, 'w') as file:
            file.write(f'The number of words in the file "{input_file}" is: {word_count}\n')

        print(f"Word count has been written to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (for more testing change the text in input file accordingly)
input_file = 'C:/Users/siddh/OneDrive/Desktop/Git/AI-ML/Task 1/File Handling/example.txt' 
output_file = 'C:/Users/siddh/OneDrive/Desktop/Git/AI-ML/Task 1/File Handling/word_count_results.txt'  
read_and_count_words(input_file, output_file)
