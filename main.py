from pet import Pet

pet = Pet("Milo", 5)

print(f"Pet name: {pet.name}")
print(f"Energy level: {pet.energy_level}")

pet.feed_pet()
print(f"Energy level after feeding: {pet.energy_level}")