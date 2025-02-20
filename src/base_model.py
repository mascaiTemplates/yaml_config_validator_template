import yaml

from pydantic import BaseModel
from typing import Union
from pathlib import Path


class YamlModel(BaseModel): 
    @classmethod 
    def from_yaml(cls, yaml_file_path: Union[str, Path]) -> "YamlModel": 
        yaml_file = Path(yaml_file_path)
        with open(yaml_file, "r") as f: 
            file_content = yaml.safe_load(f)
            
        return cls.parse_obj(file_content)