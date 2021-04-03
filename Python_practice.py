#print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("Whats is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows")

score = int(input("Enter Score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
