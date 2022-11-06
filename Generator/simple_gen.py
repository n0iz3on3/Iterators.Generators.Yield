
def flat_generator_s(list_of_lists):
    for item in list_of_lists:
        for elem in item:
            yield elem