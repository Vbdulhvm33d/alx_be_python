#definimg weather conditions
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
#collect input from user
weather_status = input("What's the weather like today? (sunny/rainy/cold): ")
if sunny:
    print("Wear a t-shirt and sunglasses.")
elif rainy:
    print("Don't forget your umbrella and a raincoat.")
elif cold:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")