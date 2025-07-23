#defining weather conditions
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
#prompting users for input
weather = input("What's the weather like today? (sunny/rainy/cold):")
if sunny:
    print(f"{sunny}")
elif rainy:
    print(f"{rainy}")
elif cold:
    print(f"{cold}")
else:
    print("Sorry, I don't have recommendations for this weather.")