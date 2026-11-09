colors = []

color = input("Add the first color you like: ")
colors.append ([color])

choice = input("Do you want to add more colors? Yes, or No? ").lower()

if choice == "yes":
    color_2 = input("Add another color to the list: ")
    colors.append ([color_2])
    print(f"The colors you like are: {[color, color_2]} ")

elif choice == "no":
    print(f"The color you like is {[color]}")

else:
    print("Invailed Choice")
