---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-auto-agents.html
---

# Capability 5. Providing secure access, usage, and implementation of generative AI agents
<a name="gen-auto-agents"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The scope of this capability is to secure autonomous agent functionality for generative AI applications. The following diagram illustrates the AWS services recommended for the Generative AI account for this capability.

![Services for implementing generative AI agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/062194d1-d580-4fa1-b650-7ee796052c27.png)

## Rationale
<a name="gen-auto-agents-rationale"></a>

AI agents extend foundation model (FM) capabilities by orchestrating chains of reasoning steps, tool invocations, and decision-making processes to accomplish complex tasks autonomously. Unlike simple model inference, agents maintain conversation context, make independent decisions about which tools to invoke, and execute multi-step workflows based on user goals rather than explicit instructions.

Agents solve problems that require multiple interactions with external systems. For example, a customer service agent might retrieve order information from a database, check inventory through an API, process a refund through a payment system, and update a CRM. These actions are all based on a single customer request. The agent determines which tools to use, in what sequence, and how to handle errors or unexpected responses.

This capability addresses Scope 3 of the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/). In Scope 3, your organization builds an agentic AI application using a pre-trained FM such as those [models offered in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). You control your application, the tools agents can access, and customer data. The FM provider controls the pre-trained model and its training data.

[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) provides a comprehensive platform for deploying and managing AI agents securely. AgentCore Runtime hosts agents with session isolation, AgentCore Gateway centralizes tool access, AgentCore Memory stores conversation history, AgentCore Identity manages authentication, and AgentCore Observability monitors agent behavior. Combined with [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html), these services address the unique security challenges of autonomous agent systems.

## Security considerations
<a name="gen-auto-agents-security"></a>

Agentic AI applications face security risks that extend beyond those of traditional generative AI applications because of their autonomous decision-making capabilities and persistent state management. The combination of autonomy, tool access, and memory creates attack surfaces that require specialized security controls.
+ Session isolation becomes critical when agents serve multiple users concurrently. Without proper isolation, one user's sensitive data could leak into another user's session through shared memory, cached context, or persistent state. Agents that maintain conversation history across sessions require secure memory stores. These memory stores prevent unauthorized access to historical interactions and protect against memory poisoning attacks where adversaries inject false information to manipulate future agent behavior.
+ Excessive autonomy introduces risks when agents make independent decisions about tool invocations without sufficient constraints. An agent with broad tool access and minimal oversight can do the following:
  + Execute unintended operations.
  + Chain tools in ways that developers did not anticipate.
  + Escalate privileges by combining low-privilege tools to achieve high-privilege outcomes.

  The autonomous nature of agents makes it difficult to predict all possible execution paths, requiring defense-in-depth controls that limit scope when agents behave unexpectedly.
+ Identity and access management complexity increases as agents authenticate with multiple systems on behalf of users. Improper credential management can expose user credentials to the agent runtime, fail to properly scope agent permissions, or allow agents to access resources beyond their intended authorization. Multi-agent architectures compound this complexity when orchestrator agents invoke subordinate agents, each requiring appropriate authentication and authorization at every step in the chain.
+ Secure execution environments become necessary when agents run code or interact with websites. Code execution capabilities enable powerful agent functionality but create risks of arbitrary code execution, resource exhaustion, or access to the underlying host system. Browser automation allows agents to interact with web applications but introduces risks of credential exposure, cross-site scripting, or unintended actions on behalf of users.

## Remediations
<a name="gen-auto-agents-remediations"></a>

This section reviews the AWS services and features that address the risks that are specific to this capability.

### Data protection
<a name="data-protection.32178887-6355-5ba3-887e-b7fa55010738"></a>

Implement session isolation through [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), which runs each user session in a dedicated microVM with isolated CPU, memory, and file system resources. This architecture provides complete separation between user sessions, preventing cross-session data contamination even when agents process requests concurrently. After session completion, AgentCore Runtime terminates the microVM and sanitizes memory, ensuring no data persists between sessions.

Secure agent memory through the [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) namespace structure for logical data isolation. Memory is organized by session ID, actor ID, and strategy ID, preventing users from accessing data belonging to other users. Configure short-term memory retention periods to the minimum required for your use case (up to 365 days). For long-term memory, which lacks built-in retention, implement automated deletion workflows using the [AgentCore Memory API](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteMemoryRecord.html) to comply with data retention policies.

Prevent memory poisoning by ensuring that users can't modify their session ID or actor ID. Don't include `ActorID` or `SessionID` values in system prompts where users could manipulate them. Implement input validation that rejects attempts to inject false information designed to corrupt the agent's memory and influence future behavior.

Encrypt agent data at rest by using AWS Key Management Service (AWS KMS) [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) for AgentCore Memory resources, AgentCore Identity [token vaults](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html#secure-credential-storage), AgentCoreGateway configuration, and Amazon CloudWatch log groups containing agent logs. This approach provides enhanced control over encryption key management and enables detailed audit trails of key usage.

### Identity and access management
<a name="identity-and-access-management.fa66fd89-fbfa-589a-b50e-fb1461f5fa7a"></a>

Design authentication architecture that addresses the following distinct authentication points:
+ User authentication to invoke the agent
+ Agent authentication to access tools and resources
+ Tool authentication to access downstream systems

Each authentication point requires appropriate identity providers and credential management strategies.

Configure inbound authentication using [AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html), which supports both AWS credentials and OAuth 2.0. For AWS credentials, limit [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) principals who can invoke agents by controlling access to the `InvokeAgentRuntime` API. Add IAM conditions to policies that specify the ARN of agents that are hosted by AgentCore, preventing unauthorized invocations. For OAuth 2.0, federate with your corporate identity provider for internal applications or select an identity provider that meets your requirements for external applications. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) integrates natively with AgentCore Runtime to facilitate OAuth authentication.

Assign IAM roles to agents running on AgentCore Runtime that provide minimum permissions required for agent functions. Follow the principle of least privilege by granting access only to specific tools, AWS resources, and secrets that the agent needs. Avoid broad permissions that enable privilege escalation through unintended tool combinations.

Centralize tool access through [AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), which manages both inbound authentication (verifying agent identity) and outbound authorization (connecting to tools). Configure the gateway with a separate identity store from the one used for user authentication. This identity store authenticates agents making calls to gateway targets using the OAuth Client Credentials flow. Store client IDs and client secrets in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) rather than in code or environment variables and configure agents to retrieve credentials at runtime.

Implement outbound authorization using authentication based in IAM with AWS Signature Version 4 (SigV4) for AWS services, OAuth 2.0 for external APIs, or, if needed, API keys for third-party services. When using IAM-based authorization, scope the gateway service role to invoke only registered AWS Lambda functions and access only required secrets. When using API keys, store them securely in [AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) instead of in application code. Add granularity to tool access using OAuth scopes that limit which tools specific agents can invoke.

Configure tool authentication by assigning IAM policies to Lambda functions that interact with AWS resources. Scope policies to only the permissions that each tool needs, preventing tools from accessing resources beyond their intended function.

### Network security
<a name="network-security.5536fda9-d270-5d1b-9388-d602cb40aa07"></a>

Deploy VPC endpoints for AgentCore Runtime and [AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools.html) to enable private connectivity without internet exposure. This architecture allows agents to access private resources, maintain secure communications within your network boundaries, and connect to enterprise data stores while preserving security isolation.

Configure [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to protect public-facing agent applications from common web exploits. Create custom AWS WAF rules that detect prompt injection patterns, rate limit requests to prevent abuse, and block malicious traffic before it reaches your agents.

Implement network-level monitoring through [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to track traffic patterns between agents and tools. Configure flow logs to capture accepted and rejected traffic, providing visibility into network communications for security analysis and threat detection.

### Application security
<a name="application-security.e84ab299-483c-54b2-a026-71da92bdb038"></a>

Evaluate tool architecture by assessing which capabilities agents require and whether those capabilities justify the associated risks. Limit agent access to mutative or destructive operations, implementing additional security controls for high-impact actions. Controls include instruction hardening that makes agent prompts resistant to manipulation, human-in-the-loop approval for sensitive operations, and [least-privilege IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) that reduces access risks.

Deploy Amazon Bedrock Guardrails to protect agents from prompt attacks, prevent unwanted behavior, and limit hallucinations. Configure guardrails with content filters appropriate for your use case, define denied topics that agents should not discuss, and create custom word filters for organization-specific sensitive terms. Deploy guardrail versions to production and configure agents to invoke the versioned guardrail as part of their response generation.

Implement pre-processing validation through Lambda functions that sanitize and validate input before passing it to agents. This additional layer of defense detects malicious prompts that attempt to bypass guardrails or manipulate agent behavior. Regularly test applications for prompt attacks using adversarial testing techniques.

Use [AWS Security Agent](https://docs.aws.amazon.com/securityagent/latest/userguide/what-is.html) to accelerate security reviews by analyzing architecture documents against AWS best practices and organizational requirements during the planning phase. It scales secure code analysis by automatically reviewing pull requests for common vulnerabilities and providing immediate remediation guidance within developer workflows. Additionally, the agent enables on-demand penetration testing to discover and report validated security vulnerabilities through tailored, multi-step attack scenarios.

### Logging and monitoring
<a name="logging-and-monitoring.f4c828ec-b473-53da-ba7e-6598270aba5f"></a>

Enable [AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to trace, debug, and monitor agent activity. Configure [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) in CloudWatch and enable observability for agents hosted by AgentCoreRuntime. This approach provides visibility into agent behavior, including input and output prompts, reasoning traces, and tool invocations.

Monitor tool usage through [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and CloudWatch to detect anomalous patterns. Create CloudWatch metrics that track tool invocation rates, execution duration, and error rates. Set alarms that trigger when metrics deviate from established baselines, indicating potential security issues or agent misbehavior.

Configure [AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) to emit logs to CloudWatch, providing visibility into data plane events such as `CreateEvent`, `DeleteEvent`, and `RetrieveMemoryRecords`. Use these logs to audit memory access patterns and detect unauthorized attempts to access or manipulate agent memory.

Implement centralized log aggregation by forwarding all agent-related logs to the [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html). This approach enables security teams to correlate events across multiple agents and detect attack patterns that span multiple sessions or users.

## Recommended AWS services
<a name="gen-auto-agents-services"></a>

This section discusses the AWS services and features that address the security risks that are specific to this capability. In addition to the services in this section, use Amazon CloudWatch, AWS CloudTrail, Amazon OpenSearch Serverless, Amazon S3, and Amazon Comprehend as explained in Capability 1 (model inference) and Capability 3 (RAG).

### Amazon Bedrock AgentCore Runtime
<a name="9999999999999999braclong--runtime.39180762-ffe8-56d1-b27a-0c5844817f0c"></a>

[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides secure, serverless hosting for AI agents with complete session isolation using dedicated microVMs. Each user session runs with isolated CPU, memory, and file system resources, ensuring separation between users and preventing cross-session data contamination.

Configure customer managed [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) for enhanced encryption control over session data. AgentCore Runtime automatically terminates sessions and sanitizes memory after completion, providing deterministic security even with non-deterministic AI processes. The service supports both real-time interactions and long-running workloads up to 8 hours while maintaining security isolation.

### Amazon Bedrock AgentCore Memory
<a name="9999999999999999braclong--memory.d96c0bab-e934-5a31-8923-9490c990bc98"></a>

[AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides secure storage for agent conversation history and context across sessions. The service offers two [memory types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html):
+ *Short-term memory* for turn-by-turn interactions within a single session
+ *Long-term memory* for persistent knowledge retention across multiple sessions

Configure short-term memory retention periods to the minimum required for your use case. Implement automated deletion workflows for long-term memory to comply with data retention policies. Use the namespace structure (session ID, actor ID, and strategy ID) to enforce logical data isolation between users. Encrypt memory resources with customer managed KMS keys and restrict IAM access to memory APIs (such as `ListMemoryRecords`, `GetMemoryRecord`, `CreateMemoryRecord`, and `DeleteMemoryRecord`) to authorized services only.

### Amazon Bedrock AgentCore Gateway
<a name="9999999999999999braclong--gateway.063a452c-29c3-5539-a423-1fb773b91b94"></a>

[AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) centralizes tool access and management, providing a single point of control for agent-tool interactions. The gateway manages both inbound authentication (verifying agent identity) and outbound authorization (connecting to tools), simplifying security architecture.

Configure the gateway with a separate identity store for agent authentication using OAuth Client Credentials flow. Implement outbound authorization using IAM-based authentication for AWS services, OAuth 2.0 for external APIs, or API keys for third-party services. Create VPC endpoints for private connectivity and apply endpoint policies to restrict access to authorized agents. Encrypt gateway configuration with customer managed KMS keys.

### Amazon Bedrock AgentCore Identity
<a name="9999999999999999braclong--identity.a6fe8400-bf94-5e0f-9437-7fd6da2f4bb9"></a>

[AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) serves as a secure credential broker for agents, supporting AWS Signature Version 4 (SigV4) signing, OAuth 2.0 with JWT bearer tokens, and API key authentication. The service maintains a protected [token vault](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html#secure-credential-storage) using AWS Key Management Service (AWS KMS) encryption for credential storage.

Configure integration with enterprise identity providers including Amazon Cognito, Okta, and Microsoft Entra ID. Implement credential rotation policies through integration with AWS Secrets Manager. AgentCore Identity ensures complete separation between ingress authentication (verifying user identity) and egress authorization (accessing tools), preventing credential exposure.

### Amazon Bedrock AgentCore Observability
<a name="9999999999999999braclong--observability.e583d66f-e28c-5627-ab04-9fdeb996022c"></a>

[AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides comprehensive monitoring, tracing, and debugging capabilities for agent behavior. Enable [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) in CloudWatch to track agent execution paths, tool invocations, and reasoning traces.

Configure observability to capture input and output prompts, tool call parameters, and error conditions. Use trace data to identify security issues, performance bottlenecks, and unusual access patterns. Integrate with [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to trigger automated responses when agents exhibit anomalous behavior.

### Amazon Bedrock Guardrails
<a name="9999999999999999brlong--guardrails.70368c56-c78b-5d6a-9d11-6c12a8f6799c"></a>

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) provides configurable safeguards that detect and filter harmful content, prevent prompt attacks, and reduce hallucinations. Configure content filters across multiple categories (hate, insults, sexual, violence, misconduct, and prompt attacks) with filter strength appropriate for your risk tolerance.

Define denied topics to prevent agents from discussing sensitive subjects or internal systems. Create custom word filters for organization-specific sensitive terminology. Implement contextual grounding checks to detect hallucinations and verify response accuracy against source documents. Deploy guardrail versions to production and configure agents to invoke versioned guardrails for consistent protection.

### AWS Security Agent
<a name="9999999999999999aws--security-agent.91e9eb66-0858-5f50-b629-22e29b0cac4d"></a>

[AWS Security Agent](https://docs.aws.amazon.com/securityagent/latest/userguide/what-is.html) is an autonomous agent that provides continuous application security validation across the software development lifecycle (SDLC). It functions as a virtual security engineer by conducting automated architectural reviews against organizational standards and performing on-demand penetration testing to identify exploitable vulnerabilities.

Configure the agent to analyze code bases and design documents for early vulnerability detection. It leverages context-aware reasoning to execute multi-step attack chains, discovering complex risks that traditional scanners miss. The agent integrates developer workflows to provide actionable remediation guidance and automated pull requests. The agent helps scale security validation with development velocity without using customer data for underlying model training.

### Amazon GuardDuty
<a name="9999999999999999gdulong-.4e477647-197d-5899-beda-a262df296375"></a>

[GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) provides threat detection for agentic applications by monitoring AWS CloudTrail management events for suspicious and malicious activity. The service detects unauthorized access attempts, unusual API call patterns, and potential compromises of agent infrastructure.

Enable GuardDuty in the [Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) as the delegated administrator for centralized management across the organization. Configure automated responses to GuardDuty findings using [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that trigger remediation workflows when threats are detected.

### Amazon Inspector
<a name="9999999999999999inslong-.b74a8772-89ff-57c3-99f5-d3d907869e41"></a>

[Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) scans agent code for known software vulnerabilities, identifying security issues in Lambda functions, container images, and [Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html) hosting agent components. The service provides continuous vulnerability assessment and prioritized findings based on risk.

Enable Amazon Inspector in the [Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) as the delegated administrator for centralized vulnerability management. Configure automated scanning for all agent-related resources and integrate findings with your security information and event management (SIEM) system for comprehensive security monitoring.

### AWS KMS
<a name="9999999999999999kms-.06e490ea-0a29-5702-96de-33204427ec63"></a>

[AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) (AWS KMS) helps you create and control cryptographic keys to help protect your data. Use customer managed AWS KMS keys to encrypt AgentCore Memory resources, AgentCore Identity token vaults, AgentCore Gateway configuration, and CloudWatch log groups that contain agent logs. Customer managed KMS keys provide enhanced control over encryption key management, enable detailed audit trails of key usage, and support key rotation policies.

Configure key policies that grant encryption and decryption permissions only to authorized services and IAM roles. Enable CloudTrail logging for all KMS key usage to maintain comprehensive audit trails of data access.

Use CloudWatch, CloudTrail, Amazon OpenSearch Serverless, Amazon S3, and Amazon Comprehend as explained in [Capability 1 (model inference)](gen-ai-model-inference.md) and [Capability 3 (RAG)](gen-ai-agents.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
