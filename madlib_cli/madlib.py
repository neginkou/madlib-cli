import re

def welcome_message():
    print("Welcome to the Mad World of Madlibs!")
    print("Please enter various words which will be used to fill out a story template.")

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def parse_template(template):
    parts = tuple(re.findall(r"\{(.*?)\}", template))
    stripped_template = re.sub(r"\{.*?\}", "{}", template)
    return stripped_template, parts

def merge(story_base, words):
    return story_base.format(*words)

def main():
    welcome_message()
    template_path = input("Enter the path to the Madlib template file: ")
    template = read_template(template_path)
    stripped_template, language_parts = parse_template(template)

    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)

    completed_madlib = merge(stripped_template, user_inputs)
    print("\nHere's your Madlib:")
    print(completed_madlib)

if __name__ == "__main__":
    main()
