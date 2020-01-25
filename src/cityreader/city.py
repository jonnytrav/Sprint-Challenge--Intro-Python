class City():
    def __init__(self, city, state_name, county_name, lat, lng, population, density, timezone, zips):
        self.city = city
        self.state_name = state_name
        self.county_name = county_name
        self.lat = lat
        self.lng = lng
        self.population = population
        self.density = density
        self.timezone = timezone
        self.zips = zips

    def __str__(self):
        return f"{self}"
