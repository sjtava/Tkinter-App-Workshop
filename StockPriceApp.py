# importing the libraries needed
from tkinter import *
import requests

# creating the main window
window = Tk()

# adding a title to the main window
window.title("Stock Price App")

# setting the size of the application window
window.geometry("350x200")

# setting the background color of the window
window.configure(background="light blue")

# creating a label that tells the user to enter a stock symbol
user_label = Label(window, text="Enter the stock symbol:", font= ("Courier New", 13, "bold"), background="light blue")

# attaching/adding/packing the userLabel widget to the window
user_label.pack(pady=10)

# creating the entry widget that the user will enter the stock symbol into
user_input = Entry(window, width=21, font=("Courier New", 12))
user_input.pack()

# defining/creating the get_close_price function
def get_close_price():

  # getting the stock symbol that the user inputted and assigning it to the variable stock
  stock = user_input.get().upper()

  key = "place your key here"

  # assigning the endpoint URL to a variable
  url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/prev?unadjusted=true&apiKey={key}"

  # making a get request to the endpoint, assigning the data that it returns to the variable r
  r = requests.get(url)

  # making the response object a Python dictionary
  data = r.json()

  # making sure the value at the resultsCount key is not equal to zero (zero would mean that the API call did not return a close price)
  if data["resultsCount"] != 0:

    # parsing/extracting the close price from the data that the API call returned
    close_price = data["results"][0]["c"]

    # updating the close_price_label with the close price
    close_price_label.config(text=f"{stock.upper()} closed at ${close_price} last!", fg="black", font=("Courier New", 12, "bold"))

  # prompting the user to enter a valid symbol if the resultsCount key has a value of zero
  else:
    close_price_label.config(text="Please enter a valid symbol!", fg="red", font=("Courier New", 13, "bold"))

# creating a button that executes the get_close_price function and returns the close price to the user
button = Button(window, text="Calculate", font=("Courier New", 12), bg="black", fg="white", command=get_close_price)
button.pack(pady=10)

# creating a blank result label (for the closing price and the error message)
close_price_label = Label(window, bg="light blue")
close_price_label.pack(pady=10)

window.mainloop()
