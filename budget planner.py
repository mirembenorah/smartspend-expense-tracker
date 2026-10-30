
# SmartSpend - Monthly Budget Planner

print("===== SMARTSPEND BUDGET PLANNER =====")

budget = float(input("enter your monthly budget (UGX): "))
spent = float(input("enter your total expenses so far (UGX): "))

remaining = budget - spent

print("\n===== BUDGET SUMMARY =====")
print(f"monthly Budget: UGX {budget:,.0f}")
print(f"total Spent: UGX {spent:,.0f}")
print(f"remaining Balance: UGX {remaining:,.0f}")

if remaining > 0:
    print("Good Job! You are still within your budget.")
elif remaining == 0:
    print("You have used your entire budget.")
else:
    print("Warning! You have exceeded your budget.")

print("Thank you for using smartspend!")
