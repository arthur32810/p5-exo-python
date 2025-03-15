students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}

student = input("Entrez le nom de l'étudiant: ")

if student not in students:
    print(f"L'étudiant {student} n'existe pas dans la liste.")
else:
    print(f"Notes de {student}:")
    for subject, mark in students[student].items():
        print(f"\t{subject}: {mark}")

    print(
        f"Moyenne de {student}: "
        f"{sum(students[student].values()) / len(students[student])}"
    )
