import json
import os
import pandas as pd

def format_data(state):
    return {
        'title': 'Counties in {}'.format(state),
        'route': 'counties_in_{}'.format(state.replace(' ', '_').lower()),
        'columns': ['county'],
        'includes_any':[{'column': 'state', 'value': state}]
    }

def main():
    df = pd.read_csv('raw_data/counties_by_us_states/raw_data.csv')
    states = set(df['state'])
    builddata = [format_data(state) for state in states]
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('builddata.json', 'w') as fp:
        json.dump(builddata, fp)
    print 'Wrote builddata.json for counties by us states'

if __name__ == '__main__':
    main()
