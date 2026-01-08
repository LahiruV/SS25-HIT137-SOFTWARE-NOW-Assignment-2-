"""
Holds constants used across the project months and seasons.
Keeping these in one place makes the project easier to maintain.
"""

# List of month columns expected in the CSV files
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Mapping of seasons to their corresponding months
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"],
}
