from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Oppo(Base):
    __tablename__ = "handphone"

    brand : Mapped[str] = mapped_column(primary_key=True)
    ram : Mapped[str]
    prosesor : Mapped[str]
    storage : Mapped[str]
    baterai : Mapped[str]
    harga : Mapped[int]
    os : Mapped[str]

    def __repr__(self) -> str :
        return f"brand={self.brand}, ram={self.ram}, prosesor={self.prosesor}, storage={self.storage}, baterai={self.baterai}, harga={self.harga}, os={self.os}"

