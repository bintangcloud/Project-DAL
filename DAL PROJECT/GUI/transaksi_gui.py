import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from repositories.transaksi_rep import transaksi_rep

class TransaksiGUI:
    def __init__(self):
        self.repo = transaksi_rep()

        self.window = tk.Toplevel()
        self.window.title("Transaksi")
        self.window.geometry("500x700")

        fields = [
            ("ID Transaksi", "id_transaksi"),
            ("Tanggal (YYYY-MM-DD HH:MM:SS)", "tanggal"),
            ("ID Pelanggan", "id_pelanggan"),
            ("ID Kasir", "id_kasir"),
            ("ID Pembayaran", "id_pembayaran"),
            ("Token Wifi", "token_wifi"),
            ("ID Ruangan", "id_ruangan"),
            ("Waktu Mulai (HH:MM:SS)", "mulai"),
            ("Waktu Selesai (HH:MM:SS)", "selesai"),
            ("ID Item FNB", "id_item"),
            ("Kuantitas", "qty")
        ]

        self.entries = {}

        for label, key in fields:
            tk.Label(self.window, text=label).pack()
            ent = tk.Entry(self.window)
            ent.pack()
            self.entries[key] = ent

        tk.Button(self.window, text="Buat Transaksi", command=self.buat_transaksi).pack(pady=10)
        tk.Button(self.window, text="Hitung Total", command=self.hitung_total).pack(pady=5)
        tk.Button(self.window, text="Lihat Laporan", command=self.lihat_laporan).pack(pady=5)

        self.output = tk.Text(self.window, height=20)
        self.output.pack(pady=10)

    def buat_transaksi(self):
        try:
            data = {k: v.get() for k, v in self.entries.items()}
            self.repo.buat_transaksi(data)
            messagebox.showinfo("Sukses", "Transaksi berhasil dibuat!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def hitung_total(self):
        try:
            id_transaksi = self.entries["id_transaksi"].get()
            total = self.repo.hitung_total(id_transaksi)
            messagebox.showinfo("Total", f"Total Transaksi: {total}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def lihat_laporan(self):
        rows = self.repo.get_laporan()
        self.output.delete(1.0, tk.END)
        for r in rows:
            self.output.insert(tk.END, f"{r}\n")
