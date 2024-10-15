import os
import numpy as np
from lightning.data import optimize
from jsonargparse import CLI
from functools import partial
from pathlib import Path
from litgpt.tokenizer import Tokenizer
import pyarrow.parquet as pq


def process(filepath, tokenizer):
    parquet_file = pq.ParquetFile(filepath)
    # reduce RAM usage
    for batch in parquet_file.iter_batches(batch_size=8192, columns=["text"]):
        for text in batch.to_pandas()["text"]:
            yield tokenizer.encode(text, bos=False, eos=True)
    parquet_file.close()


def prepare(
    input_dir: Path = Path("dataset/raw/open-web-math/data"),
    output_dir: Path = Path("dataset/processed/open-web-math"),
    tokenizer_path: Path = Path("./tokenizer"),
    chunk_bytes: str = "100MB",
    fast_dev_run: bool = False,
):

    tokenizer = Tokenizer(tokenizer_path)
    inputs = [str(p.absolute()) for p in input_dir.iterdir()]

    optimize(
        fn=partial(process, tokenizer=tokenizer),
        inputs=inputs,
        output_dir=str(output_dir),
        num_workers=(os.cpu_count() - 2),
        chunk_bytes=chunk_bytes,
        fast_dev_run=fast_dev_run,
    )


if __name__ == "__main__":
    CLI(prepare)
