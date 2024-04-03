from func import func

file = "operations.json"
data = func.load_operation(file)
sorted_data = func.date_time(data)

for transaction in sorted_data:
    print(f"{transaction['correct_date']} {transaction['description']}")
    print(func.from_to(transaction))
    print(func.sum_currency(transaction))
    print("\n")
