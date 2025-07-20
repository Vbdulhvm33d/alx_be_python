#definimg weather conditions
sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."
#collect input from user
weather_status = input("What's the weather like today? (sunny/rainy/cold): ")
if sunny:
    print(sunny)
elif rainy:
    print(rainy)
elif cold:
    print(cold)
else:
    print("Sorry, I don't have recommendations for this weather.")