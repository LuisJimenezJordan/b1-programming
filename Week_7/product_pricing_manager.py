base_product_data = []   # data from the input file stored here

category_discounts = {   # setting up the associated discount values for each category type
    "Electronics": 0.10,
    "Clothing": 0.15,
    "Books": 0.05,
    "Home": 0.12
}

tier_discounts = {      # and here for each associated tier type
    "Premium": 0.05,
    "Standard": 0.00,
    "Budget": 0.02
}

# Read product data from file
try:
    with open("products.txt", "r") as f:
        for line in f:
            line = line.strip()  # removes whitespace from either end of a string
            if not line:
                continue  # skips lines if they are empty
            try:
                product, base_price, category, tier = line.split(",")
                base_price = float(base_price)

                base_product_data.append({
                    "product": product,
                    "base_price": base_price,
                    "category": category,
                    "tier": tier
                })

            except ValueError:
                print(f"Error: Incorrect data format in line: {line}")
                
except FileNotFoundError:
    print("Error: File 'products.txt' not found.")
    exit()

# Calculate discounts for each product
discounted_products = []
total_discount_sum = 0  # Sum of all discount percentages for averaging

for product in base_product_data:
    base_price = product["base_price"]
    category = product["category"]
    tier = product["tier"]

    # Get discount percentages
    cat_discount = category_discounts.get(category, 0)
    tier_discount = tier_discounts.get(tier, 0)
    total_discount_pct = cat_discount + tier_discount
    
    # Track sum for average calculation
    total_discount_sum += total_discount_pct
    
    # Calculate discount amount and final price
    discount_amount = base_price * total_discount_pct
    final_price = base_price - discount_amount

    discounted_products.append({
        "product": product["product"],
        "base_price": base_price,
        "category": category,
        "tier": tier,
        "discount_pct": total_discount_pct * 100,  # Convert to percentage
        "discount_amount": discount_amount,
        "final_price": final_price
    })

# Calculate average discount
avg_discount = (total_discount_sum / len(discounted_products) * 100) if discounted_products else 0

# Generate pricing report
try:
    with open("pricing_report.txt", 'w') as f:
        f.write("=" * 130 + "\n")
        f.write("PRICING REPORT\n")
        f.write("=" * 130 + "\n\n")
        
        # Header row
        f.write(f"{'Product Name':<30} {'Base Price':<15} {'Category':<15} {'Tier':<12} {'Discount %':<15} {'Discount $':<15} {'Final Price':<15}\n")
        f.write("-" * 130 + "\n")
        
        # Product rows
        for product in discounted_products:
            f.write(
                f"{product['product']:<30} "
                f"${product['base_price']:<14.2f} "
                f"{product['category']:<15} "
                f"{product['tier']:<12} "
                f"{product['discount_pct']:<14.1f}% "
                f"${product['discount_amount']:<14.2f} "
                f"${product['final_price']:<14.2f}\n"
            )
        
        f.write("\n" + "=" * 130 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 130 + "\n")
        f.write(f"Total Products Processed: {len(discounted_products)}\n")
        f.write(f"Average Discount Applied: {avg_discount:.2f}%\n")
        f.write("=" * 130 + "\n")
    
    print("✓ Pricing report successfully generated: pricing_report.txt")
    
except PermissionError:
    print("Error: Permission denied. Cannot write to 'pricing_report.txt'")

# Console summary
print("\n" + "=" * 90)
print("PRICING REPORT: QUICK SUMMARY")
print("=" * 90)
print(f"Total Products Processed: {len(discounted_products)}")
print(f"Average Discount Applied: {avg_discount:.2f}%")
print("=" * 90)