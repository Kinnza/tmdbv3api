# -*- coding: utf-8 -*-

import unittest
import os
import math
from tmdbv3api import TMDb, Movie, Discover, TV, Person, Collection, Company


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['api_key']
        self.movie = Movie()
        self.discover = Discover()
        self.tv = TV()
        self.person = Person()
        self.collection = Collection()
        self.company = Company()

    def test_get_movie(self):
        movie = self.movie.details(111)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'Scarface')
        self.assertEqual(movie.id, 111)
        self.assertTrue(hasattr(movie, 'title'))
        self.assertTrue(hasattr(movie, 'overview'))
        self.assertTrue(hasattr(movie, 'id'))

    def test_get_movie_reviews(self):
        search = self.movie.search("Mad Max")
        self.assertTrue(len(search) > 0)
        first = search[0]
        reviews = self.movie.reviews(first.id)
        self.assertTrue(len(reviews) > 0)
        for review in reviews:
            self.assertTrue(hasattr(review, 'id'))
            self.assertTrue(hasattr(review, 'content'))

    def test_get_movie_lists(self):
        lists = self.movie.lists(111)
        self.assertTrue(len(lists) > 0)
        self.assertTrue(hasattr(lists[0], 'description'))
        self.assertTrue(hasattr(lists[0], 'name'))

    def test_get_movie_videos(self):
        videos = self.movie.videos(111)
        self.assertTrue(len(videos) > 0)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        recs = self.movie.recommendations(111)
        self.assertTrue(len(recs) > 0)
        self.assertTrue(hasattr(recs[0], 'id'))

    def test_discover_movies(self):
        discover = self.discover.discover_movies({
            'primary_release_year': '2015',
            'with_genres': '28',
            'page': '1',
            'vote_average.gte': '8'

        })

        self.assertTrue(len(discover) > 0)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]

        has_genre = False
        for genre_id in movie.genre_ids:
            if genre_id == 28:
                has_genre = True
        self.assertTrue(math.ceil(movie.vote_average) >= 8)
        self.assertTrue(has_genre)

    def test_discover_tv_shows(self):
        discover = self.discover.discover_tv_shows({
            'with_genres': '16',
            'vote_average.gte': '8',
            'page': '1'
        })
        self.assertTrue(len(discover) > 0)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]
        has_genre = False
        for genre_id in movie.genre_ids:
            if genre_id == 16:
                has_genre = True
        self.assertTrue(math.ceil(movie.vote_average) >= 8)
        self.assertTrue(has_genre)

    def test_get_latest_movie(self):
        videos = self.movie.latest()
        self.assertIsNotNone(videos)
        self.assertTrue(hasattr(videos, 'id'))

    def test_now_playing(self):
        now_playing = self.movie.now_playing()
        self.assertTrue(len(now_playing) > 0)
        self.assertTrue(hasattr(now_playing[0], 'id'))

    def test_top_rated(self):
        top_rated = self.movie.top_rated()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_upcoming(self):
        upcoming = self.movie.upcoming()
        self.assertTrue(len(upcoming) > 0)
        self.assertTrue(hasattr(upcoming[0], 'id'))

    def test_popular(self):
        popular = self.movie.popular()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_search(self):
        search = self.movie.search('Mad Max')
        self.assertTrue(len(search) > 0)
        self.assertTrue(hasattr(search[0], 'id'))

    def test_similar(self):
        similar = self.movie.similar(111)
        self.assertTrue(len(similar) > 0)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_get_tv_show(self):
        show = self.tv.details(12)
        self.assertIsNotNone(show)
        self.assertTrue(hasattr(show, 'id'))

    def test_get_latest_tv_show(self):
        latest_tv = self.tv.latest()
        self.assertIsNotNone(latest_tv)
        self.assertTrue(hasattr(latest_tv, 'id'))

    def test_search_tv(self):
        search_tv = self.tv.search('Sunny')
        self.assertTrue(len(search_tv) > 0)
        self.assertTrue(hasattr(search_tv[0], 'id'))

    def test_popular_shows(self):
        popular = self.tv.popular()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_top_rated_shows(self):
        top_rated = self.tv.top_rated()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_get_person(self):
        person = self.person.details(234)
        self.assertIsNotNone(person)
        self.assertTrue(hasattr(person, 'id'))

    def test_search_person(self):
        search_person = self.person.search('Bryan')
        self.assertTrue(len(search_person) > 0)
        self.assertTrue(hasattr(search_person[0], 'id'))

    def test_collection_details(self):
        c = Collection()
        details = c.details(10)
        self.assertEquals(details.name, 'Star Wars Collection')
        self.assertEquals(details.id, 10)
        self.assertTrue(hasattr(details, 'overview'))
        self.assertTrue(hasattr(details, 'poster_path'))

    def test_collection_images(self):
        c = Collection()
        images = c.images(10)
        self.assertTrue(hasattr(images, 'backdrops'))
        self.assertTrue(hasattr(images, 'posters'))

    def test_popular_people(self):
        popular = self.person.popular()
        self.assertTrue(len(popular) > 0)
        first = popular[0]
        self.assertTrue(hasattr(first, 'name'))
        self.assertTrue(hasattr(first, 'known_for'))

    def test_latest_person(self):
        latest_person = self.person.latest()
        self.assertIsNotNone(latest_person)
        self.assertTrue(hasattr(latest_person, 'name'))
        self.assertTrue(hasattr(latest_person, 'id'))

    def test_person_images(self):
        images = self.person.images(11)
        self.assertIsNotNone(images)
        self.assertTrue(hasattr(images, 'profiles'))
        self.assertTrue(hasattr(images, 'id'))

    def test_company_details(self):
        c = self.company.details(1)
        self.assertTrue(hasattr(c, 'name'))
        self.assertEquals(c.name, 'Lucasfilm')

    def test_company_movies(self):
        company = self.company.movies(1)
        self.assertTrue(len(company) > 0)
        first = company[0]
        self.assertTrue(hasattr(first, 'title'))
        self.assertTrue(hasattr(first, 'overview'))
