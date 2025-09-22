# Device Latency Data Visualization

Small end-to-end project to compute latency summaries (p50/p95) and a simple plot. I focused on a clear pipeline and tangible outputs. I plan to expand metrics and coverage over time.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make quickstart
```

Outputs will appear in `reports/tables/` and `reports/figures/`.

## What I learned
- Keep calculations simple and NA-safe first, then iterate.
- Make small, testable steps and produce artifacts (CSV/PNG) every run.
- Write down decisions so future changes are easier to review.

## Decisions & next steps
- Start with a small sample so the pipeline is easy to run.
- Percentiles over averages; I want to add geographic views and drift detection next.
- Roadmap: expand data, add better metrics, and tighten tests as I go.

## Preview
After `make quickstart`, you should see a CSV table and one PNG in `reports/`.
