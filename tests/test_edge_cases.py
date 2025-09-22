# Small sanity tests—keep these lightweight and readable.

import pandas as pd

def test_negative_latency_is_detectable():
    df = pd.DataFrame({"ts":["2025-01-01T00:00:00Z"], "latency_ms":[-1], "region":["x"], "device_id":["y"]})
    assert (df["latency_ms"] < 0).any()

