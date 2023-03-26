import os
from pathlib import Path
import random
import glob
import sys

sys.path.append("./sgd_dstc8_data_model")
from dstc_dataclasses import DstcDialog

import dstc_utils


def test_data_exists():
    data_root_dir = Path("data")
    assert data_root_dir.exists()
    data_dir = data_root_dir / "dstc8-schema-guided-dialogue"
    assert data_dir.exists()


def test_load_dialog():
    data_dir = Path("data/dstc8-schema-guided-dialogue")
    step = "dev"

    dialog_paths = glob.glob(str(data_dir / step) + "/dialogues*.json")
    assert len(dialog_paths) > 0
    file = random.choice(dialog_paths)
    dialog_json = dstc_utils.read_json(file)
    dialog = DstcDialog.from_dict(dialog_json[0])
    assert dialog is not None
