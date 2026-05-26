# Changelog

All notable changes to **AttritionIQ** will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2025-05-26

### Added
- 🧠 Random Forest ML model for employee attrition prediction
- 🌐 Flask web application with three routes: Home, History, Dashboard
- 📊 Analytics Dashboard with Chart.js doughnut chart and KPI cards
- 📋 Prediction history page with timestamped MongoDB records
- ⚠️ Risk classification: High / Medium / Low based on probability threshold
- 🔄 In-memory fallback storage when MongoDB is unavailable
- 💡 Retention insight cards with contextual advice per risk level
- 🎨 Responsive UI using Tailwind CSS with sidebar and mobile bottom nav
- 📱 Mobile-friendly bottom navigation bar
- 🔮 Loading spinner animation during model inference
- 📄 Environment variable support for MongoDB URI and Flask debug mode
- 🗂️ External CSS stylesheet with animations, scrollbar, and badge styles
- 🤖 GitHub Actions CI pipeline for linting and validation
- 📝 CONTRIBUTING.md, CHANGELOG.md, SECURITY.md documentation

### Technical
- `clean_data.py` — data preprocessing on IBM HR dataset
- `train_model.py` — model training with accuracy reporting
- `requirements.txt` — pinned Python dependencies
- `.env.example` — environment variable template
- `.gitignore` — excludes venv, pycache, model, and dataset files

### Branding
- Project renamed from **Inventeron** to **AttritionIQ**
- All templates updated with AttritionIQ branding and tagline

---

## [Unreleased]

### Planned
- [ ] Input validation with user-friendly error messages
- [ ] CSV export of prediction history
- [ ] Pagination on history page
- [ ] Dark mode toggle
- [ ] Deployment to Render / Railway
