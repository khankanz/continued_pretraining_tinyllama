import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(input_file, output_train, output_test):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Split the dataset
    train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
    
    # Save the split datasets
    train_set.to_csv(output_train, index=False)
    test_set.to_csv(output_test, index=False)
    
    print(f"Dataset split complete.")
    print(f"Training set saved to: {output_train}")
    print(f"Testing set saved to: {output_test}")

def main():
    parser = argparse.ArgumentParser(description="Split a CSV dataset into training and testing sets.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("--output_train", default="train_set.csv", help="Path to save the training set CSV (default: train_set.csv)")
    parser.add_argument("--output_test", default="test_set.csv", help="Path to save the testing set CSV (default: test_set.csv)")
    
    args = parser.parse_args()
    
    split_dataset(args.input_file, args.output_train, args.output_test)

if __name__ == "__main__":
    main()