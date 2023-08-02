def game():
    '''Plan for the game: PC is a clerk who yearns for something greater in their life. Where is the glory? Where is the excitement?
    Isn't that what we were supposed to learn from all those fairy tales and folk songs about heroes? '''
    n = input("\nName: \n\n")
    n = n.capitalize()
    np = (f"{n}'s")
    # print(n)
    gsp = input("\nSex (M/F): \n\n")
    gsp = gsp.lower()

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
      gnro = "himself"
      gnroc = "Himself"
      print(f"\nThe candle blazes before {n}, unwavering. Still. Orange. Constant. It burns sedately: a flaming droplet hovering above the waxen candle, motionless. It bathes the bare apple wood desk\nin a dull golden gloom. The solitary candle lights the dim office, alone. {np} gaze adheres to it, sticking drily like the hardening wax on the side of the stick. {gspc} stares into the\nfire and it seems to shrink. The walls leer at the ridge of {gpa} vision, nearing, leaning lower, crowding {gop}. {n} shudders.")
      input(f"\npress enter")
      print(f"\n{gspc} knows the date better than anyone in the entire city, being a clerk, and yet for all {gpa} dated records {n} has nevertheless lost track of time, {gsp} realises. Then again, what was\nthe point in tracking that which never ceases, never tires, and can never be caught? When {n} was promoted to the position of clerk, apprentice to the broker, {gsp} thought things were\ngoing to change in {gpa} life. Only... they hadn't.")
      input(f"\npress enter")
      print(f"\nBefore {gpa} promotion, the nobles and the privileged few who work alongside them seemed to live so luxuriously. Glamorous, mysterious careers replete with secret and scandal. In truth,\n{gpa} ascension had just meant more drudgery. Eternal tallying on endless scrolls for an inventory that may as well be infinite, as the task is never complete. Meaningless.")
      input(f"\npress enter")
      print(f"\nIt isn't literally meaningless, of course. It is meaningless at a deeper level. It is hard to articulate, mused {n}. Weren't things meant to get better in life, to change? Doors were\nmeant to open to new opportunities; that's what they had always said. Instead, the very ceiling seemed even now to sink towards {gop}; the walls crawled closer; the door was smaller with\neach second; {gpa} lungs even felt tight. {gspc} forced {gnro} to breathe.")
      input(f"\npress enter")
      print(f"\n{n} swallows, partly from nerves and partly disgust. What sort of dwarf is claustrophobic, {gsp} thinks dourly? {n} refuses to remove {gpa} view from the tranquil candle-flame, and\nattempts to adopt its calm. But wasn't this stasis the problem? Being calm. Becalmed. What's the difference anyway?")
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
      gnro = "herself"
      gnroc = "Herself"
      print(f"\nThe candle blazes before {n}, unwavering. Still. Orange. Constant. It burns sedately: a flaming droplet hovering above the waxen candle, motionless. It bathes the bare apple wood desk\nin a dull golden gloom. The solitary candle lights the dim office, alone. {np} gaze adheres to it, sticking drily like the hardening wax on the side of the stick. {gspc} stares into the\nfire and it seems to shrink. The walls leer at the ridge of {gpa} vision, nearing, leaning lower, crowding {gop}. {n} shudders.")
      input(f"\npress enter")
      print(f"\n{gspc} knows the date better than anyone in the entire city, being a clerk, and yet for all {gpa} dated records {n} has nevertheless lost track of time, {gsp} realises. Then again, what was\nthe point in tracking that which never ceases, never tires, and can never be caught? When {n} was promoted to the position of clerk, apprentice to the broker, {gsp} thought things were\ngoing to change in {gpa} life. Only... they hadn't.")
      input(f"\npress enter")
      print(f"\nBefore {gpa} promotion, the nobles and the privileged few who work alongside them seemed to live so luxuriously. Glamorous, mysterious careers replete with secret and scandal. In truth,\n{gpa} ascension had just meant more drudgery. Eternal tallying on endless scrolls for an inventory that may as well be infinite, as the task is never complete. Meaningless.")
      input(f"\npress enter")
      print(f"\nIt isn't literally meaningless, of course. It is meaningless at a deeper level. It is hard to articulate, mused {n}. Weren't things meant to get better in life, to change? Doors were\nmeant to open to new opportunities; that's what they had always said. Instead, the very ceiling seemed even now to sink towards {gop}; the walls crawled closer; the door was smaller with\neach second; {gpa} lungs even felt tight. {gspc} forced {gnro} to breathe.")
      input(f"\npress enter")
      print(f"\n{n} swallows, partly from nerves and partly disgust. What sort of dwarf is claustrophobic, {gsp} thinks dourly? {n} refuses to remove {gpa} view from the tranquil candle-flame, and\nattempts to adopt its calm. But wasn't this stasis the problem? Being calm. Becalmed. What's the difference anyway?")
  # age = input("Age (between 33 and 180): \n")
game()