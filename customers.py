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
