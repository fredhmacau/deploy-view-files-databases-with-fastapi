import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from databases import Database


connection_string = "sqlite:///store.db"
db = Database(connection_string)
engine = _sql.create_engine(connection_string, encoding="utf-8", echo=True)
Base = _orm.declarative_base()
Session = _orm.sessionmaker(bind=engine)


class Image(Base):
    __tablename__ = "imgs"
    id = _sql.Column(
        _sql.Integer, autoincrement=True, primary_key=True, comment="id image"
    )
    name = _sql.Column(_sql.String(80), nullable=False, comment="name image")
    img = _sql.Column(_sql.LargeBinary, nullable=False, comment="img")
    content_type = _sql.Column(_sql.String(80), nullable=False, comment="type img")

    def __repr__(self) -> str:
        return f"<Image id={self.id} name={self.name}>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
