from utils import is_relevant_call, format_call

def filter_and_format_opencalls(calls, previous_ids):
    nouveaux = []
    rappels = []

    for call in calls:
        if not is_relevant_call(call):
            continue
        if call['id'] in previous_ids:
            rappels.append(format_call(call))
        else:
            nouveaux.append(format_call(call))
    return nouveaux, rappels
