import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("sing-in Screen")
root.attributes("-fullscreen", True)

class Sing:
    def validate_input(self, input_string):
        if input_string.isalpha():
            return True
        else:
            return False
    
    def link(self):
        from login_system import Login 
        Login()

    # Validation function for login
    def validate_password(self):
        password = self.password_entry.get()
        confirmpassword = self.comfirmpassword_entry.get()
        fullname = self.fullname_entry.get()

        if password == confirmpassword and self.validate_input(fullname):
            self.label.config(text="Everything is correct", fg="green")
        else:
            self.label.config(text="Passwords are not equal", fg="red")

    def __init__(self, root):
        # Full name label
        self.fullname_label = tk.Label(root, text="Full name")
        self.fullname_label.pack()

        # Full name text entry
        self.fullname_entry = tk.Entry(root)
        self.fullname_entry.pack()

        # Username label
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        # Username text entry
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Password label
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        # Password text entry
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Confirm password label
        self.comfirmpassword_label = tk.Label(root, text="Confirm password:")
        self.comfirmpassword_label.pack()

        # Confirm password text entry
        self.comfirmpassword_entry = tk.Entry(root, show="*")
        self.comfirmpassword_entry.pack()

        # Result label
        self.label = tk.Label(root, text="")
        self.label.pack()

        # Validate button
        self.validate_button = tk.Button(root, text="Validate", command=self.validate_password)
        self.validate_button.pack()

        # Quit button
        self.quit_button = tk.Button(root, text="ja tenho conta", command=self.link)
        self.quit_button.pack()

        # Quit button
        self.quit_button = tk.Button(root, text="Quit", command=quit)
        self.quit_button.pack()

# Start the main event loop
app = Sing(root)
root.mainloop()
