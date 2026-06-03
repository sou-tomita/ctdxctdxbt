#!/usr/bin/env python3

from pathlib import Path
import pandas as pd


def get_xctd_df(fpath: Path) -> tuple[pd.DataFrame, str, str]:

    dpth_list = []
    tmp_list = []
    cnd_list = []
    sal_list = []
    sve_list = []
    den_list = []
    with open(fpath, "r") as file:

        # read a header record
        header = file.read(256)
        ymd = header.split(",")[2]
        hms = header.split(",")[3]

        # read data records
        data = file.read().split("\n")[:-1]

        num_records = len(data)

        for i in range(num_records):

            d = data[i].split(",")
            if len(d) != 7:
                break
            dpth = float(d[0])
            tmp = float(d[1])
            cnd = float(d[2])
            sal = float(d[3])
            sve = float(d[4])
            den = float(d[5])

            dpth_list.append(dpth)
            tmp_list.append(tmp)
            cnd_list.append(cnd)
            sal_list.append(sal)
            sve_list.append(sve)
            den_list.append(den)

    df = pd.DataFrame(
        {
            "depth": dpth_list,
            "Temp": tmp_list,
            "Conductivity": cnd_list,
            "Salinity": sal_list,
            "Sound Velocity": sve_list,
            "Density": den_list,
        }
    )

    return df, ymd, hms
