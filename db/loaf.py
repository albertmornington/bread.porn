from db.helpers import fields_as_dict
from db.baker import baker_from_id
from db.ingredients import ingredients_from_id
from db.verdict import verdict_from_id
from db.timeline import timeline_from_id

LOAF_FIELDS = ('name', 'baker', 'ingredients', 'verdict', 'timeline')

def loaf_from_alias(r, alias):
    loaf_key = 'loaf:{}'.format(alias)
    if not r.exists(loaf_key):
        return None

    loaf_dict = fields_as_dict(r, loaf_key, LOAF_FIELDS)

    baker = baker_from_id(r, loaf_dict['baker'])
    ingredients = ingredients_from_id(r, loaf_dict['ingredients'])
    verdict = verdict_from_id(r, loaf_dict['verdict'])
    timeline = timeline_from_id(r, loaf_dict['timeline'])

    if not all((baker, ingredients, verdict, timeline)):
        return None

    return {
        'name': loaf_dict['name'],
        'baker': baker,
        'ingredients': ingredients,
        'verdict': verdict,
        'timeline': timeline,
    }
