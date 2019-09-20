# Practice: Showroom and Junkyards
showroom = ()
showroom = set(["corvette", "mustang", "altima", "saburban"])

showroom.add("corvette")
showroom.update(["boxter", "beatle"])
showroom.discard("beatle")

print("showroom", showroom)

junkyard = ()
junkyard = set(["mustang", "boxter", "civic", "charger", "f150"])

print("junkyard", junkyard)

int = showroom.intersection(junkyard)

print("intersection", int)

combined = showroom.union(junkyard)

print("combined", combined)

combined.discard("saburban")

print("combined_2", combined)
