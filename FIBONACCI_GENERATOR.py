import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from tkinter import ttk

# Function to generate Fibonacci series
def generate_fibonacci():
    try:
        # Get the number of terms from the slider
        n = slider.get()
        if n <= 0:
            messagebox.showwarning("Input Error", "Please select a positive integer.")
            return
        
        # Start with the first two numbers of the Fibonacci series
        fib_series = [0, 1]
        
        # Generate the Fibonacci series up to n terms
        for i in range(2, n):
            next_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(next_fib)

        # Update the result label and display the Fibonacci series
        result_label.config(text="Fibonacci Series: " + ', '.join(map(str, fib_series[:n])))
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save the Fibonacci series to a file
def save_to_file():
    fib_series_text = result_label.cget("text")
    if fib_series_text == "Fibonacci Series: ":
        messagebox.showwarning("No Data", "Please generate a Fibonacci series first.")
        return
    
    # Open file dialog to choose the location and filename
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(fib_series_text)
        messagebox.showinfo("Saved", f"Fibonacci series saved to {file_path}")

# Function to reset the fields
def reset_fields():
    slider.set(10)  # Reset slider to a default value
    result_label.config(text="Fibonacci Series: ")
    custom_label_entry.delete(0, tk.END)  # Clear custom label entry field
    font_size_combobox.set("12")  # Reset font size combo box

# Set up the main window
root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("500x500")
root.config(bg="#f0f0f0")

# Create and place widgets
title_label = tk.Label(root, text="Fibonacci Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

description_label = tk.Label(root, text="Select the number of Fibonacci terms below:", bg="#f0f0f0", font=("Arial", 12))
description_label.pack(pady=5)

# Slider to choose the number of terms
slider = tk.Scale(root, from_=1, to=100, orient="horizontal", font=("Arial", 12), bg="#f0f0f0")
slider.set(10)  # Default value
slider.pack(pady=10)

generate_button = tk.Button(root, text="Generate Fibonacci", font=("Arial", 14), bg="#4CAF50", fg="white", command=generate_fibonacci)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save to File", font=("Arial", 14), bg="#2196F3", fg="white", command=save_to_file)
save_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), bg="#f44336", fg="white", command=reset_fields)
reset_button.pack(pady=10)

# Label to show Fibonacci series
result_label = tk.Label(root, text="Fibonacci Series: ", font=("Arial", 12), bg="#f0f0f0", wraplength=400)
result_label.pack(pady=20)

# Info section with description
info_label = tk.Label(root, text="The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It starts with 0 and 1.", 
                       font=("Arial", 10), bg="#f0f0f0", wraplength=450)
info_label.pack(pady=10)

# Exit button to close the app
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg="#9E9E9E", fg="white", command=root.quit)
exit_button.pack(pady=20)

# Designer name at the bottom
designer_label = tk.Label(root, text="Design by @Rohit!", font=("Arial", 12), bg="#f0f0f0", fg = "red")
designer_label.pack(side="bottom", pady=10)

# Start the Tkinter event loop
root.mainloop()
