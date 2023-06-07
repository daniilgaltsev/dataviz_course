# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_exploring_the_data.ipynb.

# %% auto 0
__all__ = ['download_path', 'dataset_suffix', 'download_data']

# %% ../nbs/01_exploring_the_data.ipynb 2
import kaggle
from pathlib import Path

# %% ../nbs/01_exploring_the_data.ipynb 3
download_path = Path("../../tmp")
download_path.mkdir(exist_ok=True)
dataset_suffix = "ruchi798/data-science-job-salaries"

# %% ../nbs/01_exploring_the_data.ipynb 7
def download_data():
    kaggle.api.dataset_download_files(dataset=dataset_suffix, path=download_path, unzip=True)
    return pd.read_csv(download_path / "ds_salaries.csv", index_col=0).head()
