from database import get_connection

class UnitOfWork:
    def __enter__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()
