STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

def isValidBoard(boardDictionary):
    valid = True
    bK = 0
    wK = 0


    black_player = {'total':0, 'pawn':0}
    white_player = {'total':0, 'pawn':0}

    for v in boardDictionary.values():
        if v == 'bK':
            bK += 1
        elif v == 'wK':
            wK += 1
    if bK > 1 or wK > 1:
        print('King is more than 1')
        valid = False

    for i in boardDictionary.values():
        if i[0] != 'w' and i[0] != 'b':
            print('Invalid piece prefix: ' +str(i))
            valid = False


    for v in boardDictionary.values():
        if v[0] == 'w':
            white_player['total'] += 1
        elif v[0] == 'b':
            black_player['total'] += 1

        if v == 'wP':
            white_player['pawn'] += 1
        elif v == 'bP':
            black_player['pawn'] += 1

    if black_player['total'] > 16 or white_player['total'] > 16:
        print('Number of pieces each player must be 16!')
        valid = False
    if black_player['pawn'] > 8 or white_player['pawn'] > 8:
        print('Number of pawns cant be more that 8 for each player!')
        valid = False

    for l,n in boardDictionary.keys():
        if l not in 'abcdefgh':
            print('Prefix of board should be valid: ' +str(l))
            valid = False
        if n not in '12345678':
            print('Prefix of board should be valid: ' +str(n))
            valid=False




    return valid







