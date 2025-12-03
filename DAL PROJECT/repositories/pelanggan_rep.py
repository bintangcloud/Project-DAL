from uow import UnitOfWork

class pelanggan_rep:

    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_pelanggan")
            return db.fetchall()

    def create(self, id_pel, nama, nohp):
        with UnitOfWork() as db:
            db.execute("INSERT INTO tabel_pelanggan VALUES (%s, %s, %s)",
                       (id_pel, nama, nohp))

    def update(self, id_pel, nama, nohp):
        with UnitOfWork() as db:
            db.execute("""
                UPDATE tabel_pelanggan 
                SET nama_pelanggan=%s, no_telepon=%s
                WHERE id_pelanggan=%s
            """, (nama, nohp, id_pel))

    def delete(self, id_pel):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_pelanggan WHERE id_pelanggan=%s",
                       (id_pel,))
