"""Local MCP server example with one tool: check_weather."""

from __future__ import annotations

from typing import TypedDict

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-weather")


class WeatherResponse(TypedDict):
    city: str
    unit: str
    temperature: float
    condition: str
    source: str


MOCK_WEATHER_C = {
    "berlin": {"temperature": 13.0, "condition": "Cloudy"},
    "tokyo": {"temperature": 21.0, "condition": "Clear"},
    "nairobi": {"temperature": 24.0, "condition": "Sunny"},
    "sao paulo": {"temperature": 19.0, "condition": "Rain"},
}


@mcp.tool()
def check_weather(city: str, unit: str = "c") -> WeatherResponse:
    """Return mocked weather data for a city.

    Args:
        city: City name from the local mock dataset.
        unit: Temperature unit, either "c" (celsius) or "f" (fahrenheit).

    Returns:
        A weather object with city, unit, temperature, condition, and source fields.

    Raises:
        ValueError: If city is empty or unit is not "c" or "f".
    """
    normalized_city = city.strip().lower()
    normalized_unit = unit.strip().lower()

    if not normalized_city:
        raise ValueError("city is required")
    if normalized_unit not in {"c", "f"}:
        raise ValueError("unit must be 'c' or 'f'")

    weather = MOCK_WEATHER_C.get(normalized_city)
    if weather is None:
        return {
            "city": city.strip(),
            "unit": normalized_unit,
            "temperature": 0.0,
            "condition": "Unknown city (mock dataset)",
            "source": "local-mock",
        }

    temperature_c = weather["temperature"]
    temperature = temperature_c if normalized_unit == "c" else (temperature_c * 9 / 5) + 32

    return {
        "city": city.strip(),
        "unit": normalized_unit,
        "temperature": round(temperature, 1),
        "condition": weather["condition"],
        "source": "local-mock",
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
