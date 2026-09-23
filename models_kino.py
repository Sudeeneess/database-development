from datetime import date
from typing import List, Optional
from sqlalchemy import Column, Table, ForeignKey, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database_kino import Base

# film_actor
film_actor = Table(
    "film_actor",
    Base.metadata,
    Column("id_film", Integer, ForeignKey("films.id", ondelete="CASCADE"), primary_key=True),
    Column("id_actor", Integer, ForeignKey("actors.id", ondelete="CASCADE"), primary_key=True),
)

# actors
class Actor(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birthday: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    # Связь с фильмами
    films: Mapped[List["Film"]] = relationship(
        secondary=film_actor,
        back_populates="actors"
    )

# films
class Film(Base):
    __tablename__ = "films"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    poster: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Связь с актерами
    actors: Mapped[List["Actor"]] = relationship(
        secondary=film_actor,
        back_populates="films"
    )