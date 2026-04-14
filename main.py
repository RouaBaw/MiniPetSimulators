from pet import Pet

pet = Pet("Milo", 5)

print(f"Pet name: {pet.name}")
print(f"Energy level: {pet.energy_level}")

pet.play_with_pet()
print(f"Energy level after playing: {pet.energy_level}")