
from datetime import datetime
from threading import Thread
from pystyle import Colors, Colorate, Center

banner = """

01001 01010 10100 10101 01010 10101 01001 01010 10100 10101 01010 10101 01001 01010 10100
10110 10101 01010 01101 10101 01010 01101 10101 01010 01101 10101 01010 01101 10101 01010

  ██████╗  █████╗ ███╗  ██╗██╗  ██╗     ██████╗ ██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
  ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝     ██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
  ██████╔╝███████║██╔██╗██║█████╔╝      ███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
  ██╔══██╗██╔══██║██║╚████║██╔═██╗      ╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
  ██████╔╝██║  ██║██║ ╚███║██║  ██╗     ███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

10110 10101 01010 01101 10101 01010 01101 10101 01010 01101 10101 01010 01101 10101 01010
01001 01010 10100 10101 01010 10101 01001 01010 10100 10101 01010 10101 01001 01010 10100

                              [ v1.0.0 ]       [ STATUS: updated ]       [ AUTHOR: you ]

"""

print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(banner)))


# ================= LOGIC =================

class Account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.tx = []
    def log(self, t, a):
        now = datetime.now().strftime("%d/%m %H:%M")

# ================= UI THEME =================

BG = "#020617"
CARD = "#020617"
BTN = "#2563eb"
TXT = "#e5e7eb"
SUB = "#94a3b8"
ERR = "#dc2626"

# ================= ATM APP =================
import tkinter as tk

class ATM(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM PRO")
        self.geometry("430x560")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.acc = None
        self.frame = None

        self.setup_screen()

    def screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = tk.Frame(self, bg=CARD)
        self.frame.pack(expand=True, fill="both", padx=20, pady=20)

    # ========== SETUP (NEW ACCOUNT) ==========
    def setup_screen(self):
        self.screen()

        tk.Label(self.frame, text="SETUP ACCOUNT", fg=TXT, bg=CARD,
                 font=("Segoe UI", 22, "bold")).pack(pady=10)

        tk.Label(self.frame, text="Bank / Account Name", fg=SUB, bg=CARD,
                 font=("Segoe UI", 11)).pack(anchor="w", padx=6, pady=(10, 0))
        self.name_var = tk.StringVar()
        tk.Entry(self.frame, textvariable=self.name_var,
                 font=("Segoe UI", 14)).pack(fill="x", pady=6)

        tk.Label(self.frame, text="PIN (4 digits)", fg=SUB, bg=CARD,
                 font=("Segoe UI", 11)).pack(anchor="w", padx=6, pady=(10, 0))
        self.pin_var = tk.StringVar()
        tk.Entry(self.frame, textvariable=self.pin_var, show="*",
                 font=("Segoe UI", 14)).pack(fill="x", pady=6)

        tk.Label(self.frame, text="Initial Balance (€)", fg=SUB, bg=CARD,
                 font=("Segoe UI", 11)).pack(anchor="w", padx=6, pady=(10, 0))
        self.bal_var = tk.StringVar()
        tk.Entry(self.frame, textvariable=self.bal_var,
                 font=("Segoe UI", 14)).pack(fill="x", pady=6)

        self.button("CREATE", self.create_account)
        self.button("EXIT", self.destroy, danger=True)

    def create_account(self):
        name = self.name_var.get().strip()
        pin = self.pin_var.get().strip()
        bal_s = self.bal_var.get().strip()

        if not name:
            return self.flash_error("NAME REQUIRED")

        if not (pin.isdigit() and len(pin) == 4):
            return self.flash_error("PIN MUST BE 4 DIGITS")

        try:
            bal = float(bal_s)
            if bal < 0:
                raise ValueError
        except:
            return self.flash_error("INVALID BALANCE")

        self.acc = Account(name, pin, bal)
        self.insert_card()

    # ========== INSERT CARD ==========
    def insert_card(self):
        self.screen()
        tk.Label(self.frame, text="INSERT CARD", fg=TXT, bg=CARD,
                 font=("Segoe UI", 26, "bold")).pack(expand=True)
        self.after(1400, self.pin_screen)

    # ========== PIN ==========
    def pin_screen(self):
        self.screen()

        tk.Label(self.frame, text=self.acc.name, fg=SUB, bg=CARD,
                 font=("Segoe UI", 12)).pack(pady=(10, 0))

        tk.Label(self.frame, text="ENTER PIN", fg=TXT, bg=CARD,
                 font=("Segoe UI", 20, "bold")).pack(pady=10)

        self.pin_enter = tk.StringVar()
        tk.Entry(self.frame, textvariable=self.pin_enter, show="*",
                 font=("Segoe UI", 20), justify="center").pack(pady=10)

        self.button("CONFIRM", self.check_pin)
        self.button("RESET ACCOUNT", self.setup_screen, ghost=True)

    def check_pin(self):
        if self.pin_enter.get() == self.acc.pin:
            self.menu()
        else:
            self.flash_error("WRONG PIN")

    # ========== MENU ==========
    def menu(self):
        self.screen()

        tk.Label(self.frame, text=self.acc.name, fg=SUB, bg=CARD,
                 font=("Segoe UI", 12)).pack()

        tk.Label(self.frame, text=f"€ {self.acc.balance:.2f}",
                 fg=TXT, bg=CARD, font=("Segoe UI", 34, "bold")).pack(pady=10)

        self.button("DEPOSIT", lambda: self.amount("DEPOSIT"))
        self.button("WITHDRAW", lambda: self.amount("WITHDRAW"))
        self.button("TRANSACTIONS / RECEIPT", self.receipt)
        self.button("LOGOUT", self.insert_card, ghost=True)

    # ========== AMOUNT ==========
    def amount(self, mode):
        self.screen()

        tk.Label(self.frame, text=mode, fg=TXT, bg=CARD,
                 font=("Segoe UI", 22, "bold")).pack(pady=18)

        val = tk.StringVar()
        tk.Entry(self.frame, textvariable=val,
                 font=("Segoe UI", 20), justify="center").pack(pady=10)

        def confirm():
            try:
                amt = float(val.get())
                if amt <= 0:
                    raise ValueError

                if mode == "WITHDRAW":
                    if amt > self.acc.balance:
                        self.flash_error("NO FUNDS")
                        return
                    amt = -amt

                self.acc.balance += amt
                self.acc.log(mode, amt)
                self.receipt()
            except:
                self.flash_error("INVALID AMOUNT")

        self.button("CONFIRM", confirm)
        self.button("BACK", self.menu, ghost=True)

    # ========== RECEIPT / TRANSACTIONS ==========
    def receipt(self):
        self.screen()

        tk.Label(self.frame, text="RECEIPT", fg=TXT, bg=CARD,
                 font=("Segoe UI", 22, "bold")).pack(pady=10)

        lines = self.acc.tx[-8:] if self.acc.tx else ["NO TRANSACTIONS"]
        for line in lines:
            tk.Label(self.frame, text=line, fg=TXT, bg=CARD,
                     font=("Consolas", 11)).pack(anchor="w", padx=10)

        tk.Label(self.frame, text=f"BALANCE: €{self.acc.balance:.2f}",
                 fg=SUB, bg=CARD, font=("Segoe UI", 14)).pack(pady=14)

        self.after(2200, self.menu)

    # ========== HELPERS ==========
    def button(self, txt, cmd, danger=False, ghost=False):
        bg = ERR if danger else BTN
        fg = TXT
        if ghost:
            bg = CARD
            fg = SUB
        tk.Button(self.frame, text=txt, command=cmd,
                  bg=bg, fg=fg,
                  font=("Segoe UI", 13, "bold"),
                  bd=0, height=2).pack(fill="x", pady=6)

    def flash_error(self, msg):
        lbl = tk.Label(self.frame, text=msg, fg=ERR, bg=CARD,
                       font=("Segoe UI", 12, "bold"))
        lbl.pack(pady=(8, 0))
        self.after(1300, lbl.destroy)

# ================= RUN =================

if __name__ == "__main__":
    ATM().mainloop()