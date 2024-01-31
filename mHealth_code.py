import tkinter as tk
from tkinter import messagebox

class MHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("mHealth App")

        # Create widgets
        self.label = tk.Label(root, text="mHealth App")
        self.label.pack(pady=10)

        self.schedule_button = tk.Button(root, text="Schedule Medication", command=self.schedule_medication)
        self.schedule_button.pack(pady=5)

        self.track_progress_button = tk.Button(root, text="Track Progress", command=self.track_progress)
        self.track_progress_button.pack(pady=5)

        self.educational_content_button = tk.Button(root, text="Educational Content", command=self.educational_content)
        self.educational_content_button.pack(pady=5)

        self.connect_professionals_button = tk.Button(root, text="Connect with Professionals", command=self.connect_professionals)
        self.connect_professionals_button.pack(pady=5)

        self.financial_support_button = tk.Button(root, text="Financial Support", command=self.financial_support)
        self.financial_support_button.pack(pady=5)

        self.hologram_ai_doctor_button = tk.Button(root, text="Hologram of a Doctor", command=self.hologram_ai_doctor)
        self.hologram_ai_doctor_button.pack(pady=5)

    def schedule_medication(self):
        messagebox.showinfo("Medication Schedule", "Medication reminders set up successfully!")

    def track_progress(self):
        messagebox.showinfo("Track Progress", "Track your treatment progress here.")

    def educational_content(self):
        messagebox.showinfo("Educational Content", "Access educational content about drug-resistant tuberculosis.")

    def connect_professionals(self):
        messagebox.showinfo("Connect Professionals", "Connect with healthcare professionals through virtual consultations.")

    def financial_support(self):
        messagebox.showinfo("Financial Support", "Explore financial assistance programs and government initiatives.")
    def hologram_ai_doctor(self):
        messagebox.showinfo("Hologram of a Doctor", "Connecting you with hologram of a doctor, please wait.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MHealthApp(root)
    root.mainloop()
