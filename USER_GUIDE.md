```markdown
# Library Management System - User Guide

## 1. System Overview

The Library Management System is a command-line application that helps librarians manage book inventory, members, borrowing operations, and overdue fee calculation.

## 2. Requirements

- Python 3.7 or higher
- No external libraries required (uses only Python Standard Library)

## 3. How to Run

```bash
python system.py
```

Or:

```bash
python3 system.py
```

## 4. Main Menu

```
==================================================
LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Delete Book
3. Search Books
4. List All Books
5. Borrow Book
6. Return Book
7. Renew Book
8. Check Borrow Records
0. Exit

Choice:
```

## 5. Pre-loaded Members

| Member ID | Name | Phone |
|-----------|------|-------|
| M001 | Alice | 13800138000 |
| M002 | Bob | 13900139000 |

## 6. Features

### 6.1 Add Book (Option 1)

Enter ISBN, title, author, and year (optional).

### 6.2 Delete Book (Option 2)

Enter ISBN to delete. Cannot delete a borrowed book.

### 6.3 Search Books (Option 3)

Enter keyword to search by title or author.

### 6.4 List All Books (Option 4)

Display all books with status (Available/Borrowed).

### 6.5 Borrow Book (Option 5)

1. Enter Member ID
2. Enter ISBN
- Borrowing period: 14 days

### 6.6 Return Book (Option 6)

1. Enter Member ID
2. Enter ISBN
- Overdue fee: HKD 0.5 per day after 14 days

### 6.7 Renew Book (Option 7)

1. Enter Member ID
2. Enter ISBN
- Resets due date to 14 days from renewal

### 6.8 Check Borrow Records (Option 8)

Choose from:
- 1: View by Member ID
- 2: View by Book ISBN
- 3: View all borrowed books

### 6.9 Exit (Option 0)

Exit the program.

## 7. Important Notes

- No duplicate ISBN checking
- No member registration (use M001 or M002 only)
- Data is NOT saved after exit
- Minimal input validation
