# Week 2 Internship Client Project
# Program: Data Cleaning and Transformation
# Intern: Neha Beldar


# Function to read data from CSV
def read_data(file_path):
    data = []

    with open(file_path, "r") as file:
        next(file)  # skip header

        for line in file:
            parts = line.strip().split(",")

            if len(parts) < 2 or parts[1] == "":
                continue

            name = parts[0]
            score = int(parts[1])

            data.append((name, score))

    return data
    
    with open(file_path, "r") as file:
        next(file)  # Skip header
        
        for line in file:
            name, score = line.strip().split(",")
            data.append((name, int(score)))
    
    return data


# Function to remove duplicate records
def remove_duplicates(data):
    return list(set(data))


# Function to filter scores greater than 80
def filter_scores(data):
    return [item for item in data if item[1] > 80]


# Function to square scores
def square_scores(data):
    return [(name, score**2) for name, score in data]


# MAIN PROGRAM

file_path = "data/student_scores.csv"

data = read_data(file_path)

print("\nOriginal Data:")
print(data)

cleaned_data = remove_duplicates(data)
print("\nAfter Removing Duplicates:")
print(cleaned_data)

filtered_data = filter_scores(cleaned_data)
print("\nScores Greater Than 80:")
print(filtered_data)

squared_data = square_scores(filtered_data)
print("\nSquared Scores:")
print(squared_data)

print("\nData Cleaning Completed Successfully!")