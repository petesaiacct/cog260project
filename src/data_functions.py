import math

"""
This functions are used to create the arrays and dataframes for the graphs and data exploration.
"""

def get_rating(start, stop, dictionary_type, ordered):
    """Gets all values from hard assigned array 'ordered' sorted to 'colexification_count', and then returns
        two lists of words and values. The first list of words are those words and found values
        if and only if, both words appear in the provided value dictionary. This list has
        first value as String of concept 1, Float of its value in dictionary, String of concept 2,
        Float of its value in dictionary, and Integer of its colexification count.
        The second returned list is all the concepts where they were not both found in the
        dictionary.

        @parameters:
        (int) start which is used as a starting index value,
        (int) stop which is used as a stopping index value.
        (dict) dictionary_type is used as the dictionary to search values in

        @return: list[[String, Float, String, Float, int],[String, String, int]]
"""
    test_value = []
    unavailable = []
    for index in range(start, stop, 1):
        key_a, key_b, count_num = ordered[index][0].lower(), ordered[index][1].lower(), ordered[index][2]
        if key_a in dictionary_type.keys() and key_b in dictionary_type.keys():
            test_value.append([key_a, dictionary_type[key_a], key_b, dictionary_type[key_b], count_num])
        else:
            unavailable.append([key_a, key_b, count_num])
    return [test_value, unavailable]


def partial_array(start, stop, input_list):
    """ This function returns the specific portion of a list
        using the parameters as index points, and the list.
        Pre-conditions: start parameter and stop parameter must be valid as in 0 or greater, and
        less than length of list -1
        @Parameters:
        (int) start
        (int) stop
        (list) input_list

        @return: list[]
        """
    list_return = []
    for j in range(start, stop, 1):
        list_return.append(input_list[j])
    return list_return


def near_values(float1, float2):
    """
    This function returns an integer ranking of how close in value two compared floats are.
    (1 being the closest, 10 being the least close or greater than .5 tolerance)
    :param float1: float value of first comparison
    :param float2: float value of second comparison
    :return: int value for rank
    """
    tolerance_list = [[0.5, 9], [0.3, 8], [0.2, 7], [0.1, 6], [0.05, 5], [0.01, 4], [0.005, 3], [0.001, 2], [0.0001, 1]]
    tolerance_value = True
    result = 10

    for toler in tolerance_list:
        tolerance_value = math.isclose(float1, float2, abs_tol=toler[0])
        if tolerance_value:
            result = toler[1]
        else:
            return result
    return result


def concept_values(results):
    """
    This function returns two versions of data for use in both graphs, and more dataframe exploration.
    It takes in the first list created by get_valence and creates a new dataframe, and a new list of arrays and returns them.
    The list of data arrays is just values which represent float value of concept 1 rating, float value of concept 2 rating, integer value
    of colxifiaction number, and float value of the average of the concept 1 and concept 2 value.
    the dataframe is the column values of 'Concept1', 'Concept1Value', 'Concept2', 'Concept2Value', 'ColexValue', 'CombinedAverage', 'NearRating'.
    :param results: ist[[String, Float, String, Float, int]
    :return: list[array, array, array, array], dataframe['Concept1', 'Concept1Value', 'Concept2', 'Concept2Value', 'ColexValue', 'CombinedAverage', 'NearRating']
    """
    concept_a, concept_b, label_num, mean_of_both = [], [], [], []
    my_list = []
    for xx in range(0, len(results)):
        concept_a.append(results[xx][1]), concept_b.append(results[xx][3]), label_num.append(
            results[xx][4]), mean_of_both.append((results[xx][1] + results[xx][3]) / 2)
        my_list.append([results[xx][0], results[xx][1], results[xx][2], results[xx][3], results[xx][4],
                        (results[xx][1] + results[xx][3]) / 2, near_values(results[xx][1], results[xx][3])])
    my_array = np.array(my_list)
    datfram = pd.DataFrame(my_array, columns=['Concept1', 'Concept1Value', 'Concept2', 'Concept2Value', 'ColexValue',
                                              'CombinedAverage', 'NearRating'])
    listofdata = [np.array(concept_a, dtype=float), np.array(concept_b, dtype=float), np.array(label_num, dtype=int),
                  np.array(mean_of_both, dtype=float)]
    return listofdata, datfram
