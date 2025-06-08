# TrueVal App

Fullstack AI-powered property valuation platform using Flask (backend) and React + Vite + Tailwind (frontend).

## 📁 Structure

```
trueval-app/
├── backend/     # Flask API
└── frontend/    # React UI with Tailwind
```

## 🚀 Development

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🌐 Render Deployment

Two services:
- `trueval-api` → Python Web Service
- `trueval-ui`  → Static Site with `VITE_API_BASE` env var pointing to backend

## 🔗 API Endpoint

`GET /predict` → returns mock valuation:
```json
{
  "valuation": 375000,
  "confidence": "high"
}
```
