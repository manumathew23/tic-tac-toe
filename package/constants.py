empty_grid = """

    |     |    
 1  |  2  |  3 
    |     |    
---------------
    |     |    
 4  |  5  |  6 
    |     |    
---------------
    |     |    
 7  |  8  |  9 
    |     |    

"""

player1_player2_input_map = {
    'x': 'o',
    "o": 'x'
}

game_tuple_indexes = (
    (1, 2, 3),
    (1, 5, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (3, 5, 7),
    (4, 5, 6),
    (7, 8, 9),

)

swtich_player = {
    0: 1,
    1: 0
}