from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from claude_trainer import generar_plan_inteligente_claude, asistente_conversacional_claude

app = FastAPI(
    title="Wings for Life - Club Mariana Carmona API",
    description="Backend oficial para gestión de atletas, planes personalizados y rutas de Medellín.",
    version="1.0.0"
)

class AtletaPerfil(BaseModel):
    nombre: str
    peso_kg: float
    ritmo_actual_min_km: float
    experiencia: str
    correo: str

class ConsultaCoach(BaseModel):
    nombre_atleta: str
    ritmo_actual: float
    pregunta: str

@app.post("/api/claude/generar-plan")
def api_generar_plan(atleta: AtletaPerfil):
    try:
        plan = generar_plan_inteligente_claude(
            nombre=atleta.nombre,
            peso=atleta.peso_kg,
            ritmo=atleta.ritmo_actual_min_km,
            nivel=atleta.experiencia
        )
        return {
            "status": "success",
            "atleta": atleta.nombre,
            "club_asignado": "Club Oficial Mariana Carmona - Wings for Life",
            "plan_entrenamiento": plan
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/claude/consultar")
def api_consultar(consulta: ConsultaCoach):
    try:
        respuesta = asistente_conversacional_claude(
            nombre=consulta.nombre_atleta,
            ritmo=consulta.ritmo_actual,
            pregunta=consulta.pregunta
        )
        return {
            "status": "success",
            "respuesta": respuesta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))