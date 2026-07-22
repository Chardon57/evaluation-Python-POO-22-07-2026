from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

class Vehicle(db.Model):
    __tablename__="vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    universe: Mapped[str] = mapped_column(String(100), nullable=False)
    main_character: Mapped[str] = mapped_column(String(100), nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(15), nullable=False)
    has_night_lighting: Mapped[bool] = mapped_column(Boolean, nullable=False)
    image_url: Mapped[str] = mapped_column(String(100), nullable=True)
    notes: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self) -> dict:
        '''Cette méthode facilite la conversiont des attributs du modèle en dictionnaire et évite de répéter inutilement du code (DRY).
        Elle renvoie un dictionnaire'''
        return {
            "id": self.id,
            "name": self.name,
            "universe": self.universe,
            "main_character": self.main_character,
            "position": self.position,
            "status": self.status,
            "has_night_lighting": self.has_night_lighting,
            "image_url": f"https://example.com{self.image_url}", # Le nom de domaine 'example.com' est à remplacer par une adresse contenant les images
            "notes": self.notes
        }

    def from_body(self, body: dict):
        '''Cette méthode affecte aux attributs du modèle les valeurs correspondantes du body passé en paramètre. Elle reçoit en 
        paramètre un body de type dictionnaire'''
        self.name = body["name"]
        self.universe = body["universe"]
        self.main_character = body["main_character"]
        self.position = body["position"]
        self.status = body["status"]
        self.has_night_lighting = body["has_night_lighting"]
        self.image_url = body["image_url"]
        self.notes = body["notes"]