import os
import re
from parse import parse
import pandas as pd


dir: str = os.path.dirname(os.path.abspath(__file__))
file: str = dir + "\data\TPFREP_CGM.edi"


def main():

    if not os.path.exists(file):
        print("ERROR: Input file does not exist!!")

    # OPEN FILE
    tpfrep_file = open(file, "r")

    table: list = []

    fmt = "{SEGMENT}+{ZZZ}++{CODE}:{MIN}+{DESCRIPTION}'"

    for row in tpfrep_file:
        # print(row)
        if re.match("FTX", row):
           pdata = parse(fmt, row.rstrip())
           table.append(pdata.named)
           
    if len(table) > 0:
        df = pd.DataFrame(table)
        print(df.head(len(table)))

if __name__ == '__main__':
    main()
