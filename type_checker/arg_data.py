from dataclasses import dataclass

@dataclass
class ArgData():
    name: str
    value: any
    expected_type: type