import json
import logging
import os

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )

def read_questions_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in file {file_path}: {e}")
        return []

def write_questions_to_file(file_path, questions):
    try:
        with open(file_path, "w") as file:
            json.dump(questions, file, indent=2)
        logging.info(f"Questions written to {file_path}")
    except Exception as e:
        logging.error(f"Error writing questions to file: {e}")

def filter_questions(questions, difficulty_level=None, tags=None):
    filtered_questions = []

    for question in questions:
        # Check if difficulty_level and tags match
        if (difficulty_level is None or question.get("difficulty_level") == difficulty_level) \
                and (tags is None or set(question.get("tags", [])).intersection(set(tags))):
            filtered_questions.append(question)

    return filtered_questions



def main():
    configure_logging()

    # Print current working directory
    logging.info("Current working directory: %s", os.getcwd())

    input_file = "input.json"
    output_file = "output.json"

    questions = read_questions_from_file(input_file)
    level = input("Enter the level: (easy/medium/hard) ")
    difficulty_level = level.strip()
    tags = ["tag1"]

    filtered_questions = filter_questions(questions, difficulty_level, tags)
    
    if filtered_questions:
        write_questions_to_file(output_file, filtered_questions)
        logging.info("Your set of questions is in the output JSON file.")
    else:
        logging.warning("No questions found matching the criteria.")

if __name__ == "__main__":
    main()
