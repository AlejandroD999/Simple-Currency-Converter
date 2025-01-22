import tkinter as tk

#Main Settings
main = tk.Tk()
title = main.title("Currency Converter")
cc_layout = main.geometry("300x300")
lock_size = main.resizable(0,0)
main_color = main.configure(bg="#F1DFA9" )
main_text_color = main.configure()
#Main Settings End

#Convertion rates 

convertion_rates = {
    "U.S Dollar":1,
    "Euro": 0.95,
    "Yen": 154.34,
    "British Pound": 0.79,
    "Swiss Feanc": 0.98
}

#Buttons Click
def convert_currency():
      try:
            amount = float(currency1_textbox.get("1.0", tk.END).strip())
            from_currency = currency_1.get()
            to_currency = currency_2.get()

            converted_amount = amount * (convertion_rates[to_currency] / convertion_rates[from_currency])
            output_label.config(text=f"{converted_amount: .2f} {to_currency}")
      except ValueError:
            output_label.config(text="Invalid input")

#Buttoncs Click End

#Buttons
currency_1 = tk.StringVar()
currency_1.set("U.S Dollar")

c1_options = ["U.S Dollar"]
c1_option_menu = tk.OptionMenu(main, currency_1, *c1_options)
c1_option_menu.place(x=35, y=100)

currency_2 = tk.StringVar()
currency_2.set("U.S Dollar")

c2_options = ["U.S Dollar", "Euro", "Yen", "British Pound", "Swiss Franc"]
c2_options_menu = tk.OptionMenu(main, currency_2, *c2_options)
c2_options_menu.place(x=180, y=100)

convert_button = tk.Button(
    main,
    text="Convert",
    command = convert_currency)
convert_button.place(x=95, y= 175,height=22 ,width=50)


#Buttons End

#Labels
canvas_title = tk.Label(
    main,
    text= "Currency Converter",
    bg="#F1DFA9",
    font = ('helvetica 15 bold underline')
)

canvas_title.pack()

c1_input = tk.Label(main, text="Input")
c1_input.place(x=35, y=80)

c2_output = tk.Label(main, text="Ouptut")
c2_output.place(x=180, y=80)

currency1_input = tk.Label(main, text="Quantity: ")
currency1_input.place(x=10, y= 155)

currency1_textbox = tk.Text(main, height=1, width=10)
currency1_textbox.place(x=10, y= 175)

output_label = tk.Label(main, text="", bg="#F1DFA9", font=('helvetica', 10))
output_label.place(x=180, y=130)
#Labels End

#Statements

#Statements End


loop = main.mainloop()
