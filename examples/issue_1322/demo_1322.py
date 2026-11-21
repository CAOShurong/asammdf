from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from asammdf import MDF, Signal


def voltage(name, codes):
    return Signal(
        samples=np.array(codes, dtype=np.uint16),
        timestamps=np.arange(len(codes), dtype=float),
        name=name,
        unit="V",
        conversion={"val_0": 65535, "text_0": "invalid", "default_addr": {"a": 0.25, "b": 0}},
    )


if __name__ == "__main__":
    with MDF(version="4.10") as measurement:
        measurement.header.start_time = datetime(2020, 1, 1, tzinfo=timezone.utc)
        measurement.append([
            voltage("with_invalid", [1380, 1384, 1388, 65535]),
            voltage("control", [1380, 1384, 1388, 1392]),
        ])
        measurement.save(Path(__file__).with_name("mixed-voltage.mf4"), overwrite=True)
