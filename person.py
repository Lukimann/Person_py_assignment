class Person:
    def __init__(self, name, age, gender):
        # Initialize attributes for name, age, gender
        self.name = name
        self.age = age
        self.gender = gender
        # Initialize next attribute to None (no next node initially)
        self.next = None

# Define a class to manage the collection of student records using a linked list
class PersonDatabase:
    def __init__(self):
        # Initialize head attribute to None (empty linked list initially)
        self.head = None

    # Method to add a new person record to the linked list
    def add_person(self, name, age, gender):
        # Create a new person object with the provided data
        new_person = Person(name, age, gender)
        # If the linked list is empty, set the new student as the head
        if not self.head:
            self.head = new_person
        else:
            # Traverse the linked list to find the last node
            current = self.head
            while current.next:
                current = current.next
            # Add the new person as the next node of the last node
            current.next = new_person

    # Method to display all people records in the linked list
    def display_person(self):
        # Start traversal from the head of the linked list
        current = self.head
        # Traverse the linked list and print each person's information
        while current:
            print(f"Name: {current.name}, Age: {current.age}, Gender: {current.gender}")
            # Move to the next node
            current = current.next

# Example Usage:
# Create a new PersonDatabase object
person_db = PersonDatabase()
# Add people records to the database
person_db.add_person("Louis", 20, "male")
person_db.add_person("Zawadi", 21, "female")
person_db.add_person("Ron", 19, "male")
# Display all peoples records in the database
person_db.display_person()

