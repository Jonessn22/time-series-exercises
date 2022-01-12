'''
Module created to make work from Time Series >> Acquire Lesson reproducible.<br>
Link to exercises ---> https://github.com/Jonessn22/time-series-exercises/blob/8a63149aa59a46e633cc70e609fbd76b4a649808/01b_acquisition_exercises.ipynb'>here</a>
'''

import requests

def API_doc(base_url):
    '''
THIS FUNCTION TAKES IN A BASE URL AND PRINTS THE API DOCUMENTATION. YOU CAN USE IT TO LOOK AT THE
URL's ENDPOINTS.    
    '''

    response = requests.get(base_url + '/documentation')
    print(response.json()['payload'])


def get_stores(url1, url2, url3, baseurl):
    '''
    
    '''

    #url1 | ITEMS DATA 
    response = requests.get(url1)
    data = response.json()
    df = pd.DataFrame(data['payload']['items'])

    while data['payload']['next_page'] != None:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload']['items'])]).reset_index(drop = True)

    df_items = df.copy
    print('Items data acquired ✔✅')

    #url2 | STORES DATA
    response = requests.get(url2)

    #url3 | SALES DATA
    response = requests.get(url3)

