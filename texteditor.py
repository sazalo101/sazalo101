#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete("1.0", tk.END)
    root.title("Mojo Editor")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), 
                                                        ("Python files", "*.py"), 
                                                        ("HTML files", "*.html"), 
                                                        ("JavaScript files", "*.js"),
                                                        ("CSS files", "*.css"),
                                                        ("Markdown files", "*.md"),
                                                        ("JSON files", "*.json"),
                                                        ("XML files", "*.xml"),
                                                        ("YAML files", "*.yaml"),
                                                        ("CSV files", "*.csv"),
                                                        ("Java files", "*.java"),
                                                        ("C files", "*.c"),
                                                        ("C++ files", "*.cpp"),
                                                        ("C# files", "*.cs"),
                                                        ("PHP files", "*.php"),
                                                        ("Ruby files", "*.rb"),
                                                        ("Perl files", "*.pl"),
                                                        ("Shell script files", "*.sh"),
                                                        ("Batch files", "*.bat"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        root.title(f"MOJO - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"), 
                                                        ("Python files", "*.py"), 
                                                        ("HTML files", "*.html"), 
                                                        ("JavaScript files", "*.js"),
                                                        ("CSS files", "*.css"),
                                                        ("Markdown files", "*.md"),
                                                        ("JSON files", "*.json"),
                                                        ("XML files", "*.xml"),
                                                        ("YAML files", "*.yaml"),
                                                        ("CSV files", "*.csv"),
                                                        ("Java files", "*.java"),
                                                        ("C files", "*.c"),
                                                        ("C++ files", "*.cpp"),
                                                        ("C# files", "*.cs"),
                                                        ("PHP files", "*.php"),
                                                        ("Ruby files", "*.rb"),
                                                        ("Perl files", "*.pl"),
                                                        ("Shell script files", "*.sh"),
                                                        ("Batch files", "*.bat"),
                                                        ("All files", "*.*")])
    if file_path:
        file_type = file_path.split('.')[-1]
        with open(file_path, "w") as file:
            if file_type in ['txt', 'py', 'html', 'js', 'css', 'md', 'json', 'xml', 'yaml', 'csv', 'java', 'c', 'cpp', 'cs', 'php', 'rb', 'pl', 'sh', 'bat']:
                file.write(text.get("1.0", tk.END))
                messagebox.showinfo("Information", f"{file_type.upper()} file is saved successfully.")
            else:
                messagebox.showwarning("Warning", f"Unsupported file format: .{file_type}")

        root.title(f"Mojo Editor - {file_path}")

def about():
    messagebox.showinfo("About", "Simple Text Editor\nCreated with Python and Tkinter")

root = tk.Tk()
root.title("Mojo Editor")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=False)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()
