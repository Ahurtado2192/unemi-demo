from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    """Clase que representa la tabla Student en la base de datos."""
    
    # Definición de columnas
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    career = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        """Método para representar la instancia de Student."""
        return f"Student(id={self.id}, name={self.name}, last_name={self.last_name}, age={self.age}, phone={self.phone}, address={self.address}, career={self.career}, is_active={self.is_active})"
