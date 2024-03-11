cats = 100
circles = 100


def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    for circle in range(1, circles + 1):
        for cat in range(circle - 1, cats, circle):
            if not array_of_cats[cat]:
                array_of_cats[cat] = True
            else:
                array_of_cats[cat] = False
    for cat in range(cats):
        if array_of_cats[cat]:
            cats_with_hats_on.append(cat + 1)
    return cats_with_hats_on


cats_with_hats = [False] * cats
print(get_cats_with_hats(cats_with_hats))
