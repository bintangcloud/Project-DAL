from uow import UnitOfWork

class fnb_rep:

    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_fnb")
            return db.fetchall()

    def create(self, id_item, nama_item, harga, id_vendor):
        with UnitOfWork() as db:
            db.execute(
                "INSERT INTO tabel_fnb VALUES (%s, %s, %s, %s)",
                (id_item, nama_item, harga, id_vendor)
            )

    def update(self, id_item, nama_item, harga, id_vendor):
        with UnitOfWork() as db:
            db.execute(
                """
                UPDATE tabel_fnb 
                SET nama_item=%s, harga=%s, id_vendor=%s 
                WHERE id_item=%s
                """,
                (nama_item, harga, id_vendor, id_item)
            )

    def delete(self, id_item):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_fnb WHERE id_item=%s", (id_item,))
