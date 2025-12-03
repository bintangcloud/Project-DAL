from uow import UnitOfWork

class transaksi_ruangan_rep:

    def get_by_transaksi(self, id_transaksi):
        with UnitOfWork() as db:
            db.execute(
                "SELECT * FROM tabel_transaksi_ruangan WHERE id_transaksi=%s",
                (id_transaksi,)
            )
            return db.fetchall()
