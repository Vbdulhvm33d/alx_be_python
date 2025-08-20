#defining weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold):")

sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
#prompting users for input

if weather.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print(rainy)
elif weather.lower() == "cold":
    print(cold)
else:
    print("Sorry, I don't have recommendations for this weather.")

