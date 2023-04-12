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
    tblcrane: list = []

    fmt = "{SEGMENT}+{ZZZ}++{CODE}:{MIN}+{DESCRIPTION}'"
    fmt_crane = "{EQD}+{GC}+{NAME}'"
    fmt_qty = "{EQD}+{GC}:{NAME}'"

    """EQD+GC+C02'
       QTY+CMV:379'
       QTY+HCV:5'
       QTY+TMV:361'"""

    for row in tpfrep_file:
        # print(row)
        """
        if re.match("FTX", row):
            pdata = parse(fmt, row.rstrip())
            table.append(pdata.named)

        match = re.findall(r'EQD', row.rstrip())
        if match:
            pddata = parse(fmt_crane, row.rstrip())
            tblcrane.append(pddata.named)
        """
        if re.match("EQD", row):
            arg = row.split('+')
            if arg[1] == 'GC':
                pddata = parse(fmt_crane, row.rstrip())
                tblcrane.append(pddata.named)

        if re.match("QTY", row):
            arg = row.split('+')
            op = arg[1].split(':')[0]
            if op == 'CMV':
                pddata = parse(fmt_qty, row.rstrip())
                tblcrane.append(pddata.named)
            if op == 'HCV':
                pddata = parse(fmt_qty, row.rstrip())
                tblcrane.append(pddata.named)
            if op == 'TMV':
                pddata = parse(fmt_qty, row.rstrip())
                tblcrane.append(pddata.named)

    if len(tblcrane) > 0:
        df = pd.DataFrame(tblcrane)
        print(df.head(len(tblcrane)))


#if __name__ == '__main__':
    #main()
