from uow import UnitOfWork

class ruangan_rep:
    
    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_ruangan")
            return db.fetchall()

    def create(self, id, nama, harga):
        with UnitOfWork() as db:
            db.execute(
                "INSERT INTO tabel_ruangan VALUES (%s, %s, %s)",
                (id, nama, harga)
            )

    def update(self, id, nama, harga):
        with UnitOfWork() as db:
            db.execute(
                "UPDATE tabel_ruangan SET nama_ruangan=%s, harga_per_jam=%s WHERE id_ruangan=%s",
                (nama, harga, id)
            )

    def delete(self, id):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_ruangan WHERE id_ruangan=%s", (id,))
