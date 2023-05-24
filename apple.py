def share_apples():
    # Number of apples
    num_apples = 2

    # Number of people
    num_people = 3

    # Perform the cut
    num_cuts = 1

    # Calculate the number of pieces after the cut
    num_pieces = num_apples * 2

    # Check if the number of pieces is divisible by the number of people
    if num_pieces % num_people == 0:
        # Calculate the number of pieces each person receives
        pieces_per_person = num_pieces // num_people

        # Print the distribution
        print(f"Each person receives {pieces_per_person} pieces of apple.")
    else:
        print("It is not possible to divide the apples equally among the people.")

# Call the function
share_apples()
