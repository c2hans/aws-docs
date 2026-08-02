---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-pattern-1-amazon-bedrock-agent-core.html
---

# Deployment Pattern 1 - Amazon Bedrock AgentCore
<a name="deployment-pattern-1-amazon-bedrock-agent-core"></a>

Amazon Bedrock AgentCore is a fully managed, purpose-built enterprise-grade platform for building, deploying, and operating highly capable AI agents securely at scale, removing the complexity of managing underlying infrastructure. The serverless runtime automatically scales to meet demand without requiring manual infrastructure management, ensuring high availability. Key advantages include enterprise-grade security with isolated sessions and comprehensive observability through integration with Amazon CloudWatch, making it a robust and hassle-free environment for hosting your agent's functionality.

## How it works:
<a name="how-it-works-.aa57201e-8cf5-572e-92a2-869299fd7577"></a>

Amazon Bedrock AgentCore Runtime hosts MCP servers as containerized workloads. When you deploy an MCP server, AgentCore expects a container that exposes the MCP streamable-HTTP endpoint at `0.0.0.0:8000/mcp` — the default path supported by official MCP SDKs (e.g., FastMCP).

**Deployment steps:**

1. **Author the MCP server** — Use the MCP Python SDK (`FastMCP`) or TypeScript SDK to define your tools. Configure the server with `stateless_http=True` (default, recommended) or `stateless_http=False` for stateful multi-turn interactions.

1. **Test locally** — Run the server on `localhost:8000` and validate with an MCP client or the MCP Inspector.

1. **Scaffold the project** — Install the AgentCore CLI (`npm install -g @aws/agentcore`) and run:

   ```
   agentcore create --protocol MCP
   ```

   This generates the project structure including `agentcore/agentcore.json` configuration.

1. **Deploy** — Run `agentcore deploy`. The CLI packages your code and dependencies, uploads to S3, and creates an AgentCore Runtime. You receive an agent runtime ARN.

1. **Invoke remotely** — Clients call the deployed MCP server via the AgentCore invocation endpoint:

   ```
   https://bedrock-agentcore.<region>.amazonaws.com/runtimes/<encoded-arn>/invocations?qualifier=DEFAULT
   ```

1. Authentication uses OAuth bearer tokens (via Cognito) or IAM SigV4.

**Stateless vs Stateful modes:**
+ **Stateless** (`stateless_http=True`): Recommended default. The platform auto-adds `Mcp-Session-Id` headers for connection continuity.
+ **Stateful** (`stateless_http=False`): Required for elicitation (multi-turn prompts), sampling (LLM-generated content), or progress notifications.

For the full walkthrough, see [Deploy MCP servers in AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html).

Sample Implementation:
+ Amazon Bedrock AgentCore with IAM SigV4 sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-agentcore-iam](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-agentcore-iam)
+ Amazon Bedrock AgentCore with OAuth sample implementation: [https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-agentcore-oauth](https://github.com/aws-samples/sample-mcp-deployment-patterns/tree/main/deploy-agentcore-iam)

![Deploy MCP servers in AgentCore Runtime](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/59c72693-ab7d-4dd8-8cb4-83a31e3e9d36.png)

**Architecture Characteristics**
+ Pros: infrastructure management (no servers, containers, or orchestration), built-in authentication and authorization, automatic scaling and high availability, integrated monitoring and logging, native AWS service access, rapid deployment (minutes vs hours/days).
+ Limitations: AWS-specific (no portability), limited runtime customization compared to self-managed options, pricing based on request volume and compute time.
