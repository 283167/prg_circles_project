def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)

print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1


def basic_stats(values):
    return min(values), max(values), round(sum(values) / len(values), 2)
print(basic_stats([1200, 980, 1430, 1600, 890]))

min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
print(min_v, max_v, avg_v)


player_name = "GlobalPlayer"

def show_player():
    player_name = "LocalPlayer"
    print("ve funkci:", player_name)

show_player()
print("mimo funkci:", player_name)