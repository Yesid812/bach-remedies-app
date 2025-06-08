from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from engine import BachFlowersEngine
from experta import KnowledgeEngine, Fact, Rule
app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = BachFlowersEngine()

@app.post("/diagnosticar")
async def diagnosticar(sintomas: dict):
    engine.reset()
    
    for sintoma in sintomas["sintomas"]:
        engine.declare(Fact(sintoma=sintoma))
    
    engine.run()
    
    # Versión CORRECTA para acceder a los hechos en Experta
    for fact in engine.facts.values():
        print(f"Evaluando hecho completo: {fact}")
        # Método robusto para verificar y acceder a los atributos
        if hasattr(fact, '__getitem__'):  # Verifica si es un hecho estilo diccionario
            recomendacion = fact.get('recomendacion')
            if recomendacion:
                return {
                    "recomendacion": recomendacion,
                    "dosis": fact.get('dosis'),
                    "explicacion": fact.get('explicacion')
                }
    
    return {
        "recomendacion": None,
        "dosis": None,
        "explicacion": "No se encontró un remedio para estos síntomas"
    }
