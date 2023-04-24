import pandas as pd
import pdb

def csv_to_html(f_in, f_out):
    try:
        df = pd.read_csv(f_in, on_bad_lines="skip", skiprows=[0,1,2,3,4])
        df["QTD Available"] = df["QTD Available"].astype(pd.Int64Dtype())
        df.to_html(f_out)
    except(FileNotFoundError):
        pass

if __name__ == "__main__":
    csv_to_html("http/boms/ovrdrive.csv", "http/boms/ovrdrive.html")
