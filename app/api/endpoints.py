from fastapi import APIRouter
from app.agents.qa_agent import run_qa_agent
from app.agents.exec_agent import run_exec_agent

router = APIRouter()

@router.get("/qa")
def qa(question: str):
    return {"answer": run_qa_agent(question)}

@router.get("/execute")
def execute(task: str):
    return {"result": run_exec_agent(task)}
