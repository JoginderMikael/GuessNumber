class LuxuryWatch:
    watches_created = 0  # Class variable to keep track of created watches

    def __init__(self):
        LuxuryWatch.watches_created += 1  # Increment counter on object creation

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @staticmethod
    def validate_engraving_text(text):
        if len(text) > 40 or not text.isalnum():
            raise ValueError("Engraving text must be alphanumeric and at most 40 characters long.")

    @classmethod
    def create_watch_with_engraving(cls, text):
        cls.validate_engraving_text(text)  # Validate text before engraving
        watch = cls()
        watch.engraving = text
        return watch


# Creating a regular watch (no engraving)
watch1 = LuxuryWatch()
print("Watches created:", LuxuryWatch.get_number_of_watches_created())

# Creating a watch with correct engraving
try:
    watch2 = LuxuryWatch.create_watch_with_engraving("MyLuxuryWatch2025")
    print("Watches created:", LuxuryWatch.get_number_of_watches_created())
except ValueError as e:
    print("Error:", e)

# Attempting to create a watch with incorrect engraving
try:
    watch3 = LuxuryWatch.create_watch_with_engraving("foo@baz.com")  # Invalid engraving
except ValueError as e:
    print("Error:", e)

# Display final count of watches
print("Final number of watches created:", LuxuryWatch.get_number_of_watches_created())
