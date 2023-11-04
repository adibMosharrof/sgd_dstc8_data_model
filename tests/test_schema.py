from pathlib import Path
import random
import glob
import sys

import yaml

sys.path.append("./sgd_dstc8_data_model")

from dstc_constants import DstcSpecialTokens, DstcConstants

from dstc_dataclasses import DstcDialog, DstcSchema

import dstc_utils


def test_load_schema():
    step = "dev"
    data_dir = Path("data/dstc8-schema-guided-dialogue")
    schema_paths = glob.glob(str(data_dir / step) + "/schema.json")
    assert len(schema_paths) > 0
    schema = random.choice(schema_paths)
    schema_json = dstc_utils.read_json(schema)
    assert len(schema_json) > 0
    dstc_schema = DstcSchema.from_dict(schema_json[0])
    schema_nlg_str = dstc_schema.get_nlg_repr()
    print(schema_nlg_str)
    schema_str = dstc_schema.get_full_repr()
    assert schema_str is not None
