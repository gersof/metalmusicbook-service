from models import Genres
# from initial_data import client_data, receipts_data, transaction_data, providers_data, products_data
from config import db


class GenresLogic:
    @classmethod
    def get_all_genres(cls):
        """
        Retrieves all the Genres inside the database
        Returns:
            List containing Genre instances.
        """
        return Genres.query.all()

    @classmethod
    def create(cls, data):
        """
        Creates a Genres instance and stores it into the database
        Args:
            data: Dict containing information about the Genres to be created

        Returns:
            Genres instance.
        """
        genre = Genres(**data)
        db.session.add(genre)
        db.session.commit()
        return genre
