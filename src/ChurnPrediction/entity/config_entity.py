from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    data_dir: Path
    schema: dict
