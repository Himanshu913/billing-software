# 🧾 Billing Software (Tkinter GUI)

A simple and user-friendly **Billing Software** built using **Python (Tkinter)**. This desktop application helps generate bills for **medical items, grocery items, and cold drinks**, with automatic calculations and bill storage.

---

## 🚀 Features

* 🛒 **Product Categories**

  * Medical Items
  * Grocery Items
  * Cold Drinks
* ➕ Quantity-based billing system
* 💰 Automatic total calculation
* 🧾 Clean and formatted bill generation
* 💾 Save bills locally as text files
* 🔍 Search and retrieve previous bills
* 🧹 Reset/Clear all inputs instantly
* ❌ Exit confirmation dialog

---

## 🖥️ Tech Stack

* **Language:** Python (3.x)
* **GUI Library:** Tkinter
* **Modules Used:**

  * `tkinter`
  * `random`
  * `os`

---

## 📂 Project Structure

```
Billing-Software/
│
├── bills/               # Auto-created folder for saved bills
├── billing_app.py       # Main application file
└── README.md            # Project documentation
```

---

## ⚙️ Getting Started

### ▶️ Run the Application

```bash
billing_app.py
```

> ⚠️ Make sure Python (3.x) is installed on your system.

---

## 🧑‍💻 How to Use

1. Enter **Customer Name** and **Phone Number**
2. Input item quantities in respective categories
3. Click **"Total"** to calculate cost
4. Click **"Generate Bill"** to view bill
5. Choose whether to **save the bill**
6. Use **Search** to find previous bills by bill number
7. Click **Clear** to reset all fields

---

## 🧾 Bill Storage

* Bills are saved automatically in the `bills/` folder
* Each bill is stored as a `.txt` file
* File name = **Bill Number** (e.g., `1234.txt`)

---

## ✨ Future Enhancements

* 📊 Add database support (SQLite/MySQL)
* 📄 Export bills as PDF
* 🔐 User authentication system
* 🎨 Improved UI/UX design
* 🛠️ Dynamic product management (add/remove items)

---

## 👨‍💻 Author

**Himanshu**

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## ❤️ Acknowledgement

Thank you for checking out this project!
If you like it, consider giving it a ⭐ on GitHub.
