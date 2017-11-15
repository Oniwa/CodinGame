def horse_race(horses):
    min_dif = 10000000
    result = None

    horses.sort()

    for i, val in enumerate(horses):
        if i < len(horses) - 1:
            diff = horses[i + 1] - horses[i]
            if diff < min_dif:
                min_dif = diff
                result = diff

    return result
