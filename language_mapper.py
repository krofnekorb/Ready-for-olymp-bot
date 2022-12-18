from_russian_to_english_mapping_holder = {
    'ТФКП': 'tfcv',
    'Линейная алгебра': 'linal',
    'Алгебра': 'algebra',
    'Классический анализ': 'calculus',
    'Комбинаторика': 'comb',
    'Теория вероятностей': 'probability'
}

def map_from_russian_to_english(section):
    return from_russian_to_english_mapping_holder.get(section.strip())
