command = "maths"

match command:
    case "maths":
        print("You have selected maths.")
    case "science":
        print("You have selected science.")
    case "english":
        print("You have selected english.")

    case _:
        print("Invalid selection.")