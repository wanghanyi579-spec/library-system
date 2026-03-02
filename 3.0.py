from datetime import datetime, timedelta
import json
import os
from collections import Counter

class Book:
    def __init__(self, isbn, title, author, year=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = False
        self.borrower_id = None
        self.borrow_date = None
        self.borrow_count = 0
    
    def __str__(self):
        status = "Available" if not self.borrowed else "Borrowed"
        return f"{self.title} - {self.author} [{self.isbn}] {status}"
    
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "borrowed": self.borrowed,
            "borrower_id": self.borrower_id,
            "borrow_date": self.borrow_date.isoformat() if self.borrow_date else None,
            "borrow_count": self.borrow_count
        }
       
    @classmethod
    def from_dict(cls, data):
        book = cls(data["isbn"], data["title"], data["author"], data["year"])
        book.borrowed = data["borrowed"]
        book.borrower_id = data["borrower_id"]
        book.borrow_date = datetime.fromisoformat(data["borrow_date"]) if data["borrow_date"] else None
        book.borrow_count = data.get("borrow_count", 0)
        return book

class Member:
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.borrowed_books = [] 
        self.register_date = datetime.now()

    def __str__(self):
        return f"Member[{self.member_id}]: {self.name} (Phone: {self.phone}), currently borrowing {len(self.borrowed_books)} books"
    
    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "phone": self.phone,
            "borrowed_books": self.borrowed_books,
            "register_date": self.register_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"], data["phone"])
        member.borrowed_books = data["borrowed_books"]
        member.register_date = datetime.fromisoformat(data["register_date"])
        return member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self._load_books()
        self._load_members()
        self.backup_file = "library_data.json"

    def _load_books(self):
        books_data = [
            ("978-7-02-000001-1", "The Old Man and the Sea", "Ernest Hemingway", 1952),
            ("978-7-02-000002-2", "Jane Eyre", "Charlotte Bronte", 1847),
            ("978-7-02-000003-3", "Anna Karenina", "Leo Tolstoy", 1877),
            ("978-7-02-000004-4", "The Red and the Black", "Stendhal", 1830),
            ("978-7-02-000005-5", "The Hunchback of Notre-Dame", "Victor Hugo", 1831),
        ]
        for isbn, title, author, year in books_data:
            self.books.append(Book(isbn, title, author, year))
        print("5 classic books loaded!")
    
    def add_book(self):
        print("\n--- Add Book ---")
        isbn = input("ISBN: ").strip()
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        year = input("Year (optional): ").strip()
        year = int(year) if year else None
        self.books.append(Book(isbn, title, author, year))
        print("Book added!")
    
    def delete_book(self):
        print("\n--- Delete Book ---")
        isbn = input("Enter ISBN to delete: ").strip()
        for book in self.books:
            if book.isbn == isbn:
                if book.borrowed:
                    print("Cannot delete: book is borrowed")
                    return
                self.books.remove(book)
                print("Book deleted!")
                return
        print("Book not found")
    
    def search_books(self):
        print("\n--- Search Books ---")
        keyword = input("Enter keyword: ").strip().lower()
        results = []
        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        if results:
            print(f"\nFound {len(results)} book(s):")
            for book in results:
                print(f"  - {book}")
        else:
            print("No books found")
    
    def list_books(self):
        print(f"\n--- All Books ({len(self.books)}) ---")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def _load_members(self):
        members_data = [
            ("M001", "Alice", "13800138000"),
            ("M002", "Bob", "13900139000")
        ]
        for mid, name, phone in members_data:
            self.members.append(Member(mid, name, phone))
        print("2 sample members loaded!")

    def _get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def _get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self):
        print("\n--- Borrow Book ---")
        member_id = input("Enter Member ID: ").strip()
        member = self._get_member_by_id(member_id)
        if not member:
            print("Member not found!")
            return
        
        isbn = input("Enter ISBN to borrow: ").strip()
        book = self._get_book_by_isbn(isbn)
        if not book:
            print("Book not found")
            return
        if book.borrowed:
            print("Book already borrowed")
            return
            
        book.borrow_count += 1
        book.borrowed = True
        book.borrower_id = member_id
        book.borrow_date = datetime.now()
        member.borrowed_books.append(isbn)
        
        print(f"Borrowed: {book}")
        print(f"Borrower: {member.name} ({member_id})")
        print(f"Borrow date: {book.borrow_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Due date: {(book.borrow_date + timedelta(days=14)).strftime('%Y-%m-%d')}")

    def return_book(self):
        print("\n--- Return Book ---")
        member_id = input("Enter Member ID: ").strip()
        member = self._get_member_by_id(member_id)
        if not member:
            print("Member not found!")
            return
        
        isbn = input("Enter ISBN to return: ").strip()
        book = self._get_book_by_isbn(isbn)
        if not book:
            print("Book not found")
            return
        if not book.borrowed:
            print("Book was not borrowed")
            return
        if book.borrower_id != member_id:
            print("This book is not borrowed by this member!")
            return
        
        return_date = datetime.now()
        overdue_days = (return_date - book.borrow_date).days - 14
        overdue_fee = max(0, overdue_days) * 0.5
        
        book.borrowed = False
        book.borrower_id = None
        book.borrow_date = None
        member.borrowed_books.remove(isbn)
        
        print(f"Returned: {book}")
        if overdue_days > 0:
            print(f"Overdue days: {overdue_days}")
            print(f"Overdue fee: ¥{overdue_fee:.2f}")
        else:
            print("No overdue fee!")

    def renew_book(self):
        print("\n--- Renew Book ---")
        member_id = input("Enter Member ID: ").strip()
        member = self._get_member_by_id(member_id)
        if not member:
            print("Member not found!")
            return
        
        isbn = input("Enter ISBN to renew: ").strip()
        book = self._get_book_by_isbn(isbn)
        if not book:
            print("Book not found")
            return
        if not book.borrowed or book.borrower_id != member_id:
            print("This book is not borrowed by this member!")
            return
        
        original_due_date = book.borrow_date + timedelta(days=14)
        book.borrow_date = datetime.now()
        new_due_date = book.borrow_date + timedelta(days=14)
        
        print(f"Renewed successfully: {book.title}")
        print(f"Original due date: {original_due_date.strftime('%Y-%m-%d')}")
        print(f"New due date: {new_due_date.strftime('%Y-%m-%d')}")

    def check_borrow_records(self):
        print("\n--- Check Borrow Records ---")
        print("1. By Member ID  2. By Book ISBN  3. All Borrowed Books")
        choice = input("Your choice (1-3): ").strip()
        
        if choice == '1':
            member_id = input("Enter Member ID: ").strip()
            member = self._get_member_by_id(member_id)
            if not member:
                print("Member not found!")
                return
            if not member.borrowed_books:
                print(f"{member.name} has no borrowed books!")
                return
            print(f"\nBorrowed books for {member.name}:")
            for isbn in member.borrowed_books:
                book = self._get_book_by_isbn(isbn)
                if book:
                    due_date = (book.borrow_date + timedelta(days=14)).strftime('%Y-%m-%d')
                    print(f"  - {book.title} (Due: {due_date})")
        
        elif choice == '2':
            isbn = input("Enter Book ISBN: ").strip()
            book = self._get_book_by_isbn(isbn)
            if not book:
                print("Book not found!")
                return
            if not book.borrowed:
                print(f"{book.title} is available!")
                return
            member = self._get_member_by_id(book.borrower_id)
            due_date = (book.borrow_date + timedelta(days=14)).strftime('%Y-%m-%d')
            print(f"\nBorrow info for {book.title}:")
            print(f"  Borrower: {member.name} ({member.member_id})")
            print(f"  Borrow date: {book.borrow_date.strftime('%Y-%m-%d')}")
            print(f"  Due date: {due_date}")
        
        elif choice == '3':
            borrowed_books = [b for b in self.books if b.borrowed]
            if not borrowed_books:
                print("No books are currently borrowed!")
                return
            print(f"\nAll borrowed books ({len(borrowed_books)}):")
            for book in borrowed_books:
                member = self._get_member_by_id(book.borrower_id)
                due_date = (book.borrow_date + timedelta(days=14)).strftime('%Y-%m-%d')
                print(f"  - {book.title} (Borrower: {member.name}, Due: {due_date})")
        else:
            print("Invalid choice!")

    def register_member(self):
        print("\n--- Register New Member ---")
        max_id = 0
        for member in self.members:
            if member.member_id.startswith("M"):
                try:
                    num = int(member.member_id[1:])
                    max_id = num if num > max_id else max_id
                except:
                    pass
        new_member_id = f"M{max_id + 1:03d}"
        
        name = input("Enter member name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return
        phone = input("Enter member phone: ").strip()
        if not phone:
            print("Phone cannot be empty!")
            return

        for member in self.members:
            if member.phone == phone:
                print("Phone number already registered!")
                return
        
        new_member = Member(new_member_id, name, phone)
        self.members.append(new_member)
        print(f"Member registered! ID: {new_member_id}")

    def delete_member(self):
        print("\n--- Delete Member ---")
        member_id = input("Enter Member ID to delete: ").strip()
        member = self._get_member_by_id(member_id)
        
        if not member:
            print("Member not found!")
            return
        
        if member.borrowed_books:
            print(f"Cannot delete: {member.name} has {len(member.borrowed_books)} borrowed books!")
            return
        
        self.members.remove(member)
        print(f"Member {member_id} deleted successfully!")

    def update_member_info(self):
        print("\n--- Update Member Info ---")
        member_id = input("Enter Member ID: ").strip()
        member = self._get_member_by_id(member_id)
        
        if not member:
            print("Member not found!")
            return
        
        print(f"\nCurrent info: Name={member.name}, Phone={member.phone}")
        print("1. Update Name  2. Update Phone  3. Cancel")
        choice = input("Choice (1-3): ").strip()
        
        if choice == '1':
            new_name = input("New name: ").strip()
            if new_name:
                member.name = new_name
                print("Name updated!")
        elif choice == '2':
            new_phone = input("New phone: ").strip()
            if not new_phone:
                print("Phone cannot be empty!")
                return
            for m in self.members:
                if m.member_id != member_id and m.phone == new_phone:
                    print("Phone already registered!")
                    return
            member.phone = new_phone
            print("Phone updated!")

    def list_members(self):
        print(f"\n--- All Members ({len(self.members)}) ---")
        if not self.members:
            print("No members!")
            return
        for i, member in enumerate(self.members, 1):
            reg_date = member.register_date.strftime('%Y-%m-%d')
            print(f"{i}. {member} | Register: {reg_date}")

    def show_borrow_ranking(self):
        print("\n--- Book Borrow Ranking ---")
        ranked_books = sorted(self.books, key=lambda x: x.borrow_count, reverse=True)
        
        if all(book.borrow_count == 0 for book in ranked_books):
            print("No borrow records!")
            return
        
        print(f"{'Rank':<5} {'Title':<30} {'Borrow Count':<10}")
        print("-" * 50)
        for rank, book in enumerate(ranked_books, 1):
            if book.borrow_count == 0:
                break
            print(f"{rank:<5} {book.title:<30} {book.borrow_count:<10}")

    def show_system_stats(self):
        print("\n--- System Statistics ---")
        total_books = len(self.books)
        borrowed_books = len([b for b in self.books if b.borrowed])
        total_members = len(self.members)
        active_members = len([m for m in self.members if m.borrowed_books])
        total_borrows = sum([b.borrow_count for b in self.books])
        
        print(f"📚 Books: Total={total_books}, Borrowed={borrowed_books}")
        print(f"👥 Members: Total={total_members}, Active={active_members}")
        print(f"📖 Total borrow times: {total_borrows}")

    def backup_data(self):
        print("\n--- Backup Data ---")
        backup_data = {
            "backup_time": datetime.now().isoformat(),
            "books": [book.to_dict() for book in self.books],
            "members": [member.to_dict() for member in self.members]
        }
        try:
            with open(self.backup_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)
            print(f"Backup saved to {self.backup_file}")
        except Exception as e:
            print(f"Backup failed: {e}") 

    def restore_data(self):
        print("\n--- Restore Data ---")
        if not os.path.exists(self.backup_file):
            print(f"Backup file {self.backup_file} not found!")
            return
        
        confirm = input("Overwrite current data? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Restore cancelled.")
            return
        
        try:
            with open(self.backup_file, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            self.books = [Book.from_dict(bd) for bd in backup_data["books"]]
            self.members = [Member.from_dict(md) for md in backup_data["members"]]
            print(f"Restored: {len(self.books)} books, {len(self.members)} members")
        except Exception as e:
            print(f"Restore failed: {e}")

    def show_main_menu(self):
        print("\n" + "="*60)
        print("🎯 LIBRARY MANAGEMENT SYSTEM")
        print("="*60)
        print("📚 BOOK MANAGEMENT")
        print("  1. Add Book        2. Delete Book")
        print("  3. Search Books    4. List All Books")
        print("\n👥 MEMBER MANAGEMENT")
        print("  5. Register Member  6. Delete Member")
        print("  7. Update Member    8. List All Members")
        print("\n📖 BORROW OPERATIONS")
        print("  9. Borrow Book    10. Return Book")
        print("  11. Renew Book     12. Check Borrow Records")
        print("\n📊 STATISTICS & BACKUP")
        print("  13. Borrow Ranking  14. System Statistics")
        print("  15. Backup Data     16. Restore Data")
        print("\n  0. Exit")
        print("="*60)
   
    def run(self):
        while True:
            self.show_main_menu()
            choice = input("\nChoice(0-16): ").strip()
            
            if choice == '0':
                print("Goodbye!")
                break
            elif choice == '1':
                self.add_book()
            elif choice == '2':
                self.delete_book()
            elif choice == '3':
                self.search_books()
            elif choice == '4':
                self.list_books()
            elif choice == '5': 
                self.register_member()
            elif choice == '6': 
                self.delete_member()
            elif choice == '7':
                 self.update_member_info()
            elif choice == '8':
                 self.list_members()
            elif choice == '9': 
                self.borrow_book()
            elif choice == '10': 
                self.return_book()
            elif choice == '11': 
                self.renew_book()
            elif choice == '12': 
                self.check_borrow_records()
            elif choice == '13': 
                self.show_borrow_ranking()
            elif choice == '14': 
                self.show_system_stats()
            elif choice == '15': 
                self.backup_data()
            elif choice == '16': 
                self.restore_data() 
            else:
                print("Invalid choice")

if __name__ == "__main__":
    library = Library()
    library.run()