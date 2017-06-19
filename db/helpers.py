def fields_as_dict(r, key, fields):
    return dict(zip(fields, r.hmget(key, fields)))
