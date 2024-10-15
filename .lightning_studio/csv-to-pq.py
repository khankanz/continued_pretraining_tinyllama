import argparse
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def csv_to_parquet(input_csv, output_parquet):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Convert the DataFrame to a PyArrow Table
    table = pa.Table.from_pandas(df)

    # Write the PyArrow Table to a Parquet file
    pq.write_table(table, output_parquet)

    print(f"Conversion complete. Parquet file saved as: {output_parquet}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert CSV to Parquet")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_parquet", help="Path to the output Parquet file")

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function
    csv_to_parquet(args.input_csv, args.output_parquet)