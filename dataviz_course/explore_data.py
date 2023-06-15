# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_exploring_the_data.ipynb.

# %% auto 0
__all__ = ['download_path', 'dataset_suffix', 'download_data', 'prepare_dataset']

# %% ../nbs/01_exploring_the_data.ipynb 6
import kaggle
from pathlib import Path

# %% ../nbs/01_exploring_the_data.ipynb 7
download_path = Path("../../tmp")
download_path.mkdir(exist_ok=True)
dataset_suffix = "ruchi798/data-science-job-salaries"

# %% ../nbs/01_exploring_the_data.ipynb 10
import pandas as pd

# %% ../nbs/01_exploring_the_data.ipynb 11
def download_data() -> pd.DataFrame:
    """Downloads the salaries dataset and reads it"""
    kaggle.api.dataset_download_files(dataset=dataset_suffix, path=download_path, unzip=True)
    return pd.read_csv(download_path / "ds_salaries.csv", index_col=0)

# %% ../nbs/01_exploring_the_data.ipynb 32
def prepare_dataset(data=None):
    if data is None:
        data = download_data()
    data["On-site/Remote"] = data["remote_ratio"].map({0: "On-site", 50: "Hybrid", 100: "Remote"})
    data["experience_level"] = data["experience_level"].map({
        "EN": "Entry-level / Junior",
        "MI": "Mid-level / Intermediate",
        "SE": "Senior-level / Expert",
        "EX": "Executive-level / Director"
    })
    data["employment_type"] = data["employment_type"].map({
        "PT": "Part-time",
        "FT": "Full-time",
        "CT": "Contract",
        "FL": "Freelance"
    })
    data["Number of Employees"] = data["company_size"].map({
        "S": "<50",
        "M": "50-250",
        "L": ">250"
    })
    data["Working for a Foreign Company"] = data["employee_residence"] != data["company_location"]
    data = data.astype({"work_year": str})
    data = data.drop(columns=["salary", "salary_currency", "remote_ratio", "company_size", "employment_type"])
    data = data.rename(columns={
        "work_year": "Work Year",
        "experience_level": "Experience Level",
#         "employment_type": "Employment Type",
        "job_title": "Job Title",
        "salary_in_usd": "Salary (usd)",
        "employee_residence": "Employee Residence",
        "company_location": "Company Location",
    })
    return data
