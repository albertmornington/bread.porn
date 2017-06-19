from db.helpers import fields_as_dict

INGREDIENT_FIELDS = ('type', 'name', 'amount', 'unit')

def ingredients_from_id(r, i):
    ingredients_key = 'ingredients:{}'.format(i)
    if not r.exists(ingredients_key):
        return None

    ingredient_id_list = r.lrange(ingredients_key, 0, -1)
    return filter(
        lambda x: x is not None,
        [ingredient_from_id(r, j) for j in ingredient_id_list]
    )

def ingredient_from_id(r, i):
    ingredient_key = 'ingredient:{}'.format(i)
    if not r.exists(ingredient_key):
        return None
    
    return fields_as_dict(r, ingredient_key, INGREDIENT_FIELDS)
