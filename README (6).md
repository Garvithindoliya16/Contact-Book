
# 📒 Contact Book (Command-Line Application)

A simple yet powerful **Python-based Contact Book** that allows users to **add**, **view**, **search**, **update**, and **delete** contacts directly from the terminal — with a **colorful interface powered by Colorama**.  

---

## 🚀 Features

✅ Add new contacts with name, phone number, and email  
✅ Prevent duplicate contacts (by name or phone number)  
✅ Validate phone numbers (must be 10 digits)  
✅ Update or delete existing contacts  
✅ Confirmation before deletion  
✅ View all contacts in alphabetical order  
✅ Color-coded and user-friendly interface (using **Colorama**)  

---

## 🧩 Tech Stack

- **Language:** Python 3  
- **Library:** [Colorama](https://pypi.org/project/colorama/)  
- **Regex:** Used for phone number validation  

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/contact-book.git
   cd contact-book
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python contact_book.py
   ```

---

## 📁 File Structure

```
contact-book/
│
├── contact_book.py      # Main application file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧠 How to Use

1. Run the program in your terminal.  
2. Choose an option from the menu:
   - **1:** Add a new contact  
   - **2:** View all saved contacts  
   - **3:** Search for a contact  
   - **4:** Update an existing contact  
   - **5:** Delete a contact  
   - **6:** Exit the program  

3. Follow on-screen prompts.  
4. All messages and warnings are **color-coded** for easy recognition.

---

## 🎨 Color Scheme

| Color | Purpose |
|--------|----------|
| 🟢 Green | Success messages |
| 🔴 Red | Errors, invalid inputs, and warnings |
| 🟡 Yellow | Prompts, updates, and alerts |
| 🔵 Blue | Titles and headers |
| 🟣 Magenta | Main menu |

---

## 📘 Example Output

```
===== CONTACT BOOK MENU =====

1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice (1-6): 1
Enter Name: John Doe
Enter Phone Number: 9876543210
Enter Email (optional): john@example.com
✅ Contact 'John Doe' added successfully!
```

---

## ⚙️ Requirements File

**requirements.txt**
```
colorama
```

---

## 💡 Future Enhancements

- Add password protection before opening the menu  
- Export contacts to CSV or JSON  
- Import contacts from existing files  
- Add search filters (by email, name initials, etc.)  

---

## 🧑‍💻 Author

**Garvit Hindoliya**  
📍 Built with ❤️ using Python and Colorama  
🔗 [GitHub Profile](https://github.com/garvithindoliya16)
