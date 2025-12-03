from uow import UnitOfWork

class kasir_rep:
    
    def get_all(self):
        with UnitOfWork() as db:
            db.execute("SELECT * FROM tabel_kasir")
            return db.fetchall()

    def create(self, id_kasir, nama):
        with UnitOfWork() as db:
            db.execute("INSERT INTO tabel_kasir VALUES (%s, %s)", 
                       (id_kasir, nama))

    def update(self, id_kasir, nama):
        with UnitOfWork() as db:
            db.execute("UPDATE tabel_kasir SET nama_kasir=%s WHERE id_kasir=%s",
                       (nama, id_kasir))

    def delete(self, id_kasir):
        with UnitOfWork() as db:
            db.execute("DELETE FROM tabel_kasir WHERE id_kasir=%s", 
                       (id_kasir,))
