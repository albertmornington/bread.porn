from db.helpers import fields_as_dict

BAKER_FIELDS = ('name', 'bio')

def baker_from_id(r, i):
    baker_key = 'baker:{}'.format(i)
    if not r.exists(baker_key):
        return None
     
    return fields_as_dict(r, baker_key, BAKER_FIELDS)
