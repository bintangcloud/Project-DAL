import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from repositories.pembayaran_rep import pembayaran_rep

class PembayaranGUI:
    def __init__(self):
        self.repo = pembayaran_rep()

        self.window = tk.Toplevel()
        self.window.title("Pembayaran")
        self.window.geometry("400x400")

        tk.Label(self.window, text="ID Pembayaran").pack()
        self.e_id = tk.Entry(self.window)
        self.e_id.pack()

        tk.Label(self.window, text="Jenis Pembayaran").pack()
        self.e_jenis = tk.Entry(self.window)
        self.e_jenis.pack()

        tk.Button(self.window, text="Simpan", command=self.create).pack(pady=10)
        tk.Button(self.window, text="Lihat Semua", command=self.show_all).pack()

        self.output = tk.Text(self.window, height=10)
        self.output.pack(pady=10)

    def create(self):
        try:
            self.repo.create(self.e_id.get(), self.e_jenis.get())
            messagebox.showinfo("Sukses", "Metode pembayaran ditambahkan!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_all(self):
        data = self.repo.get_all()
        self.output.delete(1.0, tk.END)
        for d in data:
            self.output.insert(tk.END, f"{d}\n")
