student_data = {
    "id1": {"name": "Alice", "age": 20, "major": "Computer Science"},
    "id2": {"name": "Bob", "age": 22, "major": "Mathematics"},
    "id3": {"name": "Charlie", "age": 21, "major": "Physics"},
    "id4": {"name": "Alice", "age": 20, "major": "Computer Science"},  # Duplicate entry
}

result = {}
seen_keys = {}
for student_id, student_info in student_data.items():
    unique_key = (student_info["name"], student_info["age"], student_info["major"])

    if unique_key not in seen_keys:
        seen_keys[unique_key] = student_id
        result[student_id] = student_info

for k, v in result.items():
    print(k, ":", v)