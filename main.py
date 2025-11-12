from datetime import datetime
from collections import deque

# Priority constants
NORMAL = 0
VIP = 1
EMERGENCY = 2

# Global variables
pending_queue = deque()
resolved_tickets = []
next_ticket_id = 1


def create_ticket():
    """Create a new support ticket"""
    global next_ticket_id
    
    print("\nCreating new ticket...")
    
    # Get customer details
    name = input("Enter customer name: ").strip()
    if not name:
        print("Error: Name cannot be empty")
        return
    
    issue = input("Enter issue description: ").strip()
    if not issue:
        print("Error: Issue cannot be empty")
        return
    
    # Get priority
    print("\nSelect priority level:")
    print("0. Normal")
    print("1. VIP")
    print("2. Emergency")
    
    try:
        priority = int(input("Enter priority (0-2): "))
        if priority not in [0, 1, 2]:
            print("Invalid priority. Setting to Normal.")
            priority = NORMAL
    except ValueError:
        print("Invalid input. Setting to Normal.")
        priority = NORMAL
    
    # Create ticket dictionary
    ticket = {
        'id': next_ticket_id,
        'name': name,
        'issue': issue,
        'priority': priority,
        'creation_time': datetime.now(),
        'resolution_time': None,
        'is_resolved': False
    }
    
    next_ticket_id += 1
    
    # Enqueue based on priority
    if priority == VIP or priority == EMERGENCY:
        pending_queue.appendleft(ticket)  # Add to front (deque behavior)
    else:
        pending_queue.append(ticket)  # Add to rear (FIFO)
    
    print(f"Ticket #{ticket['id']} created successfully!")


def resolve_ticket():
    """Resolve the next pending ticket (FIFO)"""
    if not pending_queue:
        print("No pending tickets to resolve.")
        return
    
    ticket = pending_queue.popleft()  # Remove from front
    ticket['resolution_time'] = datetime.now()
    ticket['is_resolved'] = True
    
    resolved_tickets.append(ticket)
    
    print(f"\nTicket #{ticket['id']} resolved successfully!")
    print(f"Customer: {ticket['name']}")
    print(f"Issue: {ticket['issue']}")


def cancel_ticket():
    """Cancel a pending ticket by ID"""
    if not pending_queue:
        print("No pending tickets to cancel.")
        return
    
    try:
        ticket_id = int(input("Enter ticket ID to cancel: "))
    except ValueError:
        print("Invalid input.")
        return
    
    # Search and remove from queue
    for i, ticket in enumerate(pending_queue):
        if ticket['id'] == ticket_id:
            del pending_queue[i]
            print(f"Ticket #{ticket_id} cancelled successfully!")
            return
    
    print(f"Ticket #{ticket_id} not found in pending queue.")


def search_ticket():
    """Search for tickets by ID or name"""
    print("\nSearch by:")
    print("1. Ticket ID")
    print("2. Customer Name")
    
    try:
        choice = int(input("Enter choice (1-2): "))
    except ValueError:
        print("Invalid input.")
        return
    
    if choice == 1:
        # Search by ID
        try:
            ticket_id = int(input("Enter ticket ID: "))
        except ValueError:
            print("Invalid input.")
            return
        
        found = False
        
        # Search in pending tickets
        for ticket in pending_queue:
            if ticket['id'] == ticket_id:
                print("\nTicket found in pending queue:")
                print_ticket(ticket)
                found = True
                break
        
        # Search in resolved tickets
        for ticket in resolved_tickets:
            if ticket['id'] == ticket_id:
                print("\nTicket found in resolved tickets:")
                print_ticket(ticket)
                found = True
                break
        
        if not found:
            print(f"Ticket #{ticket_id} not found.")
    
    elif choice == 2:
        # Search by name
        name = input("Enter customer name: ").strip()
        print(f"\nSearching for tickets by customer: {name}")
        
        found = False
        
        # Search in pending tickets
        pending_matches = [t for t in pending_queue if name.lower() in t['name'].lower()]
        if pending_matches:
            print("\nPending tickets:")
            print("=" * 50)
            for ticket in pending_matches:
                print_ticket(ticket)
            found = True
        
        # Search in resolved tickets
        resolved_matches = [t for t in resolved_tickets if name.lower() in t['name'].lower()]
        if resolved_matches:
            print("\nResolved tickets:")
            print("=" * 50)
            for ticket in resolved_matches:
                print_ticket(ticket)
            found = True
        
        if not found:
            print(f"No tickets found for customer: {name}")
    
    else:
        print("Invalid choice.")


def view_all_tickets():
    """Display all pending and resolved tickets"""
    print("\n=== ALL TICKETS ===")
    
    # Display pending tickets
    print(f"\nPending Tickets ({len(pending_queue)}):")
    print("=" * 50)
    
    if not pending_queue:
        print("No pending tickets.")
    else:
        for ticket in pending_queue:
            print_ticket(ticket)
    
    # Display resolved tickets
    print(f"\nResolved Tickets ({len(resolved_tickets)}):")
    print("=" * 50)
    
    if not resolved_tickets:
        print("No resolved tickets.")
    else:
        for ticket in resolved_tickets:
            print_ticket(ticket)


def dashboard():
    """Display statistics dashboard"""
    print("\n=== STATISTICS DASHBOARD ===")
    print(f"Pending Tickets: {len(pending_queue)}")
    print(f"Resolved Tickets: {len(resolved_tickets)}")
    print(f"Total Tickets: {len(pending_queue) + len(resolved_tickets)}")
    
    # Calculate average resolution time
    if resolved_tickets:
        total_time = 0
        for ticket in resolved_tickets:
            if ticket['resolution_time']:
                delta = ticket['resolution_time'] - ticket['creation_time']
                total_time += delta.total_seconds()
        
        avg_time = total_time / len(resolved_tickets)
        print(f"Average Resolution Time: {avg_time:.2f} seconds")
    else:
        print("Average Resolution Time: N/A (no resolved tickets)")
    
    # Priority distribution for pending tickets
    normal_count = sum(1 for t in pending_queue if t['priority'] == NORMAL)
    vip_count = sum(1 for t in pending_queue if t['priority'] == VIP)
    emergency_count = sum(1 for t in pending_queue if t['priority'] == EMERGENCY)
    
    print("\nPending Tickets by Priority:")
    print(f"Normal: {normal_count}")
    print(f"VIP: {vip_count}")
    print(f"Emergency: {emergency_count}")


def print_ticket(ticket):
    """Print ticket details"""
    priority_names = {NORMAL: "Normal", VIP: "VIP", EMERGENCY: "Emergency"}
    status = "RESOLVED" if ticket['is_resolved'] else "PENDING"
    
    print(f"\nTicket ID: {ticket['id']}")
    print(f"Customer: {ticket['name']}")
    print(f"Issue: {ticket['issue']}")
    print(f"Priority: {priority_names[ticket['priority']]}")
    print(f"Created: {ticket['creation_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    
    if ticket['is_resolved'] and ticket['resolution_time']:
        print(f"Resolved: {ticket['resolution_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        delta = ticket['resolution_time'] - ticket['creation_time']
        print(f"Resolution Time: {delta.total_seconds():.2f} seconds")
    
    print(f"Status: {status}")
    print("-" * 50)


def load_sample_data():
    """Load sample tickets for testing"""
    global next_ticket_id
    
    print("Loading sample data...")
    
    # Sample ticket 1 - Normal priority
    ticket1 = {
        'id': next_ticket_id,
        'name': "John Doe",
        'issue': "Unable to login to account",
        'priority': NORMAL,
        'creation_time': datetime.now(),
        'resolution_time': None,
        'is_resolved': False
    }
    next_ticket_id += 1
    pending_queue.append(ticket1)
    
    # Sample ticket 2 - VIP priority
    ticket2 = {
        'id': next_ticket_id,
        'name': "Jane Smith",
        'issue': "Payment processing error",
        'priority': VIP,
        'creation_time': datetime.now(),
        'resolution_time': None,
        'is_resolved': False
    }
    next_ticket_id += 1
    pending_queue.appendleft(ticket2)
    
    # Sample ticket 3 - Emergency priority
    ticket3 = {
        'id': next_ticket_id,
        'name': "Bob Johnson",
        'issue': "System down - critical business impact",
        'priority': EMERGENCY,
        'creation_time': datetime.now(),
        'resolution_time': None,
        'is_resolved': False
    }
    next_ticket_id += 1
    pending_queue.appendleft(ticket3)
    
    # Sample resolved ticket
    creation = datetime.now()
    ticket4 = {
        'id': next_ticket_id,
        'name': "Alice Brown",
        'issue': "Password reset request",
        'priority': NORMAL,
        'creation_time': creation,
        'resolution_time': datetime.now(),
        'is_resolved': True
    }
    next_ticket_id += 1
    resolved_tickets.append(ticket4)
    
    print("Sample data loaded: 3 pending tickets, 1 resolved ticket\n")


def main():
    """Main program loop"""
    load_sample_data()
    
    print("Customer Ticket Booking System")
    print("=" * 50)
    
    while True:
        print("\nMenu Options:")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Cancel Ticket")
        print("4. Search Ticket")
        print("5. View All Tickets")
        print("6. Dashboard")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            create_ticket()
        elif choice == 2:
            resolve_ticket()
        elif choice == 3:
            cancel_ticket()
        elif choice == 4:
            search_ticket()
        elif choice == 5:
            view_all_tickets()
        elif choice == 6:
            dashboard()
        elif choice == 7:
            print("Thank you for using the Customer Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()

    