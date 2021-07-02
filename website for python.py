import tkinter as tk
window = tk.Tk
website_greeting = tk.Label(text = 'Enter your username.')
website_username = tk.Entry()

website_user_storage = website_username.get()
f = open("username saves", "a")
f.write(website_user_storage)
file.close()
#how do I make the user make a username one time only

website_greeting.pack()
website_username.pack()
tk.mainloop()
