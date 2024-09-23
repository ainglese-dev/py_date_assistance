import pytz
from datetime import datetime
from logo import logo  # Importing from logo.py
from countries import latam_country_codes, country_flags, country_timezones_to_exclude  # Importing from countries.py

class EventScheduler:
    def __init__(self):
        self.event_name = ""
        self.event_date = ""
        self.event_time = ""
        self.origin_country_code = ""
        self.localized_event_datetime = None
        self.timezone_dict = {}

    def get_event_details(self):
        print("\nPlease enter the event details:\n")
        self.event_name = input("Enter the name of the event: ")
        self.event_date = input("Enter the date of the event (YYYY-MM-DD): ")
        self.event_time = input("Enter the time of the event (HH:MM AM/PM): ")
        self.origin_country_code = input("Enter the origin country code (e.g., CO for Colombia): ")

    def combine_date_time(self):
        event_datetime_str = f"{self.event_date} {self.event_time}"
        event_datetime = datetime.strptime(event_datetime_str, '%Y-%m-%d %I:%M %p')
        origin_timezone = pytz.country_timezones[self.origin_country_code][0]
        origin_tz = pytz.timezone(origin_timezone)
        self.localized_event_datetime = origin_tz.localize(event_datetime)

    def populate_timezone_dict(self):
        for country_code in latam_country_codes:
            if country_code not in country_timezones_to_exclude:
                main_timezone = pytz.country_timezones[country_code][0]
                tz = pytz.timezone(main_timezone)
                localized_time = self.localized_event_datetime.astimezone(tz).strftime('%I:%M %p')
                self.add_to_timezone_dict(localized_time, country_code)

    def add_to_timezone_dict(self, localized_time, country_code):
        if localized_time not in self.timezone_dict:
            self.timezone_dict[localized_time] = set()
        self.timezone_dict[localized_time].add(country_code)

    def sort_timezones(self):
        return sorted(self.timezone_dict.items())

    def print_event_details(self):
        print("\nEvent Details:")
        print(f"  Event name: {self.event_name}")
        print(f"  Original country ({self.origin_country_code}), date and time: {self.localized_event_datetime.strftime('%Y-%m-%d %I:%M %p %Z')}\n")
        print("Converted Times:")
        sorted_timezones = self.sort_timezones()
        for localized_time, countries in sorted_timezones:
            country_emojis = [country_flags[country] for country in sorted(countries)]
            print(f"  {localized_time} | {', '.join(country_emojis)}")
        print("\n")

if __name__ == "__main__":
    print(logo)
    scheduler = EventScheduler()
    scheduler.get_event_details()
    scheduler.combine_date_time()
    scheduler.populate_timezone_dict()
    scheduler.print_event_details()
