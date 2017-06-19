from db.helpers import fields_as_dict

ACTION_FIELDS = ('duration', 'temperature', 'name', 'notes')

def timeline_from_id(r, i):
    actions_key = 'actions:{}'.format(i)
    if not r.exists(actions_key):
        return None

    action_id_list = r.lrange(actions_key, 0, -1)
    return filter(
        lambda x: x is not None,
        [action_from_id(r, j) for j in action_id_list]
    )

def action_from_id(r, i):
    action_key = 'action:{}'.format(i)
    if not r.exists(action_key):
        return None
    
    return fields_as_dict(r, action_key, ACTION_FIELDS)
