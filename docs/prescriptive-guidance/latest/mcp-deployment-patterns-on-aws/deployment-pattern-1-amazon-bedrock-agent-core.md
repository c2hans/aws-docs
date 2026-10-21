---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-1-amazon-bedrock-agent-core.html
---

# Deployment Pattern 1 - Amazon Bedrock AgentCore
<a name="deployment-pattern-1-amazon-bedrock-agent-core"></a>

Amazon Bedrock AgentCore provides two approaches for exposing MCP capabilities on AWS: AgentCore Gateway and AgentCore Runtime. AgentCore Gateway converts existing AWS Lambda functions and APIs into MCP-compatible tools without requiring a standalone MCP server. AgentCore Runtime hosts custom MCP server implementations.

For most new deployments, use AgentCore Gateway when existing Lambda functions or APIs provide the required business logic. Use AgentCore Runtime only when Gateway does not support the required target or when the solution requires a custom MCP server implementation.

## How it works:
<a name="how-it-works-.185d5907-05f4-52d8-aa78-cbd1ab5d6284"></a>

With AgentCore Gateway, MCP clients connect to a managed Streamable HTTP endpoint. Gateway uses the configured Lambda tool schema or OpenAPI specification to present target operations as MCP tools. When a client invokes a tool, Gateway authenticates and authorizes the request, translates it into a target-specific request, invokes the target using configured credentials, and returns the result as an MCP response.

Policy in AgentCore provides fine-grained authorization for individual tools. Request and response interceptors support custom validation, identity propagation, request transformation, and response filtering. Guardrail policies provide content controls when required.

With AgentCore Runtime, teams package and deploy a custom MCP server as a managed workload. Use Runtime only when the implementation requires custom MCP server behavior that Gateway targets cannot provide.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/3971a52b-a405-4fd2-8cae-6cec4f632cb9.png)

**Deployment steps:**

1. **Select the AgentCore approach **– Use AgentCore Gateway for existing Lambda functions and APIs. Use AgentCore Runtime only for custom MCP server implementations.

1. **Select the Gateway target **– Use a Lambda target for business logic implemented in Lambda. Use an OpenAPI or API Gateway target for an existing REST API with an OpenAPI specification.

1. **Define the tools** – Provide a clear name, description, input schema, and expected output for each tool.

1. **Create the Gateway **– Create an AgentCore Gateway and configure JWT or IAM authentication for MCP clients.

1. **Add the target** – Register the Lambda function or OpenAPI specification with the Gateway.

1. **Configure target credentials** – Grant the Gateway only the permissions required to invoke the target. Use IAM for Lambda and an authentication method supported by the target API.

1. **Apply authorization policies** – Use default-deny Cedar policies that permit only the required identities and tools.

1. **Add additional controls **– Configure interceptors when requests or responses require validation, transformation, or filtering. Add guardrail policies when content controls are required.

1. **Test the deployment** – Validate tools/list, successful tools/call requests, invalid inputs, and denied requests with an MCP client or MCP Inspector.

1. **Configure monitoring **– Monitor requests, authorization decisions, target errors, latency, and throttling.

Sample implementation
+ [AgentCore Gateway target configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets.html)
+ [AgentCore Runtime custom MCP server](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)

![Deploy MCP servers in AgentCore Runtime](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/59c72693-ab7d-4dd8-8cb4-83a31e3e9d36.png)

**Architecture Characteristics**
+ Pros: AgentCore Gateway removes the need to develop and operate a standalone MCP server for supported targets. It provides managed MCP translation, authentication, credential management, fine-grained authorization, guardrails, interceptors, and observability. Teams can reuse existing Lambda functions and REST APIs. AgentCore Runtime provides a managed deployment option when a custom MCP server is required.
+ Limitations: AgentCore Gateway requires a supported target and a defined tool schema. Teams remain responsible for operating the Lambda functions and APIs behind the Gateway. Gateway introduces additional request cost and latency. Implementations that require custom MCP server behavior must use AgentCore Runtime or another hosting pattern.
