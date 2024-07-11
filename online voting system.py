candidate_1 = input("Enter first candidate name: ")
candidate_2 = input("Enter second candidate name: ")
candidate_3 = input("Enter third candidate name: ")
candidate_4 = input("Enter fourth candidate name: ")

cand1_votes = 0
cand2_votes = 0
cand3_votes = 0
cand4_votes = 0

voters_id = [555, 556, 557, 558, 559, 560]
no_of_voters = len(voters_id)
print("Number of voters:", no_of_voters)

voted = []

while True:
    if not voters_id:
        print("Voting is over! ^_^")
        if cand1_votes > cand2_votes and cand1_votes > cand3_votes and cand1_votes > cand4_votes:
            print(f"{candidate_1} won the election with {cand1_votes} votes")
        elif cand2_votes > cand1_votes and cand2_votes > cand3_votes and cand2_votes > cand4_votes:
            print(f"{candidate_2} won the election with {cand2_votes} votes")
        elif cand3_votes > cand1_votes and cand3_votes > cand2_votes and cand3_votes > cand4_votes:
            print(f"{candidate_3} won the election with {cand3_votes} votes")
        elif cand4_votes > cand1_votes and cand4_votes > cand3_votes and cand4_votes > cand2_votes:
            print(f"{candidate_4} won the election with {cand4_votes} votes")
        else:
            print("Election tied!")
        break
    else:
        voter = int(input("Enter your ID: "))
        if voter in voted:
            print("You already voted.")
        else:
            if voter in voters_id:
                print(f"1.{candidate_1}\n2.{candidate_2}\n3.{candidate_3}\n4.{candidate_4}")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    cand1_votes += 1
                    print(f"You voted for {candidate_1}")
                elif choice == 2:
                    cand2_votes += 1
                    print(f"You voted for {candidate_2}")
                elif choice == 3:
                    cand3_votes += 1
                    print(f"You voted for {candidate_3}")
                elif choice == 4:
                    cand4_votes += 1
                    print(f"You voted for {candidate_4}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("Sorry, you are not registered to vote.")