def add_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added.")

def show_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        print("Notes:")
        for note in notes:
            print(note.strip())
    except FileNotFoundError:
        print("No notes saved.")

if __name__ == "__main__":
    add_note("This is a test note.")
    show_notes()
