# --- Student Record System ---

# Dictionary দিয়ে student এর তথ্য রাখা
students = []

# Function — নতুন student যোগ করা
def add_student(naam, boyos, shahor):
    student = {
        "naam": naam,
        "boyos": boyos,
        "shahor": shahor
    }
    students.append(student)
    print(f"{naam} ke add kora hoyeche!")

# Function — সব student দেখানো
def show_students():
    print("\n--- Sob Student ---")
    for student in students:
        print(f"Naam: {student['naam']}, Boyos: {student['boyos']}, Shahor: {student['shahor']}")

# Function — বড় কে
def boro_boyos(a, b):
    if a > b:
        return a
    else:
        return b

# --- Main Program ---

# Input নিয়ে student যোগ করা
naam = input("Student er naam: ")
boyos = int(input("Student er boyos: "))
shahor = input("Student er shahor: ")
add_student(naam, boyos, shahor)

naam = input("Student er naam: ")
boyos = int(input("Student er boyos: "))
shahor = input("Student er shahor: ")
add_student(naam, boyos, shahor)

# সব student দেখানো
show_students()

# দুই student এর মধ্যে বড় কে
print(f"\nboro boyos: {boro_boyos(students[0]['boyos'], students[1]['boyos'])}")