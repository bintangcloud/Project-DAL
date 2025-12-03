from uow import UnitOfWork

class vendor_rep:
    
    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_vendor")
            return db.fetchall()

    def create(self, id, nama):
        with UnitOfWork() as db:
            db.execute("INSERT INTO tabel_vendor VALUES (%s, %s)",
                       (id, nama))

    def update(self, id, nama):
        with UnitOfWork() as db:
            db.execute(
                "UPDATE tabel_vendor SET nama_vendor=%s WHERE id_vendor=%s",
                (nama, id)
            )

    def delete(self, id):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_vendor WHERE id_vendor=%s", (id,))
