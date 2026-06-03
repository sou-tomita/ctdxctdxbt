#! /usr/bin/env python3

import pandas as pd

import namelist as nl
from getdf import get_xctd_df

nl.output_dir.mkdir(exist_ok=True)

# read field book
fbook_df = pd.read_csv(nl.field_book_path)

for data_fpath in nl.input_dir.glob("*.CTD"):

    df, _, _ = get_xctd_df(data_fpath)
    output_fpath = nl.output_dir / data_fpath.with_suffix(".csv").name
    print(f"Processing {data_fpath} -> {output_fpath}")

    df.to_csv(output_fpath, index=False)
