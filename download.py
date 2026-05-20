import gdown
import os

def download_checkpoint(file_id, checkpoint_dir="./checkpoints"):
    """
    Download checkpoint if it does not exist.

    Recommended:
        Google Drive + gdown

    Return:
        checkpoint_path
    """

    checkpoint_path = os.path.join(
        checkpoint_dir,
        "model.pth",
    )

    os.makedirs(
        checkpoint_dir,
        exist_ok=True,
    )

    if os.path.exists(checkpoint_path):

        print("Checkpoint already exists.")

        return checkpoint_path


    # Example link:
    # https://drive.google.com/file/d/FILE_ID/view
    # put your file id instead
    
    url = (
        f"https://drive.google.com/uc?id={file_id}"
    )

    gdown.download(
        url,
        checkpoint_path,
        quiet=False,
    )

    return checkpoint_path

if __name__ == "__main__":
    download_checkpoint("YOUR_FILE_ID")