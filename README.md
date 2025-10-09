# Device Latency Data Visualization

Reproducible mini-pipeline that computes latency summaries (p50/p95/p99), validates inputs, and exports tables and figures to `reports/`.  
Structured for reliability, documentation, and repeatability.

---

## Purpose
Operational analytics relies on validated and reproducible data flows.  
This workflow handles:
- extraction and merge of raw latency data  
- cleaning and validation  
- computation of descriptive statistics  
- generation of reusable artifacts for dashboards or QA reports  

---

## Project Structure
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

___ 
## Setup & Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
make quickstart
Artifacts produced

reports/tables/latency_summary.csv

reports/figures/latency_distribution.png

Input Schema

| Column       | Type    | Description                   |
| ------------ | ------- | ----------------------------- |
| `device_id`  | string  | Unique identifier for device  |
| `timestamp`  | ISO8601 | Timestamp of recorded latency |
| `latency_ms` | float   | Latency in milliseconds       |

Validation rules

negative or zero latency_ms values removed

missing latency_ms dropped; count recorded in summary

optional capping of extreme tail values for visualization only

___

Metrics

| Category    | Metric                       | Description                   |
| ----------- | ---------------------------- | ----------------------------- |
| Descriptive | count, mean, std, min, max   | Basic distribution statistics |
| Percentiles | p50, p95, p99 (configurable) | Latency thresholds            |
| Tail Share  | share above SLA threshold    | Default SLA >100 ms           |

Command-Line Execution
python -m latency.run \
  --input data/sample/latency_sample.csv \
  --out_dir reports \
  --pcts 50 95 99 \
  --sla_ms 100

Testing
pytest -q

Roadmap

- weekly aggregation

- region and device roll-ups

- drift alerts on percentile change
