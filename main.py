import tkinter as tk
from tkinter import ttk

class AircraftOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aircraft Strip Tracker")

        # Entry for aircraft callsign
        self.callsign_label = tk.Label(root, text="Aircraft Callsign:")
        self.callsign_label.grid(row=0, column=0, padx=5, pady=5)
        self.callsign_entry = tk.Entry(root)
        self.callsign_entry.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for flight phase
        self.phase_label = tk.Label(root, text="Flight Phase:")
        self.phase_label.grid(row=1, column=0, padx=5, pady=5)
        self.phase_var = tk.StringVar(value="Select Phase")
        self.phase_dropdown = ttk.Combobox(root, textvariable=self.phase_var)
        self.phase_dropdown['values'] = ("IFR", "VFR", "Taxi", "Push")
        self.phase_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Add Aircraft Strip", command=self.add_aircraft_strip)
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Frame to display aircraft strips
        self.strips_frame = tk.Frame(root)
        self.strips_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def add_aircraft_strip(self):
        callsign = self.callsign_entry.get().strip()
        phase = self.phase_var.get()

        # Check if both callsign and phase are provided
        if callsign and phase != "Select Phase":
            # Create a frame for the strip
            strip_frame = tk.Frame(self.strips_frame, relief="raised", bd=2, padx=5, pady=5, bg="lightgrey")
            strip_frame.pack(fill="x", pady=2)

            # Callsign and phase label
            callsign_label = tk.Label(strip_frame, text=f"{callsign} - {phase}", font=("Arial", 12, "bold"), bg="lightgrey")
            callsign_label.grid(row=0, column=0, padx=5)

            # Scratchpad entry
            scratchpad_entry = tk.Entry(strip_frame, width=20)
            scratchpad_entry.grid(row=0, column=1, padx=5)

            # Checkbox to clear the strip
            clear_var = tk.BooleanVar()
            clear_check = tk.Checkbutton(
                strip_frame, text="Clear", variable=clear_var,
                command=lambda: self.remove_strip(clear_var, strip_frame)
            )
            clear_check.grid(row=0, column=2, padx=5)

            # Clear the entry and reset the dropdown
            self.callsign_entry.delete(0, tk.END)
            self.phase_var.set("Select Phase")
        else:
            tk.messagebox.showwarning("Input Error", "Please enter a callsign and select a flight phase.")

    def remove_strip(self, clear_var, strip_frame):
        """Remove the strip frame if the checkbox is selected."""
        if clear_var.get():
            strip_frame.pack_forget()

# Run the application
root = tk.Tk()
app = AircraftOrderApp(root)
root.mainloop()
