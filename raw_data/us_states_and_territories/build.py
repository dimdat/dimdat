import json
import os
import pandas as pd

cols = [
    'iso_3166',
    'ansi_alphabetic_code',
    'ansi_numeric_code',
    'usps_code',
    'uscg_code',
    'gpo_abbrev',
    'ap_abbrev',
    'capital',
    'established_date',
    'total_square_miles',
    'total_square_kilometers',
    'land_square_miles',
    'land_square_kilometers',
    'water_square_miles',
    'water_square_kilometers',
]

other_data = {
    "title": "US States list",
    "route": "us_states",
    "columns": ["name"],
    "includes_any":[{"column": "is_state", "value": 1}]
}

def format_data(col, md):
    return {
        'title': 'US States and {}'.format(md['description']),
        'route': 'us_states_and_{}'.format(md['title']),
        'columns': ['name', col],
        'includes_any':[{'column': 'is_state', 'value': 1}]
    }

def main():
    df = pd.read_csv('raw_data/us_states_and_territories/raw_data.csv')

    with open('raw_data/us_states_and_territories/metadata.json', 'r') as fp:
        metadata = json.load(fp)

    builddata = [format_data(col, metadata[col]) for col in cols] + [other_data]
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('builddata.json', 'w') as fp:
        json.dump(builddata, fp)
    print 'Wrote builddata.json for states'

if __name__ == '__main__':
    main()
