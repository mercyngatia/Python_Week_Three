# Calculate Discount Program

## 📌 Description

This Python program calculates the final price of an item after applying a discount.
If the discount percentage is **20% or more**, the program applies the discount.
If the discount is **less than 20%**, the program returns the original price without changes.

---

## 🚀 How It Works

1. **The `calculate_discount` function**

   * Takes two inputs:

     * `price` → the original price of the item
     * `discount_percent` → the discount percentage
   * If the discount is **≥ 20%**, it applies the discount.
   * Otherwise, it returns the original price.

2. **User Input**

   * The program asks the user to enter the original price and the discount percentage.

3. **Output**

   * Displays the original price, discount applied (if any), and final price.

---

## 🖥 Example Run

```
Enter original price of the item: 100
Enter the discount percentage: 25
You got a 25.0% discount applied!
Original price: 100.00
Final price: 75.00
```

```
Enter original price of the item: 100
Enter the discount percentage: 10
Discount not given (10.0% less than 20%), too small.
Original price: 100.00
```

---

## 📂 File Structure

```
calculate_discount.py   # Main program file
README.md               # Program documentation
```

---

## ▶ How to Run

1. Make sure you have **Python 3** installed.
2. Save the code as `calculate_discount.py`.
3. Run the program in a terminal:

```bash
python calculate_discount.py
```
