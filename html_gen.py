import pandas as pd

def csv_to_html(f_in, f_out):
    df = pd.read_csv(f_in, on_bad_lines="skip", skiprows=[0,1,2,3,4])
    df.to_html(f_out)

if __name__ == "__main__":
    csv_to_html("http/boms/ovrdrive.csv", "http/boms/ovrdrive.html")
