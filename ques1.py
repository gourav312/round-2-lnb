def calculate_performance(employees):
    # Initialize an empty list to store the results
    results = []

    # Iterate through each employee in the input list
    for employee in employees:
        name = employee["name"]
        scores = employee["scores"]
        weights = employee["weights"]

        # Initialize the total score for this employee
        total_score = 0

        # Calculate the weighted sum of scores for each criterion
        for criterion, score in scores.items():
            if criterion in weights:
                weight = weights[criterion]
                total_score += score * weight

        # Create a dictionary to store the result for this employee
        result = {
            "name": name,
            "performance_score": total_score
        }

        # Append the result to the results list
        results.append(result)

    return results
# Take user input for a list of employees
num_employees = int(input("Enter the number of employees: "))
employees = []

for i in range(num_employees):
    name = input(f"Enter the name of employee {i + 1}: ")
    scores = {}
    weights = {}

    num_criteria = int(input("Enter the number of criteria: "))
    for j in range(num_criteria):
        criterion_name = input(f"Enter the name of criterion {j + 1}: ")
        score = float(input(f"Enter the score for {criterion_name}: "))
        weight = float(input(f"Enter the weightage for {criterion_name}: "))

        scores[criterion_name] = score
        weights[criterion_name] = weight

    employee = {
        "name": name,
        "scores": scores,
        "weights": weights
    }

    employees.append(employee)

# Calculate and display the performance scores
performance_scores = calculate_performance(employees)
print("\nPerformance Scores:")
for score in performance_scores:
    print(f"Employee: {score['name']}, Performance Score: {score['performance_score']}")