import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from repositories.kasir_rep import kasir_rep

class KasirGUI:
    def __init__(self):
        self.repo = kasir_rep()

        self.window = tk.Toplevel()
        self.window.title("Kasir")
        self.window.geometry("400x400")

        tk.Label(self.window, text="ID Kasir").pack()
        self.e_id = tk.Entry(self.window)
        self.e_id.pack()

        tk.Label(self.window, text="Nama Kasir").pack()
        self.e_nama = tk.Entry(self.window)
        self.e_nama.pack()

        tk.Button(self.window, text="Simpan", command=self.create).pack(pady=10)
        tk.Button(self.window, text="Lihat Semua", command=self.show_all).pack()

        self.output = tk.Text(self.window, height=10)
        self.output.pack(pady=10)

    def create(self):
        try:
            self.repo.create(
                self.e_id.get(),
                self.e_nama.get()
            )
            messagebox.showinfo("Sukses", "Data kasir berhasil ditambahkan!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_all(self):
        data = self.repo.get_all()
        self.output.delete(1.0, tk.END)

        for d in data:
            self.output.insert(tk.END, f"{d}\n")
