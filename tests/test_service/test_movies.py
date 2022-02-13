import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService



@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    film1 = Movie(id=1, title='Пирог', genre_id = 1, director_id = 1)
    film2 = Movie(id=2, title='Пирожок', genre_id = 1, director_id = 1)
    film3 = Movie(id=3, title='Пирожище', genre_id = 1, director_id = 1)

    movie_dao.get_one = MagicMock(return_value=film1)
    movie_dao.get_all = MagicMock(return_value=[film1, film2, film3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.partially_update = MagicMock()
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_create(self):
        movie_d = {
            "title": "Американский пирог"

        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Неамерикнский пирог"
        }
        self.movie_service.update(movie_d)

    def test_partially_update(self):
        movie_d = {
            "id": 3,
            "title": "Неамерикнский пирог 2"
        }

        self.movie_service.update(movie_d)