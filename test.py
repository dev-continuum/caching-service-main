import unittest
import redis
from lambda_function import get_it, cache_it, redis_client


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:

        self.dummy_data = [{"name": "abhishek"}, {"booking_id": "ghkdhgkhdkghd"}]

    def test_caching(self):
        cache_it(self.dummy_data)

    def test_get(self):
        response = get_it("booking_id").decode()
        self.assertEqual(response, "ghkdhgkhdkghd")


if __name__ == '__main__':
    unittest.main()
