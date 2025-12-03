from uow import UnitOfWork

class pembayaran_rep:
    
    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_pembayaran")
            return db.fetchall()

    def create(self, id, jenis):
        with UnitOfWork() as db:
            db.execute("INSERT INTO tabel_pembayaran VALUES (%s, %s)",
                       (id, jenis))

    def update(self, id, jenis):
        with UnitOfWork() as db:
            db.execute(
                "UPDATE tabel_pembayaran SET jenis_pembayaran=%s WHERE id_pembayaran=%s",
                (jenis, id)
            )

    def delete(self, id):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_pembayaran WHERE id_pembayaran=%s", (id,))
