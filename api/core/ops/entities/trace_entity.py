from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel


class BaseTraceInfo(BaseModel):
    message_id: str
    message_data: Any
    inputs: Union[str, dict[str, Any], list, None]
    outputs: Union[str, dict[str, Any], list, None]
    start_time: datetime
    end_time: datetime
    metadata: dict[str, Any]


class WorkflowTraceInfo(BaseTraceInfo):
    workflow_data: Any
    conversation_id: Optional[str] = None
    workflow_id: str
    tenant_id: str
    workflow_run_id: str
    workflow_run_elapsed_time: Union[int, float]
    workflow_run_status: str
    workflow_run_inputs: dict[str, Any]
    workflow_run_outputs: dict[str, Any]
    workflow_run_version: str
    error: Optional[str] = None
    total_tokens: int
    file_list: list[str]
    query: str
    metadata: dict[str, Any]


class MessageTraceInfo(BaseTraceInfo):
    conversation_model: str
    message_tokens: int
    answer_tokens: int
    total_tokens: int
    error: Optional[str] = None
    file_list: list[str]
    message_file_data: Any
    conversation_mode: str


class ModerationTraceInfo(BaseTraceInfo):
    flagged: bool
    action: str
    preset_response: str
    query: str


#
class SuggestedQuestionTraceInfo(BaseTraceInfo):
    total_tokens: int
    status: Optional[str] = None
    error: Optional[str] = None
    from_account_id: str
    agent_based: bool
    from_source: str
    model_provider: str
    model_id: str
    suggested_question: list[str]
    level: str
    status_message: Optional[str] = None


class DatasetRetrievalTraceInfo(BaseTraceInfo):
    documents: Any


class ToolTraceInfo(BaseTraceInfo):
    tool_name: str
    tool_inputs: dict[str, Any]
    tool_outputs: str
    metadata: dict[str, Any]
    message_file_data: Any
    error: Optional[str] = None
    tool_config: dict[str, Any]
    time_cost: Union[int, float]
    tool_parameters: dict[str, Any]
    file_url: Union[str, None, list]


class GenerateNameTraceInfo(BaseTraceInfo):
    conversation_id: str
    tenant_id: str