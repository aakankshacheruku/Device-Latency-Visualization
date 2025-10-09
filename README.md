# Device Latency Data Visualization

Reproducible mini-pipeline that computes latency summaries (p50/p95/p99), validates inputs, and exports a table and figure to `reports/`.  
Structured to reflect internal analytics standards: documented, parameterized, and testable.

## Purpose
Operational analytics depends on repeatability and validated data.  
This workflow performs:
- extraction and merge of raw latency data  
- cleaning and validation  
- descriptive statistics generation  
- artifact output for review or dashboard import  

## Structure
data/
sample/ # example CSV inputs
reports/
tables/ # generated .csv
figures/ # generated .png
src/latency/
io.py # read/write helpers
compute.py # percentiles, tails, summary
plot.py # visualization
run.py # CLI entrypoint
tests/
test_compute.py # unit tests
Makefile
requirements.txt

bash
Copy code

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
make quickstart
Artifacts produced:

reports/tables/latency_summary.csv

reports/figures/latency_distribution.png

Input schema
CSV columns required:

device_id (string)

timestamp (ISO8601)

latency_ms (float)

Validation rules:

negative or zero latency_ms removed

missing values dropped, count recorded

optional capping of long-tail values for visualization only

Metrics
Descriptive: count, mean, std, min, max

Percentiles: p50, p95, p99 (configurable)

Tail share: proportion above SLA threshold (>100 ms by default)

Running on custom data
bash
Copy code
python -m latency.run \
  --input data/sample/latency_sample.csv \
  --out_dir reports \
  --pcts 50 95 99 \
  --sla_ms 100
Testing
bash
Copy code
pytest -q
Roadmap
weekly aggregation

region and device roll-ups

drift alerts on percentile change
