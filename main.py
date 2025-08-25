print("\n")
intro = """
      ////////////////// HOE INVERTER CALCULATOR ///////////////////

      Hoe Inverter Calculator allows users to take smart budget decisions
      with precise costs and effort. In the times we live, where love is no more
      than an utopia, we need to take care of each other and provide the best
      defenses possible to fight the hoe inflation and loneliness.

      This program saves you time and money by:
      - Predicts probabilities of success
      - Included newest taxes due to hoe inflation
      - Strict control of the budget
"""
budget = 0
location = 0
fineness = 0
time = 0
skills = 0
hoe_inflation_tax = 40
dollar_cost = 1
print(intro)

while True:
    try:
        budget = float(input("\nEnter your budget (in dollars): $"))
        location = int(input("Enter location quality (1-10, where 10 is best): "))
        fineness = int(input("Enter desired fineness level (1-10): "))
        time = int(input("Enter available time (hours): "))
        skills = int(input("Enter your skills level (1-10): "))
    except ValueError:
        print("Please enter valid numbers!")
        continue
    
    base_cost = (fineness * 20) + (location * 15)
    
    skills_discount = skills * 2
    base_cost = max(base_cost - skills_discount, 10)
    
    if time < 5:
        time_multiplier = 1.5
    elif time < 10:
        time_multiplier = 1.2
    else:
        time_multiplier = 1.0
    
    total_cost = (base_cost * time_multiplier) + hoe_inflation_tax
    
    success_prob = min(90, (budget / total_cost * 30) + (skills * 5) + (time * 0.5))
    success_prob = max(5, success_prob) 
    
    print(f"\n{'='*50}")
    print("CALCULATION RESULTS:")
    print(f"{'='*50}")
    print(f"Estimated total cost: ${total_cost:.2f}")
    print(f"Your budget: ${budget:.2f}")
    print(f"Success probability: {success_prob:.1f}%")
    
    if budget >= total_cost:
        print("Budget is SUFFICIENT for this operation!")
        remaining = budget - total_cost
        print(f"Remaining funds: ${remaining:.2f}")
    else:
        deficit = total_cost - budget
        print("Budget is INSUFFICIENT!")
        print(f"Additional funds needed: ${deficit:.2f}")
    
    print(f"\n{'='*50}")
    choice = input("Would you like to perform another calculation? (yes/no):").lower()
    if choice not in ['yes', 'y']:
        print("\nThank you for using the Hoe Inverter Calculator!")
        print("Stay safe out there!")
        break

