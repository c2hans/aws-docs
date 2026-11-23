---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/agent-to-agent-a2-a-protocol.html
---

# Agent-to-Agent (A2A)

The **Agent-to-Agent (A2A) Protocol** enables external agents to discover and delegate tasks to Orchestration Layer agents (Q&A Agent, Business Elicitation Agent, Ontology Maintenance Agent) using **HTTP \+ JSON-RPC 2.0 \+ SSE**.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/00ce1347-71cc-43b2-81a6-01f8a92f4f52.png)

**Agent Discovery**

Each agent publishes an **Agent Card** (JSON document) advertising capabilities, schemas, and endpoints. External agents discover cards via Agent Registry, DNS-SD, or `./well-known/agent-card.json`.

**Q&A Agent Card**

```
{
  "agent_id": "urn:aws:bedrock:...:agent/qa-agent",
  "name": "Question & Answer Agent",
  "capabilities": [{
    "capability_id": "semantic_qa",
    "input_schema": { "question": "string", "ontology_id": "string?" },
    "output_schema": { "answer": "string", "evidence": "array", "citations": "array" }
  }],
  "endpoints": { "invoke": "/invoke" },
  "authentication": {
    "methods": ["IAM_SigV4", "JWT_OIDC"],
    "required_claims": ["sub", "groups", "act"],
    "scope": "semantic-layer:access"
  }
}
```

## Task Delegation Workflow
<a name="task-delegation-workflow.5373033b-44b4-5d72-833d-2e27ff11862f"></a>

**1. Discovery** → External agent retrieves Agent Card

**2. Invocation** → Sends JSON-RPC request:

```
{
  "jsonrpc": "2.0",
  "method": "semantic_qa",
  "params": { "question": "What is the average claim amount for diabetes patients in Q4 2025?" }
}
```

**3. Authentication** → JWT/OIDC validation (preferred) or IAM SigV4 for AWS-native callers

**4. Execution** → Agent orchestrates internal services (Intent Classification, VKG, GraphRAG, Reasoning)

**5. Response** → Returns result with answer, evidence, citations, confidence

**6. Async (Optional)** → Long-running tasks return `task_id` and stream progress via SSE

## Orchestration Layer Agents
<a name="orchestration-layer-agents.91e9754f-5147-544c-b458-626c00cf1012"></a>

All agents can support A2A delegation:
+ **Q&A Agent** — Semantic question answering with federated knowledge graphs
+ **Business Elicitation Agent** — Business rule extraction, requirement validation
+ **Ontology Maintenance Agent** — Entity resolution, ontology alignment, truth maintenance

## A2A \+ MCP Integration
<a name="a2a---mcp-integration.acc826fb-3012-56ba-80ac-5c3cbb9b6477"></a>

**A2A** (agent-to-agent) and **MCP** (agent-to-service) are complementary:

```
External Agent → A2A → Q&A Agent → MCP → Semantic Layer Services
```

## Security & Observability
<a name="security-9999999999999999amp--observability.2037ef41-a967-5d0c-8f4c-48da767e757c"></a>

**Auth** — Auth - JWT/OIDC (preferred), IAM SigV4 (AWS-native callers) \| Authz - Group-based authorization via JWT `groups` claim with `semantic-layer:access` scope

**Observability** — OpenTelemetry traces, CloudWatch Logs, AWS X-Ray

**Provenance** — All responses include source data, reasoning steps, ontology axioms

## Benefits
<a name="benefits.7600188e-f81c-5f45-a14c-5f8192a9c52d"></a>

**Interoperability** — Agents from different vendors collaborate without custom integration

**Scalability** — Enterprise-wide agent discovery and delegation

**Open Standards** — Linux Foundation governance ensures long-term compatibility.
