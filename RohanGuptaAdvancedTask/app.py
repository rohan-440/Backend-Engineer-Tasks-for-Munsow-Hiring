questions = [
    {
        "text": "Can you explain the concept of inheritance in object-oriented programming?",
        "role": "software engineer",
        "level": "junior"
    },
    {
        "text": "How would you design a scalable microservices architecture?",
        "role": "software engineer",
        "level": "senior"
    },
    {
        "text": "What is your experience with cloud computing platforms like AWS or GCP?",
        "role": "devops engineer",
        "level": "intermediate"
    },
    {
        "text": "Explain the difference between HTTP and HTTPS protocols.",
        "role": "software engineer",
        "level": "junior"
    },
    {
        "text": "What are some common design patterns used in software development?",
        "role": "software engineer",
        "level": "senior"
    },
    {
        "text": "How do you ensure high availability in a distributed system?",
        "role": "devops engineer",
        "level": "senior"
    },
    {
        "text": "Describe the CAP theorem and its implications in distributed systems.",
        "role": "devops engineer",
        "level": "senior"
    },
    {
        "text": "What are the advantages and disadvantages of using containerization?",
        "role": "devops engineer",
        "level": "intermediate"
    },
    {
        "text": "Explain the concept of virtualization in cloud computing.",
        "role": "devops engineer",
        "level": "intermediate"
    }
]



def recommend_questions(role, level, tags=None, difficulty=None):
    role = role.lower()
    level = level.lower()
    relevant_questions = [q for q in questions if q["role"] == role and q["level"] == level]

    if tags:
        for tag in tags:
            relevant_questions = [q for q in relevant_questions if tag in q["text"]]

    if difficulty is not None:
        if difficulty == "easy":
            relevant_questions = [q for q in relevant_questions if "easy" in q["text"]]
        elif difficulty == "hard":
            relevant_questions = [q for q in relevant_questions if "hard" in q["text"]]

    return [q["text"] for q in relevant_questions]

candidate_role = input("Enter your role : ")
candidate_level = input("Enter your level (junior, intermediate, senior) : ")
questions = recommend_questions(candidate_role, candidate_level)
print("Recommended Questions Are : ")
for question in questions:
    print(question)

