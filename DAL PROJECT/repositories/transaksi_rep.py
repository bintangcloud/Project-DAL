from uow import UnitOfWork

class transaksi_rep:

    def buat_transaksi(self, data):
        with UnitOfWork() as db:
            db.callproc("sp_buat_transaksi", (
                data["id_transaksi"],
                data["tanggal"],
                data["id_pelanggan"],
                data["id_kasir"],
                data["id_pembayaran"],
                data["token_wifi"],
                data["id_ruangan"],
                data["mulai"],
                data["selesai"],
                data["id_item"],
                data["qty"]
            ))

    def get_header_laporan(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM v_laporan_transaksi_header")
            return db.fetchall()

    def hitung_total(self, id_transaksi):
        with UnitOfWork() as db:
            db.execute(
                "SELECT fn_total_transaksi(%s) AS total",
                (id_transaksi,)
            )
            return db.fetchone()["total"]
