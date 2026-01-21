class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    # Method Overriding: providing specific implementation
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    # Method Overriding: providing specific implementation
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

print("--- Bird ---")
obj_bird.intro()
obj_bird.flight()

print("\n--- Sparrow ---")
obj_sparrow.intro()
obj_sparrow.flight()

print("\n--- Ostrich ---")
obj_ostrich.intro()
obj_ostrich.flight()
