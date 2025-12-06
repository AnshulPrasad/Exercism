def resistor_label(colors):
    color_band = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }

    tolerance_band = {
        "grey": "0.05",
        "violet": "0.1",
        "blue": "0.25",
        "green": "0.5",
        "brown": "1",
        "red": "2",
        "gold": "5",
        "silver": "10",
    }
    ans = ""
    if len(colors) == 1:
        return f"{color_band[colors[0]]} ohms"
    elif len(colors) == 2:
        return f"{color_band[colors[0]]}{color_band[colors[1]]} ohms"
    elif len(colors) == 3:
        return f"{color_band[colors[0]]}{color_band[colors[1]]}{color_band[colors[2]]} ohms"

    for i in colors[:-2]:
        ans += color_band[i]
    ans += "0" * int(color_band[colors[-2]])

    if len(ans) <= 3:
        return f"{ans} ohms ±{tolerance_band[colors[-1]]}%"
    elif 3 < len(ans) <= 6:
        return f"{int(ans)/1000:g} kiloohms ±{tolerance_band[colors[-1]]}%"
    elif 6 < len(ans) <= 9:
        return f"{int(ans)/1000000:g} megaohms ±{tolerance_band[colors[-1]]}%"
