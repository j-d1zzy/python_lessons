def game():
    '''Plan for the game: PC is a clerk who yearns for something greater in their life. Where is the glory? Where is the excitement?
    Isn't that what we were supposed to learn from all those fairy tales and folk songs about heroes? '''
    n = input("\nName: \n\n")
    n = n.capitalize()
    # print(n)
    gsp = input("\nSex (M/F): \n\n")
    gsp = gsp.lower()
    gspc = ""
    gs = ""
    gsc = ""
    gpa = ""
    gpc = ""

    if gsp == "m":
      # print(f"{n} is male!")
      gsp = "he" 
      gspc = "He"
      gpa = "his"
      gpac = "His"
      gop = "him"
      gopc = "Him"
      gpp = "his"
      gppc = "His"
      print(f"\nThe candle blazes before {n}, unwavering. Still. Orange. Constant. It burns sedately: a flaming droplet hovering above the waxen candle, motionless...")
      input(f"\npress enter")
      print(f"\nIt bathes the bare apple wood desk in a dull golden gloom. The candle alone lights the dim office, and {gpa} gaze adheres to it, sticking drily like\nthe hardening wax on the side of the stick. {gspc} stares into the fire and it seems to shrink. The walls leer at the ridge of {gpa} vision, nearing,\nleaning lower, crowding {gop}.")
      input(f"\npress enter")
      print(f"\n{n} shudders.")
      input(f"\npress enter")
      print(f"\n{gspc} knows the date better than anyone in the entire city, being a clerk, and yet for all {gpa} dated records {n} had nevertheless lost track of time. After all, what was the point in tracking that which never ceases, never tires, and can never be caught? When {n} had been promoted to the position of clerk, apprentice to the broker, {gsp} thought things were going to change in {gpa} life. Maybe it would have been...")
    elif gsp == "f":
      # print(f"{n} is female.")
      gsp = "she"
      gspc = "She"
      gpa = "her"
      gpac = "Her"
      gop = "her"
      gopc = "Her"
      gpp = "hers"
      gppc = "Hers"
      print(f"\nThe candle blazes before {n}, unwavering. Still. Orange. Constant. It burns sedately: a flaming droplet hovering above the waxen candle, motionless...")
      input(f"\npress enter")
      print(f"\nIt bathes the bare apple wood desk in a dull golden gloom. The candle alone lights the dim office, and {gpa} gaze adheres to it, sticking drily like\nthe hardening wax on the side of the stick. {gspc} stares into the fire and it seems to shrink. The walls leer at the ridge of {gpa} vision, nearing,\nleaning lower, crowding {gop}.")
      input(f"\npress enter")
      print(f"\n{n} shudders.")
      input(f"\npress enter")
      print(f"\n{gspc} knows the date better than anyone in the entire city, being a clerk, and yet for all {gpa} dated records {n} had nevertheless lost track of time. After all, what was the point in tracking that which never ceases, never tires, and can never be caught? When {n} had been promoted to the position of clerk, apprentice to the broker, {gsp} thought things were going to change in {gpa} life. Maybe it would have been...")
  # age = input("Age (between 33 and 180): \n")

game()