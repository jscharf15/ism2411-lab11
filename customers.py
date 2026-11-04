# Self-Assessment Questions
# 1. I use .get() when a key might not be there, so my code does not crash.
# I use brackets when the key should be there, so I get an error if
# something is wrong. What I think is that I use .get() for maybe and brackets for must.
# 2. The Exercise 8 pattern reminds me of a PivotTable in Excel, which also groups
# rows by a category and totals them. The Python version is more useful for
# large datasets because a loop can process thousands of rows automatically
# and be rerun on new data without rebuilding anything by hand.

print("----- Exercise 1 -----")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("----- Exercise 2 -----")
customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

print("----- Exercise 3 -----")
# New version
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError Caught: {error}")

print("----- Exercise 4 -----")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items()
for item in customer:
    print(item)

# The difference is that looping over the dict directly gives only the keys, so each
# pass prints just 'name', 'tier', etc. Adding .items() gives both the
# key and its value on each pass, which lets me print "key: value" pairs.

print("----- Exercise 5 -----")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")

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

print("----- Exercise 7 -----")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")

print("----- Exercise 8 -----")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}

for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")