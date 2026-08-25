from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="0032-ghost-reseller-hub Production API",
    version="1.0.0",
    description="MammoInsight & Angelus AGI Production Node"
)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>0032-ghost-reseller-hub | Node Status</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0D0F17;
            --card-bg: #161926;
            --primary: #AB3689;
            --accent: #00A896;
            --text: #F3F4F6;
            --text-dim: #9CA3AF;
        }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 168, 150, 0.15);
            color: #2DD4BF;
            padding: 6px 14px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 20px;
        }
        .dot {
            width: 8px;
            height: 8px;
            background: #2DD4BF;
            border-radius: 50%;
            box-shadow: 0 0 10px #2DD4BF;
        }
        h1 {
            font-size: 24px;
            margin: 0 0 10px 0;
            color: #FFF;
        }
        p {
            color: var(--text-dim);
            line-height: 1.6;
            font-size: 15px;
            margin-bottom: 30px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 30px;
        }
        .btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        .btn-primary {
            background: linear-gradient(135deg, var(--primary), #802364);
            color: white;
        }
        .btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .btn:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }
        .footer {
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 20px;
            font-size: 13px;
            color: var(--text-dim);
            display: flex;
            justify-content: space-between;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge"><div class="dot"></div> PRODUCTION NODE ONLINE</div>
        <h1>0032-ghost-reseller-hub</h1>
        <p>Nodo de microservicio biomédico y desarrollo agéntico desplegado exitosamente en Render Cloud.</p>
        
        <div class="grid">
            <a href="/docs" class="btn btn-primary">📖 Probar API (/docs)</a>
            <a href="/health" class="btn btn-secondary">🩺 Estado (/health)</a>
        </div>
        
        <div class="footer">
            <span>Autor: <strong>Perez, Ernesto Rafael ("Rafa")</strong></span>
            <span>Plataforma: <strong>Render Cloud</strong></span>
        </div>
    </div>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
def root_dashboard():
    return HTML_TEMPLATE

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "0032-ghost-reseller-hub",
        "author": "Perez, Ernesto Rafael (Rafa)",
        "mcp_services": ["context7", "stitch", "supabase", "v0"]
    }

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "An internal service error occurred."}
    )
