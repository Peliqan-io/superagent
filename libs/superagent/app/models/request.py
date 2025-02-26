from typing import Any, Dict, Optional

from pydantic import BaseModel

from prisma.enums import VectorDbProvider


class ApiUser(BaseModel):
    email: str


class Agent(BaseModel):
    isActive: bool = True
    name: str
    initialMessage: Optional[str]
    prompt: Optional[str]
    llmModel: str
    description: str
    avatar: Optional[str]


class AgentLLM(BaseModel):
    llmId: str


class AgentDatasource(BaseModel):
    datasourceId: str


class AgentInvoke(BaseModel):
    input: str
    sessionId: Optional[str]
    enableStreaming: bool
    outputSchema: Optional[str]


class Datasource(BaseModel):
    name: str
    description: str
    type: str
    content: Optional[str]
    url: Optional[str]
    metadata: Optional[Dict[Any, Any]]
    vectorDbId: Optional[str]


class Tool(BaseModel):
    name: str
    description: str
    type: str
    metadata: Optional[Dict[Any, Any]]
    returnDirect: bool


class AgentTool(BaseModel):
    toolId: str


class LLM(BaseModel):
    provider: str
    apiKey: str
    options: Optional[Dict]


class Workflow(BaseModel):
    name: str
    description: str


class WorkflowStep(BaseModel):
    order: int
    agentId: str


class WorkflowInvoke(BaseModel):
    input: str
    enableStreaming: bool
    sessionId: Optional[str]


class VectorDb(BaseModel):
    provider: VectorDbProvider
    options: Dict
