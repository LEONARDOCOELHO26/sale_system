import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Login Screen")
root.attributes("-fullscreen", True)

class Login:    
    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Example validation (replace with your own validation code)
        if username == "admin" and password == "secret":
            self.label.config(text="Login successful", fg="green")
        else:
            self.label.config(text="Invalid login", fg="red")
    
    def link01(self):
        from sing_system import Sing 
        Sing()

    def __init__(self, root):
        # Create a label for the username
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        # Create a text entry for the username
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Create a label for the password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        # Create a text entry for the password
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.label = tk.Label(root, text="")
        self.label.pack()

        # Create a login button
        self.login_button = tk.Button(root, text="Login", command=self.validate_login)
        self.login_button.pack()

        self.validate_button = tk.Button(root, text="Don't have an account", command=self.link01)
        self.validate_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()


login = Login(root)

# Start the window's event loop
root.mainloop()

