
# SmartSpend - Monthly Budget Planner

print("===== SMARTSPEND BUDGET PLANNER =====")

budget = float(input("Enter your monthly budget (UGX): "))
spent = float(input("Enter your total expenses so far (UGX): "))

remaining = budget - spent

print("\n===== BUDGET SUMMARY =====")
print(f"Monthly Budget: UGX {budget:,.0f}")
print(f"Total Spent: UGX {spent:,.0f}")
print(f"Remaining Balance: UGX {remaining:,.0f}")

if remaining > 0:
    print("Good job! You are still within your budget.")
elif remaining == 0:
    print("You have used your entire budget.")
else:
    print("Warning! You have exceeded your budget.")

print("Thank you for using SmartSpend!")
