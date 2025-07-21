from typing import Union, List, Dict

NextUUIDsList = List[str]

SaveDataValues = Union[str,int,None,NextUUIDsList]

SaveData = Dict[str,SaveDataValues]

SavesList = List[SaveData]

RunDataValues = Union[str,None,SavesList]

RunData = Dict[str,RunDataValues]

RunList = List[RunData]

DataFileValues = Union[str,RunList]

DataFileStructure = Dict[str, DataFileValues]
