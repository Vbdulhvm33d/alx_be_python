#defining weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold):")

sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
#prompting users for input

if weather == sunny:
    print(f"{sunny.lower()}")
elif weather == sunny:
    print(f"{rainy.lower()}")
elif weather == cold:
    print(f"{cold}")
else:
    print("Sorry, I don't have recommendations for this weather.")

