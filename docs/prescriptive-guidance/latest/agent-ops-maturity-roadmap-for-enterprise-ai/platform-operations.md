---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/platform-operations.html
---

# Platform operations
<a name="platform-operations"></a>

This section covers the operational infrastructure that spans all accounts in the platform: how agents are deployed and promoted across environments, how accounts communicate securely, how governance is enforced, how telemetry is aggregated, and how costs are tracked. These are cross-cutting concerns that operate between accounts rather than within any single one.

## Security and governance
<a name="security-and-governance"></a>

Security for agentic AI systems combines standard AWS multi-account controls with governance mechanisms specific to autonomous agent behavior. SCPs enforce platform-wide boundaries at the organizational unit level. Agent-specific governance addresses the unique risks of autonomous systems: unbounded token consumption, uncontrolled tool access, and actions taken without human oversight.

### Service control policies
<a name="service-control-policies.d4006230-d0fe-574b-bd4a-2e4f092f3044"></a>

Apply SCPs at the Agentic organizational unit level to enforce three controls uniformly across all agent runtime accounts:
+ **Region restriction. **Limit AI workloads to the AWS Regions where your data residency and compliance requirements are met. AI services are expanding across regions rapidly; without this control, a misconfigured deployment can land in an unsanctioned region.
+ **Service allowlisting. **Permit only the AWS services required for Agentic AI operations. This reduces the attack surface and simplifies compliance scope.
+ **Privilege escalation prevention. **Restrict IAM actions that could allow an account-level principal to bypass the account boundaries the architecture depends on.

### Agent-specific governance
<a name="agent-specific-governance.af1f8ab2-78b3-5787-8ef1-eecab132caba"></a>
+ **Model access controls. **Use Amazon Bedrock model access policies to govern which foundation models are available in each environment. Development accounts can access a broader set of models for experimentation; production accounts should be restricted to approved models that have completed your organization's security and privacy review.
+ **Token budget enforcement. **Implement rate limiting and budget alerts in the generative AI gateway accounts. Autonomous agents can enter extended reasoning loops that consume tokens at rates no individual developer would anticipate. Budget enforcement at the gateway layer catches overruns before they become significant cost events.
+ **Data classification. **Tag and classify data flowing through agent interactions. Use Amazon Macie to detect sensitive data in conversation logs and agent outputs, particularly where agents have access to customer data or internal documents.
+ **Human-in-the-loop checkpoints. **For production agents that perform consequential actions, including financial transactions, infrastructure changes, or communications sent on behalf of users, implement approval workflows that pause agent execution pending human review. Not all agents require the same governance posture. Design tiered controls based on the consequences of agent actions rather than applying uniform restrictions.
+ **Bedrock Guardrails.** Deploy Amazon Bedrock Guardrails on all model invocations to filter prompt injection attempts, block sensitive information disclosure, and enforce content policies. Enable prompt attack filters as a baseline requirement. Guardrails operate independently of application logic and provide a consistent safety layer across all agents regardless of framework.

For comprehensive security best practices covering threat modeling, input validation, data governance, and incident response for agentic AI systems, see [Security for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html) in AWS Prescriptive Guidance.

## Networking and connectivity
<a name="networking-and-connectivity"></a>

Cross-account networking connects the platform's isolated accounts while preserving the security boundaries the architecture depends on. The primary traffic pattern is workload-to-gateway: every agent model invocation crosses an account boundary. The networking design ensures this traffic stays private, environment-isolated, and auditable.

|
|
| NoteThe architecture diagram omits the networking account for simplicity. In enterprise deployments, a dedicated networking account hosts Transit Gateway for inter-account routing, PrivateLink endpoint service configurations, centralized NAT gateways, and Network Firewall for controlled internet egress. |
| --- |

### Cross-account communication
<a name="cross-account-communication.3aaca1f0-d941-5e24-ba25-d1629d7e4c50"></a>

Use AWS PrivateLink to expose generative AI gateway services and shared tooling services to workload accounts. PrivateLink endpoints keep traffic on the AWS network backbone and avoid the complexity of VPC peering across many-to-many account relationships.

In each workload account, deploy VPC endpoints for the generative AI gateway in the corresponding environment (dev workload → dev gateway, staging → staging gateway, prod → prod gateway). This is the primary cross-account communication path: every model invocation from an agent runtime traverses this connection. Deploy additional VPC endpoints for AWS service access to Amazon Bedrock, Amazon S3, and Amazon DynamoDB.

For organizations with an existing networking account, use AWS Transit Gateway for inter-account routing and apply network segmentation through route table associations. Ensure that route tables enforce environment isolation - dev workload accounts should not be able to reach the production gateway, and vice versa.

### Internet access
<a name="internet-access.852b5bb6-1177-5d52-9756-c8ecc664737e"></a>

Agentic workloads that require external API access, such as calls to third-party tool endpoints or external data sources, should egress through a centralized NAT gateway or AWS Network Firewall in the networking account. Apply allowlisting for outbound destinations. Agents should only reach approved external endpoints, and every outbound connection should be logged.

## CI/CD agent promotion pipeline
<a name="ci-cd-agent-promotion-pipeline"></a>

The CI/CD pipeline, implemented using AWS CodeCommit, AWS CodePipeline and AWS CodeBuild in the shared tooling account, governs all agent promotions from code commit through production deployment. Every promotion decision is gated by automated evaluation, manual approval, or both. The pipeline architecture enforces a single artifact through all environments. Because the container image is built once and promoted by digest reference, there is no possibility of a configuration difference between what was validated in staging and what runs in production.

### Pipeline stages
<a name="pipeline-stages.70b21718-98b1-551d-880e-16dc41bc049d"></a>

1. **Build. **Agentic engineers push to feature or main branches in CodeCommit from their local IDE. CodeBuild compiles the agent code, runs unit tests, and pushes the resulting container image to the shared Amazon ECR registry in the shared tooling account. All subsequent pipeline stages consume this image by digest reference.

1. **Deploy to dev and evaluate. **CodeBuild deploys the image to the development account. AgentCore Evaluations runs on-demand against the deployed agent, executing a defined set of behavioral and performance tests. The pipeline proceeds only if the evaluation passes the configured quality gate. Failures halt promotion and require the engineering team to address the underlying issue before re-triggering.

1. **Promote to staging. **A manual approval gate requires a lead engineer or product owner to review the evaluation results before the pipeline promotes the agent to staging. This gate is intentional: it ensures that a human with product context, not just automated test coverage, makes the promotion decision. CodeBuild deploys the same image digest to the staging account.

1. **Promote to production. **A second manual approval gate guards production promotion. After approval, CodeBuild deploys to the production account. AgentCore online evaluation activates in production to provide continuous monitoring for drift between releases.

This pipeline runs entirely within the shared tooling account. Workload accounts receive deployments but never execute build or promotion logic.

## Observability and monitoring
<a name="observability-and-monitoring"></a>

Traditional application monitoring is insufficient for agentic AI workloads. Agents execute multi-step reasoning chains, invoke external tools, and consume model tokens at variable rates. These behaviors are not visible through standard infrastructure metrics. The observability account provides a unified view of agent behavior, cost, and performance across all workload accounts without requiring direct access to workload resources.

### Agent-specific telemetry
<a name="agent-specific-telemetry.ad28206e-ef9d-5519-8a68-44052a8c5ad4"></a>

The observability account should capture the following telemetry categories:

|
|
| Telemetry type | Description | Key metrics |
| --- |--- |--- |
| **Agent traces** | End-to-end execution path of agent reasoning, tool use, and response generation | Latency per reasoning step, tool call success rate, reasoning chain depth |
| **Model metrics** | LLM performance and cost data per invocation | Tokens consumed (input and output), latency percentiles (p50, p95, p99), error rates by model |
| **Token usage analytics** | Cost attribution and budget tracking across agents and environments | Spend by agent, by environment, by model; trend analysis for capacity planning |
| **Tool invocation metrics** | MCP server and external tool performance | Call frequency, latency, error rates, retry counts |
| **Business metrics** | Agent effectiveness at the task level | Task completion rate, escalation rate, user satisfaction scores where measurable |

### Alerting and operational response
<a name="alerting-and-operational-response.f884fdf5-d337-5141-8757-a4a0a56b7df1"></a>

Define alerting thresholds for critical metrics. At minimum, configure alarms for:
+ **Token spend** exceeding the daily or weekly budget for any agent or environment.
+ **Agent error rates** rising above the established baseline, indicating a deployment regression or upstream model degradation.
+ **Tool call latency** exceeding SLA thresholds, which can cause agent timeouts and cascading task failures.
+ **Guardrail block rate spikes**, which may indicate an active prompt injection campaign or a change in user behavior that requires investigation.

## Cost optimization
<a name="untitled"></a>

Agentic AI workloads introduce cost patterns that differ from traditional infrastructure. Token consumption scales with reasoning complexity, not compute provisioning. A single agent processing a complex request can consume more budget in one invocation than an idle server costs in a day. Cost management requires attribution at the agent level, proactive alerting for budget overruns, and right-sizing strategies that evolve as workload patterns stabilize.

### Cost allocation strategy
<a name="cost-allocation-strategy.a77cac8d-6f2f-51f1-8efc-f96f5711219d"></a>

Enable AWS Cost Allocation Tags across all platform accounts from day one. Apply consistent tags: Platform=AgenticAIPlatform, Environment={dev\|staging\|prod}, and Agent={agent-name}. Retrofitting tags across a multi-account structure after workloads are running is substantially more expensive than enforcing them from the start.

Use the model gateway in each generative AI gateway account to track per-agent and per-model token consumption and attribute costs to business units. Within a given environment, the gateway is the single point through which all model invocations pass, regardless of which workload account initiated them. Aggregate gateway-level cost data across environments in the observability account to produce a unified, platform-wide view of token spend.

Set AWS Budgets alerts at both the account level and the OU level. AI workloads can produce cost spikes that are qualitatively different from conventional infrastructure: a single agent entering an unintended loop can exhaust a monthly budget in hours.

### Right-sizing guidance
<a name="right-sizing-guidance.f6783e6c-1358-57fe-94e6-193782cdd17b"></a>
+ Start with on-demand capacity for development and early experimentation. Do not over-provision.
+ Move to Provisioned Throughput for Amazon Bedrock and reserved capacity for self-hosted models once production workloads have established a predictable baseline.
+ Evaluate smaller, task-specific models for routine agent operations. Not every invocation requires the most capable foundation model. Use model access policies in the gateway to route traffic to the most cost-effective model that meets the quality threshold for each use case.
+ Use data lake account analytics to identify cost optimization opportunities from historical usage patterns before committing to reserved capacity.

For a comprehensive framework covering ROI analysis, human-versus-agent cost modeling, and break-even calculations for agentic AI investments, see [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/introduction.html) in AWS Prescriptive Guidance.

## Limitations and considerations
<a name="limitations-and-considerations"></a>

The following considerations may affect deployment timelines or require additional planning beyond the core architecture.
+ **CloudWatch cross-account dashboards. **Some widget types and custom metric configurations require additional IAM trust configuration to function across account boundaries. Test dashboard rendering during initial deployment before building operational workflows that depend on it.
+ **Cross-account latency. **AWS PrivateLink and cross-account API calls introduce latency overhead compared to in-account calls. For latency-sensitive agent workloads, benchmark the overhead during development and consider co-locating time-critical resources where the architecture permits.
+ **Service quotas. **AWS accounts have default service quotas. When running multiple agents at high concurrency, request quota increases for Amazon Bedrock, AWS Lambda, and Amazon ECS in workload accounts ahead of production launch. Quota requests can take several business days to process.
+ **MCP protocol maturity. **The Model Context Protocol is an evolving standard. Vendor implementations differ, and breaking changes in MCP server libraries have occurred between minor versions. Build upgrade testing into your shared tooling account change management process and version-pin MCP dependencies in production.
+ **Model availability by region.** Not all Amazon Bedrock foundation models are available in all AWS Regions. If your SCPs restrict workloads to specific regions for data residency or compliance reasons, verify that your required models are available in those regions before finalizing the architecture.

Some AWS services aren't available in all AWS Regions. For Region availability, see the Service endpoints and quotas page in the AWS documentation, and choose the link for the service.
