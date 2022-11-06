
def flat_generator_h(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            yield from flat_generator_h(item)
        else:
            yield item