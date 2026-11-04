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
