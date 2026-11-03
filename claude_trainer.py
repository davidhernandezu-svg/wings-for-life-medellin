import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def generar_plan_inteligente_claude(nombre: str, peso: float, ritmo: float, nivel: str) -> str:
    prompt = f"""
    Eres el entrenador jefe de élite del club de running de Mariana Carmona para el evento Wings for Life World Run.
    Genera un plan de entrenamiento de 4 semanas estructurado y motivador para el siguiente atleta:
    - Nombre: {nombre}
    - Peso: {peso} kg
    - Ritmo actual: {ritmo} min/km
    - Nivel: {nivel}
    
    El plan debe incluir:
    1. Distribución de cargas semanales (incorporando rutas clave de Medellín como el Aeroparque Juan Pablo II, Parques del Río o Vía a Las Palmas).
    2. Pautas de nutrición e hidratación personalizadas de acuerdo a su peso.
    3. Táctica específica de ritmo constante para resistir al Catcher Car el día de la carrera.
    """

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        temperature=0.7,
        system="Eres un experto en fisiología del ejercicio, biomecánica de carrera y estrategia táctica para eventos de persecución global.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text

def asistente_conversacional_claude(nombre: str, ritmo: float, pregunta: str) -> str:
    prompt = f"Atleta: {nombre} | Ritmo actual: {ritmo} min/km | Consulta: {pregunta}"
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        temperature=0.5,
        system="Eres un asistente de entrenamiento de élite en Medellín, experto en análisis de datos de carrera y control de fatiga.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text