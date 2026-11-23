---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/mcp-server.html
---

# Model Context Protocol (MCP)

## MCP Server
<a name="mcp-server.46ec48e3-2fca-536e-821b-d70c5c7de25a"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/3c4f4b85-4231-494e-b6e2-929130078815.png)

Data Flow

**1. MCP Client → AgentCore Gateway** The MCP Client initiates a connection to the MCP Server endpoint exposed via **Amazon Bedrock AgentCore Gateway**. AgentCore Gateway supports two inbound authorization mechanisms: **IAM SigV4** (the default, requiring no additional configuration) and **JWT/OIDC bearer tokens** from trusted identity providers — including Amazon Cognito, Microsoft Entra ID, Okta, Auth0, Keycloak, and other OIDC-compliant providers. For JWT authorization, the Gateway is configured with a discovery URL, allowed audiences, and optionally allowed client IDs. The Gateway validates the token, enforces access policies, and routes the MCP tool invocation to the configured backend target.

**2. AgentCore Gateway → AWS Lambda (MCP-Enabled Tool)** AgentCore Gateway MCP-enables an **AWS Lambda** function by mapping MCP tool definitions to Lambda invocations — without requiring changes to the Lambda function's core logic. The Gateway manages session context, input schema validation, and response formatting, returning structured MCP-compliant tool responses to the client. Lambda executes within a VPC or public subnet depending on the target data source or service integration.

**3. (Optional) Lambda → AgentCore Runtime (Agent-as-Tool Pattern)** For use cases requiring multi-step reasoning or orchestration, the Lambda function invokes **Amazon Bedrock AgentCore Runtime**, implementing the *Agent-as-Tool* pattern. AgentCore Runtime hosts the agent process in an isolated, serverless execution environment with managed memory and session state. Any supported agent framework — such as **AWS Strands** — can run within AgentCore Runtime, enabling the MCP tool to transparently delegate to a full agentic workflow.

**4. Observability — OpenTelemetry Integration** All components emit traces, metrics, and logs via **OpenTelemetry (OTel)**. AgentCore Runtime natively supports OTel instrumentation, capturing agent reasoning steps, tool invocations, latency, and token usage. Telemetry is exported to **AWS X-Ray** for distributed tracing and **Amazon CloudWatch** for metrics and log aggregation — providing end-to-end visibility across the MCP client, Gateway, Lambda, and agent execution layers.

**5. Security & Governance** AgentCore Gateway enforces **IAM-based authentication** and supports resource-based policies for fine-grained tool access control. Lambda execution roles follow least-privilege principles. Optionally, **Amazon Bedrock Guardrails** — including Automated Reasoning checks — can be applied within the agent pipeline to validate outputs before returning responses to the MCP client.

*[Tool Catalog for Answer-Getting](tool-catalog-for-answer-getting.md)*
