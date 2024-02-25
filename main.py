

# Copyright 2024 David Baker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Designed to work with the ORR Origin-Destination Data,
# distributed according to the Open Government Licence v3.0

import pandas as pd


def pivot_origin_destination_matrix(source_fpath: str, destination_fpath):
    with open(source_fpath, 'r') as file:
        df = pd.read_csv(file, delimiter=",", quotechar='"')

    matrix = df.pivot_table(
        index="origin_station_name",
        columns="destination_station_name",
        values="journeys",
        fill_value=0
    )

    with open(destination_fpath, "w+") as file:
        matrix.to_csv(file, index=True, lineterminator='\n')
