import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

class CryptoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('CryptoCurrent')
        self.root.geometry('800x600')

        self.get_crypto_prices()

    def get_crypto_prices(self):
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for index, coin in enumerate(data):
                if index > 10:  # limiting to 10 coins for performance
                    break

                # Fetching and displaying logo
                logo_url = coin['image']
                logo_image = Image.open(BytesIO(requests.get(logo_url).content))
                logo_photo = ImageTk.PhotoImage(logo_image.resize((50, 50), Image.ANTIALIAS))
                logo_label = tk.Label(self.root, image=logo_photo)
                logo_label.image = logo_photo
                logo_label.grid(row=index, column=0, padx=10, pady=10)

                # Displaying name
                name_label = tk.Label(self.root, text=f"Name: {coin['name']}", font=('Arial', 12))
                name_label.grid(row=index, column=1, padx=10, pady=10)

                # Displaying symbol
                symbol_label = tk.Label(self.root, text=f"Symbol: {coin['symbol']}", font=('Arial', 12))
                symbol_label.grid(row=index, column=2, padx=10, pady=10)

                # Displaying price
                price_label = tk.Label(self.root, text=f"Price: ${coin['current_price']}", font=('Arial', 12))
                price_label.grid(row=index, column=3, padx=10, pady=10)

        else:
            print(f"Failed to fetch data. HTTP status code: {response.status_code}")

if __name__ == "__main__":
    root = tk.Tk()
    CryptoGUI(root)
    root.mainloop()
