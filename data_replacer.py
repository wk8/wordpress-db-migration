# -*- coding: utf-8 -*-

import re


class DataReplacer(object):

    _serialized_regex = re.compile(r's:(\d+):([\\]*[\'"])(.*?)\2;')

    def __init__(self, search, replace):
        self._replace = replace
        self._length_delta = len(search) - len(replace)
        self._count = 0
        self._search_regex = re.compile(re.escape(search))

    @property
    def count(self):
        return self._count

    def process(self, data):
        new_data = []
        last_match_end = 0
        for match in self._serialized_regex.finditer(data):
            (_, processed_data) = self._replace_in_string_data(data[last_match_end:match.start()])
            new_data.append(processed_data)

            (nb_occurences, processed_data) = self._replace_in_string_data(match.group(3))
            length = int(match.group(1)) - self._length_delta * nb_occurences
            delimiter = match.group(2)
            new_serialized_data = 's:%s:%s%s%s;' % (length, delimiter, processed_data, delimiter)
            new_data.append(new_serialized_data)

            last_match_end = match.end()

        (_, processed_data) = self._replace_in_string_data(data[last_match_end:])
        new_data.append(processed_data)
        return ''.join(new_data)

    def _replace_in_string_data(self, data):
        new_data = []
        last_match_end = 0
        count = -1
        for count, match in enumerate(self._search_regex.finditer(data)):
            new_data.append(data[last_match_end:match.start()])
            new_data.append(self._replace)
            last_match_end = match.end()
        new_data.append(data[last_match_end:])

        self._count += (count + 1)
        return (count + 1, ''.join(new_data))
