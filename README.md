litgpt pretrain --config configs/tinyllama-2krad.yaml --train.max_seq_length 64 --train.micro_batch_size 1

# On creating valid / train
python utils/split_ds.py kaggle-2k-radiology-reports-public.csv

# On conversion to pq from .csv
Testing set saved to: test_set.csv
⚡ main ~ python utils/csv2pq.py test_set.csv val.parquet   
Conversion complete. Parquet file saved as val.parquet
⚡ main ~ python utils/csv2pq.py train_set.csv train.parquet
Conversion complete. Parquet file saved as train.parquet

# On preparing ds for pretraining:
prepare_dataset.py --input_dir=data/raw/val --output_dir=data/processed/val