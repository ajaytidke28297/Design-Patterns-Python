# SRP (Single Responsibility Principle), SOC (Separation of Concerns)

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}:{text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file_obj = open(filename, 'w')
        file_obj.write(str(journal))
        file_obj.close()


j = Journal()
j.add_entry("I Laughed today.")
j.add_entry("I learned something new today")
print(f"Journal entries:\n{j}")

file = r'c:\temp\journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())