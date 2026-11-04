print("----- Exercise 1 -----")
customer = {
    "name": "Janice",
    "email": "janice@example.com",
    "tier": "diamond",
    "ytd_spend": 1500.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("----- Exercise 2 -----")
customer["phone"] = "555-0123"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

print("----- Exercise 3 -----")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as e:
    print("KeyError caught: the key", e, "does not exist")

print("----- Exercise 4 -----")
# ----- Exercise 4 -----
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items()
for item in customer:
    print(item)

# The difference is that looping over the dict directly gives only the keys, so each
# pass prints just 'name', 'tier', etc. Adding .items() gives both the
# key and its value on each pass, which lets me print "key: value" pairs.

print("----- Exercise 5 -----")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - discount_rate)

print("Tier:", tier)
print("Discount:", f"{discount_rate * 100:.0f}%")
print("Final price:", f"${final_price:.2f}")

print("----- Exercise 6 -----")
dict1 = {"name": "John", "tier": "silver", "ytd_spend": 640.00}
dict2 = {"name": "Bob", "tier": "gold", "ytd_spend": 1480.00}
dict3 = {"name": "Dave", "tier": "bronze", "ytd_spend": 120.00}

customers = [dict1, dict2, dict3]

purchase = 300

for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount: ${discount_amount:.2f}")