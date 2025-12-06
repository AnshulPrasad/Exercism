def score(x, y):
    radii = (x**2+y**2)**0.5
    if radii<=1: return 10
    elif 1<radii<=5: return 5
    elif 5<radii<=10: return 1
    else: return 0