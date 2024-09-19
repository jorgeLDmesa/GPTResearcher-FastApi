from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from gpt_researcher import GPTResearcher
import asyncio
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Set environment variables
os.environ['OPENAI_API_KEY'] = dotenv.get_key('.env', 'OPENAI_API_KEY')
os.environ['TAVILY_API_KEY'] = dotenv.get_key('.env', 'TAVILY_API_KEY')
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes de origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)

@app.get("/report/{report_type}")
async def get_report(query: str, report_type: str, api_key: str = Header(...)) -> dict:
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="API key inválida")
    
    researcher = GPTResearcher(query, report_type,verbose=False)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report}

# Run the server
# uvicorn main:app --reload
