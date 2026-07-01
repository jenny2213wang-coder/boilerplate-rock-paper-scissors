def player(prev_play, opponent_history=[]):
    if not hasattr(player, 'pattern_dict'):
        player.pattern_dict = {}
        player.history = []

    if prev_play:
        player.history.append(prev_play)

    # 1. update
    for n in range(3, 6):
        if len(player.history) >= n:
            pattern = "".join(player.history[-n:])
            prefix = pattern[:-1]
            last_move = pattern[-1]
            
            key = (n, prefix) # use (n, prefix) as key
            if key not in player.pattern_dict:
                player.pattern_dict[key] = {'R': 0, 'P': 0, 'S': 0}
            player.pattern_dict[key][last_move] += 1

    # 2. predict
    for n in range(5, 2, -1): # from 5 to 3
        prefix = "".join(player.history[-(n-1):])
        key = (n, prefix)
        
        if key in player.pattern_dict:
            counts = player.pattern_dict[key]
            # find the most requent one
            prediction = max(counts, key=counts.get)
            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
            return ideal_response[prediction]

    return "R" 
