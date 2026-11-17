# Free deployment

Frontend: Vite + vanilla JavaScript + sql.js SQLite/WebAssembly. Browser database contains 50,000 deterministic mock query records and is regenerated on reload; export a SQLite file to retain a copy. No external database account, billing or shared persistence is required. Measured benchmark JSON/CSV is shipped separately.

Hosting: GitHub Pages via GitHub Actions; repository public visibility authorized by user on 2026-11-16. Expected URL: https://jabrielabdillle.github.io/distributed-vector-search/ . Do not claim live deployment until the deploy job and URL are verified.

Local: `cd web && npm ci && npm run dev`. Production checks: `npm test`. Python: create a Python 3.12 virtual environment, `pip install -r requirements.lock`, then `python -m pytest -q`. Run new CPU evidence with `python -m lab.benchmark --output <new-report.json>` from repository root. No overwrite of existing reports.

Settings → Pages → GitHub Actions is required before deploying. Workflow validates Python and production-browser checks before publishing main. Static hosting runs the dashboard; heavy compute runs locally. Hosted GPU workers and database engines are not deployed by this workflow.

## Design tools
Taste skill: graphite/safety-orange palette and Host Grotesk/JetBrains Mono pairing. Dashboard navigation, data tables, plots and explicit mock labels take priority over marketing-page section height rules. Emil Kowalski guidance informs fast press feedback, reduced motion, focus visibility and restrained transitions. Playwright plugin directory search returned no results; official @playwright/test is used, not represented as an installed connector.
