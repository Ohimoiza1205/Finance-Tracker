import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import threading
import requests
import sqlite3


class FinanceTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Personal Finance Tracker")
        self.setGeometry(100, 100, 800, 600)

        # Layouts
        layout = QVBoxLayout()
        
        # Transaction Table
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)  # Date, Description, Amount, Category
        self.table_widget.setHorizontalHeaderLabels(["Date", "Description", "Amount", "Category"])
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.table_widget)

        # Add Transaction Section
        self.add_transaction_input = QLineEdit(self)
        self.add_transaction_input.setPlaceholderText("Add a new transaction (e.g. 2024-12-01 Groceries 50 Food)")
        layout.addWidget(self.add_transaction_input)

        self.add_button = QPushButton("Add Transaction", self)
        self.add_button.clicked.connect(self.add_transaction)
        layout.addWidget(self.add_button)

        # Graph Section for spending analysis
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Set up main widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize database
        self.setup_database()

        # Fetch real-time data (e.g., currency rates or stock prices) in background
        threading.Thread(target=self.fetch_real_time_data, daemon=True).start()

    def setup_database(self):
        """Set up SQLite database to store financial transactions."""
        self.db = sqlite3.connect("finance_tracker.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                description TEXT,
                amount REAL,
                category TEXT
            )
        """)
        self.db.commit()
        self.load_transactions()

    def load_transactions(self):
        """Load transactions from the database and populate the table."""
        self.cursor.execute("SELECT * FROM transactions")
        rows = self.cursor.fetchall()
        self.table_widget.setRowCount(0)
        for row in rows:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, value in enumerate(row[1:]):  # Exclude the ID column
                self.table_widget.setItem(row_position, col, QTableWidgetItem(str(value)))
        self.update_graph()

    def add_transaction(self):
        """Add a new transaction to the database."""
        transaction_text = self.add_transaction_input.text()

        # Check if the input is empty
        if not transaction_text:
            print("Error: Transaction input is empty")
            return

        # Split the input text into date, description, amount, category (e.g., "2024-12-01 Groceries 50 Food")
        parts = transaction_text.split()
        if len(parts) < 4:
            print("Error: Invalid input format. Expected format: Date Description Amount Category")
            return

        # Extract fields
        date, description, amount, category = parts[0], " ".join(parts[1:-2]), float(parts[-2]), parts[-1]

        # Insert the transaction into the database
        try:
            self.cursor.execute("INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)", 
                                (date, description, amount, category))
            self.db.commit()
            self.add_transaction_input.clear()
            self.load_transactions()
            print(f"Transaction added: {date} | {description} | {amount} | {category}")
        except Exception as e:
            print(f"Error adding transaction to database: {e}")

    def fetch_real_time_data(self):
        """Fetch real-time data (e.g., exchange rates or stock prices) using an API."""
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            if response.status_code == 200:
                data = response.json()
                rates = data["rates"]
                print("Real-time exchange rates:", rates)
        except Exception as e:
            print("Error fetching real-time data:", e)

    def update_graph(self):
        """Update the graph to show spending trends."""
        # Fetch data from the database
        self.cursor.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        data = self.cursor.fetchall()

        # Extract categories and amounts
        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]

        # Clear the previous plot
        ax = self.figure.add_subplot(111)
        ax.clear()

        # Plot the new data
        ax.bar(categories, amounts)
        ax.set_title("Spending by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")
        ax.set_xticks(range(len(categories)))  # Ensure correct x-axis labeling
        ax.set_xticklabels(categories, rotation=45, ha='right')  # Rotate labels for better visibility

        # Update the canvas
        self.canvas.draw()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinanceTrackerApp()
    window.show()
    sys.exit(app.exec_())
