from db.helpers import fields_as_dict

VERDICT_FIELDS = ('sweetness', 'sourness', 'crust', 'texture', 'toasting', 'notes')

def verdict_from_id(r, i):
    verdict_key = 'verdict:{}'.format(i)
    if not r.exists(verdict_key):
        return None
    
    return fields_as_dict(r, verdict_key, VERDICT_FIELDS)
