import argparse
from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser(description="Download a model from Hugging Face Hub")
parser.add_argument(
    "--model_id",
    type=str,
    help="Model ID on Hugging Face Hub",
    required=True,
)

args = parser.parse_args()

model_id = args.model_id

snapshot_download(repo_id=model_id, local_dir="models", local_dir_use_symlinks=False, revision="main")