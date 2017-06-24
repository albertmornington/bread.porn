from db.helpers import fields_as_dict

SCORE_FIELDS = ('sweetness', 'sourness', 'crust', 'texture', 'toasting')
VERDICT_FIELDS = ('sweetness', 'sourness', 'crust', 'texture', 'toasting', 'notes')


def verdict_from_id(r, i):
    """
    :param r: redis instance
    :param i: verdict id
    :returns: dict
    """
    verdict_key = 'verdict:{}'.format(i)
    if not r.exists(verdict_key):
        return None
    
    verdict = fields_as_dict(r, verdict_key, VERDICT_FIELDS)
    rating = 0
    for score_field in SCORE_FIELDS: 
        # converts (0, 1, 2, 3, 4, 5) to (0, 0.5, 1, 0.5, 0)
        score = (2 - abs(int(verdict[score_field]) - 2))/2.
        rating += score

    # 4. -> 4_0, 3.5 -> 3_5
    verdict['rating'] = str(rating).replace('.', '_')

    return verdict
