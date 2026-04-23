import copy

def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}
         },
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}
         }
    ]

def replicate_data(users):
    assigned = users
    shallow = users[:]
    deep = copy.deepcopy(users)
    return assigned, shallow, deep

def modify_data(data, reg_no):
    for user in data:
        if reg_no % 2 == 0:
            user["data"]["files"].append("new_file.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()

        user["data"]["usage"] += 100

def check_integrity(original, modified):
    leakage = 0
    safe = 0
    overlap = 0
    for i in range(len(original)):
        # leakage detection
        if original[i]["data"]["files"] != modified[i]["data"]["files"]:
            leakage += 1
        else:
            safe += 1

        common = set(original[i]["data"]["files"]) & set(modified[i]["data"]["files"])
        overlap += len(common)

    return (leakage, safe, overlap)


name = "Ramita"
reg_no = int(input("Enter your register number: "))
original = generate_data()
print("Before Modification:")
print("Original Data:", original)

assigned, shallow, deep = replicate_data(original)
modify_data(assigned, reg_no)

print("\nAfter Assignment Modification:")
print("Original (affected due to assignment):", original)

original = generate_data()
assigned, shallow, deep = replicate_data(original)
modify_data(shallow, reg_no)

print("\nAfter Shallow Copy Modification:")
print("Original (partially affected):", original)
print("Shallow Copy:", shallow)

modify_data(deep, reg_no)
print("\nAfter Deep Copy Modification:")
print("Original (unchanged):", original)
print("Deep Copy:", deep)

result = check_integrity(original, shallow)
print("\nIntegrity Report (leakage, safe, overlap):", result)

if original != deep:
    print("Deep Copy Consistency: Maintained (no data leakage)")

print("\nMutation Depth Analysis:")
print("Inner list changed in shallow copy = affects original")
print("Deep copy creates separate inner objects = no effect on original")
print("\nData Corruption Definition:")
print("Data corruption occurs when original data is unintentionally modified due to improper copying (like assignment or shallow copy).")