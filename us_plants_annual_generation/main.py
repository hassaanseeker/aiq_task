from flask import Flask, render_template, request, jsonify
import pandas as pd


app=Flask(__name__)

state_dict = {'00':'ALL',
    '01': 'AL',
 '02': 'AK',
 '04': 'AZ',
 '05': 'AR',
 '06': 'CA',
 '08': 'CO',
 '09': 'CT',
 '10': 'DE',
 '11': 'DC',
 '12': 'FL',
 '13': 'GA',
 '15': 'HI',
 '16': 'ID',
 '17': 'IL',
 '18': 'IN',
 '19': 'IA',
 '20': 'KS',
 '21': 'KY',
 '22': 'LA',
 '23': 'ME',
 '30': 'MT',
 '31': 'NE',
 '32': 'NV',
 '33': 'NH',
 '34': 'NJ',
 '35': 'NM',
 '36': 'NY',
 '37': 'NC',
 '38': 'ND',
 '39': 'OH',
 '40': 'OK',
 '41': 'OR',
 '24': 'MD',
 '25': 'MA',
 '26': 'MI',
 '27': 'MN',
 '28': 'MS',
 '29': 'MO',
 '42': 'PA',
 '44': 'RI',
 '45': 'SC',
 '46': 'SD',
 '47': 'TN',
 '48': 'TX',
 '49': 'UT',
 '50': 'VT',
 '51': 'VA',
 '53': 'WA',
 '54': 'WV',
 '55': 'WI',
 '56': 'WY'}

def get_states_plants_data(state):
    """
    Function that generates the per state per plant annual net generation.
    """

    df_plants_anual_loc_v1 = pd.read_csv('/data/plants_final_data.csv', index_col=0)
    df_plants_anual_loc_v1 = df_plants_anual_loc_v1[df_plants_anual_loc_v1['Plant state abbreviation_x'] == state].reset_index(drop = True)

    markers = df_plants_anual_loc_v1.to_dict(orient='records')
    
    return markers

def get_top_n_states(n, state):
    """
    Function that generates per state top n plants.
    """

    df_plants_anual_loc_v1 = pd.read_csv('data/plants_final_data.csv', index_col=0)
    df_plants_anual_loc_v1 = df_plants_anual_loc_v1[df_plants_anual_loc_v1['Plant state abbreviation_x'] == state].reset_index(drop = True)

    df_plants_anual_loc_v1 = df_plants_anual_loc_v1.sort_values(by='plant_annual_generation', ascending=False).reset_index(drop=True).loc[0:n-1]
    markers = df_plants_anual_loc_v1.to_dict(orient='records')
    
    return markers


@app.route('/')
def root():
    """
    Function that returns all the plants for whole US.
    """

    df_plants_anual_loc = pd.read_excel('data/eGRID2021_data.xlsx', sheet_name='PLNT21')
    df_plants_anual_loc_v1 = df_plants_anual_loc[['Plant name', 'Plant latitude', 'Plant longitude']]
    df_plants_anual_loc_v1 = df_plants_anual_loc_v1.loc[1:].reset_index(drop = True)
    df_plants_anual_loc_v1.rename(columns = {'Plant name':'popup', 'Plant latitude':'lat', 'Plant longitude':'lon'},inplace=True)
    df_plants_anual_loc_v2 = df_plants_anual_loc_v1
    markers = df_plants_anual_loc_v2.to_dict(orient='records')
    
    return render_template('index_2.html',markers=markers )

@app.route('/zoom_to_state', methods=['POST'])
def zoom_to_state():
    """
    Function that returns the plants for state select on the UI.
    """
    selected_state = request.json.get('selected_state')
    # Do something with the selected state (e.g., process it, fetch data, etc.)
    # Here, I'm just echoing back the selected state for demonstration purposesx

    response = {
        'selected_state':selected_state ,
        'markers': get_states_plants_data(state_dict[selected_state])
    }
    return jsonify(response)

@app.route('/top_n_for_state', methods=['POST'])
def top_n_for_state():
    """
    Function that returns top n plants for the state and top n selected
    from the UI.
    """
    # Get the selected Top N value from the request
    selected_top_n = int(request.json.get('selected_top_n'))

    # Get the selected state from the request
    selected_state = request.json.get('selected_state')

    # Get all markers (replace this with your method to retrieve markers)
    all_markers = get_top_n_states(selected_top_n, state_dict[selected_state])
    
    return jsonify({'markers': all_markers})

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
