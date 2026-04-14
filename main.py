from pet import Pet

pet = Pet("Milo", 5)

print(f"Pet name: {pet.name}")
print(f"Initial energy level: {pet.energy_level}")

pet.feed_pet()
pet.play_with_pet()

print(f"Final energy level: {pet.energy_level}")