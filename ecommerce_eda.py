import pandas as pd
from pathlib import Path

# Search for the customers CSV automatically
matches = list(Path.home().rglob("olist_customers_dataset.csv"))

print("Searching for customers dataset...")

if len(matches) == 0:
    print("❌ Customers CSV was not found.")
else:
    file_path = matches[0]

    print("✅ File found:")
    print(file_path)

    customers = pd.read_csv(file_path)

    print("\n✅ Customers dataset loaded successfully!")
    print("\nFirst 5 rows:")
    print(customers.head())

    print("\nShape:")
    print(customers.shape)