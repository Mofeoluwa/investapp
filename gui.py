# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from etf_recommender import recommend_etfs

class InvestmentAdvisorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ETF Investment Advisor")
        self.geometry("500x500")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = ttk.Label(self, text="ETF Investment Advisor", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)

        # Frame for input fields
        frame = ttk.Frame(self)
        frame.pack(pady=10, padx=20, fill="x")

        # Investment Amount
        ttk.Label(frame, text="Amount to invest (USD):").grid(row=0, column=0, sticky="w", pady=5)
        self.amount_entry = ttk.Entry(frame)
        self.amount_entry.grid(row=0, column=1, pady=5, sticky="ew")

        # Investment Horizon (years)
        ttk.Label(frame, text="Investment horizon (years):").grid(row=1, column=0, sticky="w", pady=5)
        self.horizon_entry = ttk.Entry(frame)
        self.horizon_entry.grid(row=1, column=1, pady=5, sticky="ew")

        # Risk Tolerance
        ttk.Label(frame, text="Risk tolerance:").grid(row=2, column=0, sticky="w", pady=5)
        self.risk_combobox = ttk.Combobox(frame, values=["low", "medium", "high"], state="readonly")
        self.risk_combobox.grid(row=2, column=1, pady=5, sticky="ew")
        self.risk_combobox.current(0)

        # Investment Goal
        ttk.Label(frame, text="Investment goal:").grid(row=3, column=0, sticky="w", pady=5)
        self.goal_combobox = ttk.Combobox(frame, values=["growth", "income"], state="readonly")
        self.goal_combobox.grid(row=3, column=1, pady=5, sticky="ew")
        self.goal_combobox.current(0)

        # Submit Button
        submit_btn = ttk.Button(self, text="Submit", command=self.get_recommendations)
        submit_btn.pack(pady=20)

        # Text widget to display recommendations
        self.result_text = tk.Text(self, height=10, wrap="word", state="disabled")
        self.result_text.pack(padx=20, pady=10, fill="both", expand=True)

    def get_recommendations(self):
        # Retrieve and validate user inputs
        try:
            money = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the investment amount.")
            return

        try:
            horizon = float(self.horizon_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the investment horizon (years).")
            return

        risk = self.risk_combobox.get()
        goal = self.goal_combobox.get()

        # Get recommendations (now a string response from GPT-4)
        recommendations = recommend_etfs(risk, horizon, goal)

        # Display recommendations in the text widget
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        # Display user input summary
        self.result_text.insert(tk.END, f"Based on your inputs:\n")
        self.result_text.insert(tk.END, f" - Amount to invest: ${money:,.2f}\n")
        self.result_text.insert(tk.END, f" - Investment horizon: {horizon} years\n")
        self.result_text.insert(tk.END, f" - Risk tolerance: {risk.capitalize()}\n")
        self.result_text.insert(tk.END, f" - Investment goal: {goal.capitalize()}\n\n")

        # Now simply insert the GPT-4 recommendations text.
        self.result_text.insert(tk.END, "ETF Recommendations:\n\n")
        self.result_text.insert(tk.END, recommendations)
        self.result_text.config(state="disabled")


# # gui.py

# import tkinter as tk
# from tkinter import ttk, messagebox
# from etf_recommender import recommend_etfs

# class InvestmentAdvisorGUI(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("ETF Investment Advisor")
#         self.geometry("500x500")
#         self.resizable(False, False)
#         self.create_widgets()

#     def create_widgets(self):
#         # Title Label
#         title = ttk.Label(self, text="ETF Investment Advisor", font=("Helvetica", 16, "bold"))
#         title.pack(pady=10)

#         # Frame for input fields
#         frame = ttk.Frame(self)
#         frame.pack(pady=10, padx=20, fill="x")

#         # Investment Amount
#         ttk.Label(frame, text="Amount to invest (USD):").grid(row=0, column=0, sticky="w", pady=5)
#         self.amount_entry = ttk.Entry(frame)
#         self.amount_entry.grid(row=0, column=1, pady=5, sticky="ew")

#         # Investment Horizon (years)
#         ttk.Label(frame, text="Investment horizon (years):").grid(row=1, column=0, sticky="w", pady=5)
#         self.horizon_entry = ttk.Entry(frame)
#         self.horizon_entry.grid(row=1, column=1, pady=5, sticky="ew")

#         # Risk Tolerance
#         ttk.Label(frame, text="Risk tolerance:").grid(row=2, column=0, sticky="w", pady=5)
#         self.risk_combobox = ttk.Combobox(frame, values=["low", "medium", "high"], state="readonly")
#         self.risk_combobox.grid(row=2, column=1, pady=5, sticky="ew")
#         self.risk_combobox.current(0)

#         # Investment Goal
#         ttk.Label(frame, text="Investment goal:").grid(row=3, column=0, sticky="w", pady=5)
#         self.goal_combobox = ttk.Combobox(frame, values=["growth", "income"], state="readonly")
#         self.goal_combobox.grid(row=3, column=1, pady=5, sticky="ew")
#         self.goal_combobox.current(0)

#         # Submit Button
#         submit_btn = ttk.Button(self, text="Submit", command=self.get_recommendations)
#         submit_btn.pack(pady=20)

#         # Text widget to display recommendations
#         self.result_text = tk.Text(self, height=10, wrap="word", state="disabled")
#         self.result_text.pack(padx=20, pady=10, fill="both", expand=True)

#     def get_recommendations(self):
#         # Retrieve and validate user inputs
#         try:
#             money = float(self.amount_entry.get())
#         except ValueError:
#             messagebox.showerror("Invalid Input", "Please enter a valid number for the investment amount.")
#             return

#         try:
#             horizon = float(self.horizon_entry.get())
#         except ValueError:
#             messagebox.showerror("Invalid Input", "Please enter a valid number for the investment horizon (years).")
#             return

#         risk = self.risk_combobox.get()
#         goal = self.goal_combobox.get()

#         # Get recommendations
#         recommendations = recommend_etfs(risk, horizon, goal)

#         # Display recommendations in the text widget
#         self.result_text.config(state="normal")
#         self.result_text.delete("1.0", tk.END)
#         self.result_text.insert(tk.END, f"Based on your inputs:\n")
#         self.result_text.insert(tk.END, f" - Amount to invest: ${money:,.2f}\n")
#         self.result_text.insert(tk.END, f" - Investment horizon: {horizon} years\n")
#         self.result_text.insert(tk.END, f" - Risk tolerance: {risk.capitalize()}\n")
#         self.result_text.insert(tk.END, f" - Investment goal: {goal.capitalize()}\n\n")

#         if recommendations:
#             self.result_text.insert(tk.END, "ETF Recommendations:\n\n")
#             for etf in recommendations:
#                 # If the recommendation is a warning message, display it differently.
#                 if etf.get("ticker") == "":
#                     self.result_text.insert(tk.END, f"{etf['description']}\n\n")
#                 else:
#                     self.result_text.insert(tk.END, f"{etf['name']} ({etf['ticker']})\n")
#                     self.result_text.insert(tk.END, f"Description: {etf['description']}\n\n")
#         else:
#             self.result_text.insert(tk.END, "No ETF recommendations available for your criteria.\n")
#         self.result_text.config(state="disabled")
