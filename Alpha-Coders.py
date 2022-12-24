from datetime import datetime

print("------------------  Let's See How Many Days You Have Lived ------------------\n\n\n")

print("\t[!] Note -----> Date must be in format ( DD/MM/YY )\n\n")

dob = input("\tEnter Your date of Birth :-) ")

pd = input("\tEnter present date       :-) ")


start_date = datetime.strptime(pd, "%d/%m/%Y")
end_date = datetime.strptime(dob, "%d/%m/%Y")
result = start_date - end_date

print("\n\n")
print("-"*70)
print(f"\t Today {result.days} days completed of Your Life")
print("-"*70)
