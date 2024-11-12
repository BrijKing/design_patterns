class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
        
    def add_entries(self, txt):
        self.entries.append(f"{self.count}. {txt}")
        self.count += 1
        
    def remove_entries(self, pos):
        del self.entries[pos]
        
    def __str__(self):
        return "\n".join(self.entries)
    
    
    #This will break the single resposnibility principle.
    
    # def save_to_file(self, filename):
    #     file = open(filename, "w")
    #     file.write(self.entries)
    #     file.close()
    
    
class PersistenceManager:
    
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
        
        
j = Journal()

j.add_entries("I cried Today !!")
j.add_entries("I laugh today!!")

# print(f"Journal entries : \n{j}\n")

file = "my_journal"
PersistenceManager.save_to_file(j,file)

with open(file) as f:
    print(f.read())

    
        
        
        