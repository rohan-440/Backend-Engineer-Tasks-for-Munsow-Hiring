import json
import logging

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
    except Exception as e:
        logging.error(f"Error reading questions from file: {e}")
        return []

def write_questions_to_file(file_path, questions):
    try:
        with open(file_path, "w") as file:
            json.dump(questions, file, indent=2)
    except Exception as e:
        logging.error(f"Error writing questions to file: {e}")

def filter_questions(questions, difficulty_level=None, tags=None):
    filtered_questions = []

    for question in questions:
        if (
            (difficulty_level is not None and question["difficulty_level"] != difficulty_level)
            or (tags is not None and not set(question["tags"]).intersection(set(tags)))
        ):
            continue

        filtered_questions.append(question)

    return filtered_questions

def main():
    configure_logging()

    input_file = "input.json"
    output_file = "output.json"

    questions = read_questions_from_file(input_file)

    difficulty_level = "easy"
    tags = ["tag1"]

    filtered_questions = filter_questions(questions, difficulty_level, tags)

    write_questions_to_file(output_file, filtered_questions)

if __name__ == "__main__":
    main()