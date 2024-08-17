amount=int(input("Enter the amount you want to withdraw"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("Number of 100 notes:", note1)
print("Number of 50 notes:", note2)
print("Number of 10 notes:", note3)
