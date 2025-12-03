import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from repositories.fnb_rep import fnb_rep
from repositories.vendor_rep import vendor_rep

class FnbGUI:
    def __init__(self):
        self.repo = fnb_rep()
        self.vendor_repo = vendor_rep()

        self.window = tk.Toplevel()
        self.window.title("FNB")
        self.window.geometry("450x450")

        tk.Label(self.window, text="ID Item").pack()
        self.e_id = tk.Entry(self.window)
        self.e_id.pack()

        tk.Label(self.window, text="Nama Item").pack()
        self.e_nama = tk.Entry(self.window)
        self.e_nama.pack()

        tk.Label(self.window, text="Harga").pack()
        self.e_harga = tk.Entry(self.window)
        self.e_harga.pack()

        tk.Label(self.window, text="ID Vendor").pack()
        self.e_vendor = tk.Entry(self.window)
        self.e_vendor.pack()

        tk.Button(self.window, text="Simpan", command=self.create).pack(pady=10)
        tk.Button(self.window, text="Lihat Semua", command=self.show_all).pack()
        tk.Button(self.window, text="Lihat Vendor", command=self.show_vendor).pack()

        self.output = tk.Text(self.window, height=10)
        self.output.pack(pady=10)

    def create(self):
        try:
            self.repo.create(
                self.e_id.get(),
                self.e_nama.get(),
                self.e_harga.get(),
                self.e_vendor.get()
            )
            messagebox.showinfo("Sukses", "Item FNB ditambahkan!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_all(self):
        data = self.repo.get_all()
        self.output.delete(1.0, tk.END)
        for d in data:
            self.output.insert(tk.END, f"{d}\n")

    def show_vendor(self):
        data = self.vendor_repo.get_all()
        self.output.delete(1.0, tk.END)
        for d in data:
            self.output.insert(tk.END, f"Vendor: {d}\n")
