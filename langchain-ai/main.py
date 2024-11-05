from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an experienced technical interviewer crafting interview questions based on a job description for a Senior Software Engineer role. Each question should assess relevant skills, experience, and thought processes for a candidate applying to this role.",
        ),
        (
            "human",
            "Given the following job description, generate a list of targeted interview questions:\n\nJob Description:\n{job_description}"
        ),
    ]
)

chain = prompt | llm


class JobDescriptionRequest(BaseModel):
    job_description: str


@app.post("/")
async def generate_interview_questions(request: JobDescriptionRequest):
    try:
        # Generate interview questions based on the job description
        questions = prompt | llm
        result = questions.invoke({"job_description": request.job_description})
        return {"message": result.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
