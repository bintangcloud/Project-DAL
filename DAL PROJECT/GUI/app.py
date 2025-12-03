import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from pelanggan_gui import PelangganGUI
from kasir_gui import KasirGUI
from ruangan_gui import RuanganGUI
from vendor_gui import VendorGUI
from fnb_gui import FnbGUI
from transaksi_gui import TransaksiGUI

root = tk.Tk()
root.title("DAL Project — Dago Management")
root.geometry("500x400")

def open_pelanggan():
    PelangganGUI()

def open_kasir():
    KasirGUI()

def open_ruangan():
    RuanganGUI()

def open_vendor():
    VendorGUI()

def open_fnb():
    FnbGUI()

def open_transaksi():
    TransaksiGUI()

tk.Label(root, text="Menu Utama", font=("Arial", 18)).pack(pady=20)

tk.Button(root, text="Data Pelanggan", width=20, command=open_pelanggan).pack(pady=5)
tk.Button(root, text="Data Kasir", width=20, command=open_kasir).pack(pady=5)
tk.Button(root, text="Data Ruangan", width=20, command=open_ruangan).pack(pady=5)
tk.Button(root, text="Data Vendor", width=20, command=open_vendor).pack(pady=5)
tk.Button(root, text="Data FNB", width=20, command=open_fnb).pack(pady=5)
tk.Button(root, text="Transaksi", width=20, command=open_transaksi).pack(pady=5)

root.mainloop()
