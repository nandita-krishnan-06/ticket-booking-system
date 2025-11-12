# Customer Ticket Booking System (Python)

A customer support ticket management system implementing queue data structures with priority handling, built in Python.

## 🎯 Features

- **FIFO Queue Processing** - Tickets resolved in first-come-first-served order
- **Priority Handling** - VIP and Emergency tickets jump to the front of the queue
- **Complete CRUD Operations** - Create, Read, Update (Resolve), Delete (Cancel) tickets
- **Advanced Search** - Search tickets by ID or customer name (partial matching)
- **Real-time Statistics** - Dashboard showing pending/resolved counts and average resolution time
- **Sample Data** - Pre-loaded test tickets for immediate demonstration

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Installation & Usage

### Quick Start
```bash
# Clone or download the file
# Navigate to the directory
cd ticket-booking-system

# Run the program
python ticket_system.py
```

Or on some systems:
```bash
python3 ticket_system.py
```

### No Installation Required!
This project uses only Python's standard library:
- `datetime` - For timestamp tracking
- `collections.deque` - For efficient queue operations

## 💻 How to Use

### Main Menu
```
Menu Options:
1. Create Ticket
2. Resolve Ticket
3. Cancel Ticket
4. Search Ticket
5. View All Tickets
6. Dashboard
7. Exit
```

### 1. Create Ticket
Enter customer information and select priority level:
- **0 - Normal**: Standard FIFO processing
- **1 - VIP**: Jumps to front of queue
- **2 - Emergency**: Highest priority, processed first
```
Enter customer name: John Doe
Enter issue description: Cannot access dashboard
Select priority level:
0. Normal
1. VIP
2. Emergency
Enter priority (0-2): 1
```

### 2. Resolve Ticket
Processes the next ticket in queue (FIFO order with priority):
```
Ticket #3 resolved successfully!
Customer: Bob Johnson
Issue: System down - critical business impact
```

### 3. Cancel Ticket
Remove a pending ticket by ID:
```
Enter ticket ID to cancel: 5
Ticket #5 cancelled successfully!
```

### 4. Search Ticket
Search by ticket ID (exact match) or customer name (partial match):
```
Search by:
1. Ticket ID
2. Customer Name
Enter choice (1-2): 2
Enter customer name: John
```

### 5. View All Tickets
Displays all pending and resolved tickets with full details

### 6. Dashboard
Shows system statistics:
- Number of pending tickets
- Number of resolved tickets
- Average resolution time
- Breakdown by priority level

## 📊 Sample Output
```
=== STATISTICS DASHBOARD ===
Pending Tickets: 3
Resolved Tickets: 1
Total Tickets: 4
Average Resolution Time: 120.50 seconds

Pending Tickets by Priority:
Normal: 1
VIP: 1
Emergency: 1
```

## 🏗️ System Architecture

### Data Structures

**Queue (deque)**
```python
pending_queue = deque()  # O(1) append/appendleft/popleft operations
```

**Ticket Dictionary**
```python
ticket = {
    'id': 1,
    'name': 'John Doe',
    'issue': 'Login problem',
    'priority': VIP,
    'creation_time': datetime.now(),
    'resolution_time': None,
    'is_resolved': False
}
```

### Priority System

| Priority | Value | Behavior |
|----------|-------|----------|
| NORMAL | 0 | Added to rear (standard FIFO) |
| VIP | 1 | Added to front (immediate processing) |
| EMERGENCY | 2 | Added to front (highest priority) |


## 🔍 Code Structure
```python
# Global Variables
pending_queue = deque()      # Queue for pending tickets
resolved_tickets = []        # List of resolved tickets
next_ticket_id = 1          # Auto-incrementing ID counter

# Core Functions
create_ticket()             # Create new ticket
resolve_ticket()            # Resolve next ticket (FIFO)
cancel_ticket()             # Cancel ticket by ID
search_ticket()             # Search by ID or name
view_all_tickets()          # Display all tickets
dashboard()                 # Show statistics
print_ticket(ticket)        # Display ticket details
load_sample_data()          # Load test data
main()                      # Main program loop
```

## 📚 Key Concepts Demonstrated

### Data Structures
- **Deque (Double-ended Queue)** - Efficient O(1) operations on both ends
- **Dictionary** - Key-value storage for ticket attributes
- **List** - Dynamic array for resolved tickets

### Algorithms
- **FIFO Queue** - First-In-First-Out processing
- **Priority Queue** - Higher priority items processed first
- **Linear Search** - Search through unsorted data
- **String Matching** - Substring search with case-insensitive comparison


## 🎓 Learning Outcomes

This project demonstrates:
- Queue implementation and operations
- Deque behavior (insertion at both ends)
- FIFO (First-In-First-Out) processing
- Priority-based scheduling
- Time complexity analysis
- Search algorithms (linear search)
- Data persistence (in-memory)
- Statistical calculations (averages)
- User input validation
- Menu-driven program design

## 🔧 Customization

### Change Priority Values
```python
NORMAL = 0
VIP = 1
EMERGENCY = 2
CRITICAL = 3  # Add new priority level
```

### Modify Sample Data
Edit the `load_sample_data()` function to add/remove test tickets.

### Adjust Display Format
Modify the `print_ticket()` function to change how tickets are displayed.

## 🐛 Error Handling

The system handles:
- Invalid menu choices
- Invalid priority selections
- Non-numeric input for IDs
- Empty customer names/issues
- Operations on empty queues
- Non-existent ticket IDs

## 📝 Example Session
```
Customer Ticket Booking System
==================================================
Loading sample data...
Sample data loaded: 3 pending tickets, 1 resolved ticket

Menu Options:
1. Create Ticket
2. Resolve Ticket
3. Cancel Ticket
4. Search Ticket
5. View All Tickets
6. Dashboard
7. Exit
Enter your choice (1-7): 1

Creating new ticket...
Enter customer name: Alice Johnson
Enter issue description: Password reset needed

Select priority level:
0. Normal
1. VIP
2. Emergency
Enter priority (0-2): 0
Ticket #5 created successfully!

Menu Options:
1. Create Ticket
2. Resolve Ticket
3. Cancel Ticket
4. Search Ticket
5. View All Tickets
6. Dashboard
7. Exit
Enter your choice (1-7): 2

Ticket #3 resolved successfully!
Customer: Bob Johnson
Issue: System down - critical business impact
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

MIT License - Free to use for educational purposes

## 👨‍💻 Author

**Nandita Krishnan**
## 🙏 Acknowledgments

Built as a demonstration of queue data structures and ticket management systems for educational purposes.

---

**Happy Coding! 🐍**
