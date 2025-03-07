# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

exchange_rate = 0.91
eur_amount = shipping_cost * exchange_rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
print(f"Shipping Cost in EUR is : {shipping_cost} EUR")
