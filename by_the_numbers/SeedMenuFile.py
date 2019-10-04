import json

def seedmenufile():
    """
    
    :return: 
    """

    menu = {}
    cheeseburger = {}
    hamandcheese = {}
    tunafish = {}
    a = {}
    b = {}
    c = {}

    """
        UTILITY => item template detail
        
        1:{'component':'',
                'quantity': 0,
                'prep': '',
                'degree': ''},      
    """

    a= dict({1:{'component':'Kaiser roll',
                'quantity': 0.5,
                'prep': 'toasted',
                'degree': 'medium'},
             2: { 'component': 'cheddar',
                  'quantity': 1 },
             3 : {'component': 'hamburger',
                  'quantity': 1,
                  'prep': 'grilled',
                  'degree': 145},
             4: {'component':'Kaiser roll',
                'quantity': 0.5,
                'prep': 'toasted',
                'degree': 'light'}}
            )

    b= dict({1: {'component':'brioche',
                'quantity': 1},
            2: {'component': 'jarslburg',
                  'quantity': 2},
            3: {'component': 'ham',
                'quantity': 1
                },
            4:{'component':'brioche',
                'quantity': 1}}
            )

    c= dict({1:{'component':'white bread',
                'quantity': 1,
                'prep': 'toasted',
                'degree': 'medium'},
            2: {'component': 'bacon',
                  'quantity': 4},
            3: {'component': 'chedder',
                'quantity': 1},
            4: {'component': 'tomato',
                'quantity': 2},
            5: {'component': 'tuna',
                 'quantity': 4},
            6: {'component':'white bread',
                'quantity': 1,
                'prep': 'toasted',
                'degree': 'medium'}
            }
            )


    #for key in a: print(key)

    #for p_item, p_info in a.items():
    #    print("\nItem Info:", p_info)


    menu = {'cheeseburger' : a}
    menu['hamandcheese'] = b
    menu['tunafish'] = c

    #for p_item, p_components in menu.items():
    #    print("\nItem Info:", p_item,'  uses', p_components)

    jstring = json.dumps(menu, sort_keys = True, indent = 4)

    print (jstring)

if __name__ == "__main__":
        seedmenufile()