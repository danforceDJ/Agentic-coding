"""Unit tests for the local weather MCP example."""

import unittest

from server import check_weather


class CheckWeatherTestCase(unittest.TestCase):
    def test_returns_mocked_city_weather(self) -> None:
        response = check_weather("Berlin", "c")
        self.assertEqual(response["city"], "Berlin")
        self.assertEqual(response["unit"], "c")
        self.assertEqual(response["temperature"], 13.0)
        self.assertEqual(response["condition"], "Cloudy")

    def test_returns_unknown_city_response(self) -> None:
        response = check_weather("Unknownopolis", "c")
        self.assertEqual(response["temperature"], 0.0)
        self.assertEqual(response["condition"], "Unknown city (mock dataset)")

    def test_rejects_empty_city(self) -> None:
        with self.assertRaises(ValueError):
            check_weather("   ", "c")

    def test_rejects_invalid_unit(self) -> None:
        with self.assertRaises(ValueError):
            check_weather("Berlin", "kelvin")

    def test_converts_to_fahrenheit(self) -> None:
        response = check_weather("Berlin", "f")
        self.assertEqual(response["temperature"], 55.4)


if __name__ == "__main__":
    unittest.main()
