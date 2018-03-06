#!/usr/bin/env python3
import unittest
import os
import json
import tempfile
from datetime import datetime
from app import create_app
from db_setup import init_db

class BookingsTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_filename = tempfile.mkstemp()
        self.db_uri = 'sqlite:///' + self.db_filename
        init_db(self.db_uri)
        self.app = create_app(self.db_uri)
        self.client = self.app.test_client()
        self.booking = dict(
            user_id=1,
            amount=100,
            merchant_id=1,
            book_date='201801010000',
            flight_origin='Paris',
            flight_dest='Tokyo',
            flight_date='201801010000',
            flight_nr=123456789
        )

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_filename)

    def test_default_endpoint(self):
        """Test default service endpoint"""
        resp = self.client.get('/')
        assert(b'info' in resp.data)
        assert(b'Simple flight booking service.' in resp.data)
    
    def test_commit_booking(self):
        """Test commiting a booking"""
        resp = self.client.post('/commit', data=json.dumps(self.booking), content_type='application/json')
        assert(b'success' in resp.data)
        assert(b'1' in resp.data)

    def test_get_bookings(self):
        """Test getting bookings list of user"""
        resp = self.client.post('/commit', data=json.dumps(self.booking), content_type='application/json')
        resp = self.client.get('/bookings/' + str(self.booking['user_id']))
        assert(b'123456789' in resp.data)

if __name__ == '__main__':
    unittest.main()
