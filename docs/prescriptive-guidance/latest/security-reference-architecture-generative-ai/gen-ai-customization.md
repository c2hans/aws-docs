---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-customization.html
---

# Capability 4. Providing secure access, usage, and implementation of tools
<a name="gen-ai-customization"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The scope of this capability is to secure tool access and authentication for AI applications. The following diagram illustrates the AWS services recommended for the Generative AI account for this capability.

![Services recommended for the Generative AI account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/9e20180d-f6ad-463e-91e2-43e939820376.jpeg)

## Rationale
<a name="customization-rationale"></a>

Tool integration extends AI capabilities by connecting foundation models (FMs) to external functions and services. AI applications integrate tools through the following patterns:
+ AWS Lambda functions for serverless business logic
+ Model Context Protocol (MCP) servers for standardized tool interfaces
+ External APIs for real-time data access
+ Operating system tools for system-level operations
+ Agent-to-agent (A2A) communication protocols for multi-agent workflows

This capability addresses Scope 3 of the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/). In Scope 3, your organization builds a generative AI application using a pre-trained FM such as those offered in Amazon Bedrock while integrating external tools and services. You control your application, the tools it accesses, customer data, and permissions granted to the AI application. The FM provider controls the pre-trained model and its training data.

**Note**
Although this guidance focuses on application-level tool integration with Amazon Bedrock FMs (Scope 3), similar principles apply to fine-tuned and self-trained models (Scopes 4 and 5).

For user-facing AI applications that provide tool access to end users, see Capability 6.

## Security considerations
<a name="customization-security"></a>

AI applications with tool access face unique security risks that extend beyond traditional application vulnerabilities. When you grant AI applications the ability to invoke external functions and services, you create new attack surfaces. Adversaries can exploit these surfaces through both technical vulnerabilities and manipulation of the AI's reasoning process:
+ Tool access introduces authentication and authorization challenges across multiple integration points. Unauthorized tool access can occur when authentication mechanisms fail to properly validate AI application identities, or when authentication credentials are exposed during tool invocation chains. Adversaries who gain unauthorized access can execute privileged operations, access sensitive data, or manipulate business logic.
+ Prompt injection attacks represent a threat vector specific to AI applications with tool access. Attackers craft malicious inputs designed to manipulate the AI's reasoning process, causing it to misuse tools or generate malicious parameters for tool invocations. The AI application may interpret attacker-controlled prompts as legitimate instructions, leading to unintended tool executions that compromise security controls.
+ Privilege escalation risks emerge when AI applications chain multiple tools with varying permission levels. An attacker who compromises a low-privilege tool can potentially leverage the AI's orchestration capabilities to access higher-privilege tools through unintended combinations. This risk intensifies in autonomous agent scenarios where the AI makes independent decisions about which tools to invoke and in what sequence.
+ Resource exhaustion and API abuse pose operational and security risks when AI applications make excessive tool calls. AI-driven workloads can generate high volumes of tool invocations through reasoning loops or self-perpetuating execution patterns. Adversaries can exploit this behavior to launch denial-of-service attacks by crafting prompts that trigger resource-intensive tool chains, exhausting API limits and consuming compute resources.
+ Supply chain vulnerabilities affect both upstream and downstream components in tool integration architectures. Upstream risks include compromised tool dependencies, malicious MCP servers, or vulnerable third-party APIs. Downstream risks involve insecure network routes between AI applications and external tools, man-in-the-middle attacks on tool communication channels, and exposure of sensitive data in transit.

## Remediations
<a name="customization-remediations"></a>

This section reviews the AWS services and features that address the risks that are specific to this capability.

### Data protection
<a name="data-protection.49a40d4d-79f7-593c-9d2b-9c0dcc1bb7c1"></a>

Encrypt tool inputs, outputs, and execution contexts in transit and at rest using AWS Key Management Service (AWS KMS) [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html). Amazon Bedrock AgentCore [encrypts all data at rest and in transit by default](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-encryption.html). Use TLS 1.2 or higher with AES-256 encryption for all tool communications.

Implement session isolation to prevent data leakage between tool executions. [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides dedicated microVM architecture that isolates each session with separate CPU, memory, and file system resources. Sessions terminate automatically and purge all state data to prevent cross-contamination.

Store authentication credentials for external tool access in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) encrypted with customer managed keys. Configure [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) as a secure credential broker that retrieves credentials at runtime without exposing them to AI applications.

Apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to validate and filter tool inputs and outputs across all integration patterns. Configure guardrails to detect and block malicious parameters, sensitive data exposure, and policy violations before tools execute.

### Identity and access management
<a name="identity-and-access-management.ac3315b1-0da1-54c5-bbd8-fb284f59fa37"></a>

Create custom service roles for AI application tool integration following the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). Grant permissions only for specific tools and AWS services that are required for your use case. Implement permission boundaries to prevent privilege escalation through unintended tool combinations.

Configure AgentCore Identity as a secure credential broker supporting Signature Version 4 (SigV4) signing for AWS services and OAuth 2.0 authentication for external APIs. Store credentials in AWS Secrets Manager with automatic rotation where supported by external services.

Implement fine-grained access controls through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) centralized tool management. Register tools explicitly and configure which AI applications can invoke each tool. Apply rate limiting and resource quotas at the identity level to prevent resource exhaustion from excessive tool calls.

Apply guardrails with identity context for persona-based content filtering. Configure your orchestration and agent layers to require identity invocation and creation for each scoped task rather than using default settings.

### Network security
<a name="network-security.4b757ce2-e8c9-539d-adc9-e9db0d3f43b0"></a>

Use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) to establish private connectivity to Amazon Bedrock AgentCore services. Create VPC endpoints for AgentCore Gateway and AgentCore Runtime to help ensure tool integration occurs through private network paths without internet exposure.

Deploy AI applications and AWS Lambda function tools within private subnets using restrictive security groups. Configure security group rules to allow only necessary communication between AgentCore Gateway and registered tools. Use AgentCore Gateway native VPC support for secure, isolated tool access.

Configure VPC endpoint policies to restrict service access to authorized AI applications only. Implement network-level rate limiting and traffic controls to prevent resource exhaustion. Use [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) to inspect traffic between AI applications and external tools for malicious patterns.

### Logging and monitoring
<a name="logging-and-monitoring.8fe72dac-0297-55c4-a3f2-68bbef89a380"></a>

Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to log tool invocation activities with user context attribution. Configure organization trails to capture cross-account tool access and maintain comprehensive audit trails. Forward all logs to the [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) for centralized security analysis.

Configure [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor tool executions and detect anomalous behavior. Create metrics for tool invocation rates, execution duration, failure patterns, and resource consumption across different integration types. Set [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to alert when metrics deviate from established baselines.

Implement [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) for MCP servers integrated with AgentCore Gateway. Monitor agent behavior, multi-agent workflows, and tool chain executions. Use trace data to identify security issues, performance bottlenecks, and unusual access patterns.

For operating system (OS) tools, use [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to log session activity to Amazon CloudWatch Logs or Amazon S3. Deploy [CloudWatch agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) to collect OS-level metrics and logs. Use [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) to maintain history of commands and outputs for audit purposes.

## Recommended AWS services
<a name="customization-services"></a>

This section reviews the AWS services that are recommended to build this capability securely.

### Amazon Bedrock AgentCore Runtime
<a name="9999999999999999braclong--runtime.6e9d7722-2281-58bd-93f9-875ad085f5c1"></a>

[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides secure, serverless hosting environments for AI agents with complete session isolation using dedicated microVMs. Each user session runs with isolated CPU, memory, and file system resources, ensuring separation between users regardless of tool type.

Configure customer managed KMS keys for enhanced encryption control over session data. AgentCore Runtime automatically terminates sessions and sanitizes memory after completion. The service supports both real-time interactions and long-running workloads up to 8 hours while maintaining security isolation throughout execution.

### Amazon Bedrock AgentCore Gateway
<a name="9999999999999999braclong--gateway.b32c6883-09cd-56af-ae28-092b1509d76c"></a>

[AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides centralized tool discovery and invocation using the Model Context Protocol (MCP). It supports multiple tool types including AWS Lambda functions, OpenAPI specifications, Smithy models, and MCP servers through a standardized interface.

Configure OAuth authorizers for gateway access and [manage authentication credentials](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html) securely with AgentCore Identity. Create VPC endpoints for private connectivity and apply endpoint policies to restrict access to authorized AI applications. The gateway enforces mandatory TLS 1.2\+ encryption for all communications by default.

Register tools explicitly through the gateway console or API. Configure tool-specific access controls, rate limits, and timeout values. Monitor tool usage through integrated CloudWatch metrics and CloudTrail logging.

### Amazon Bedrock AgentCore Identity
<a name="9999999999999999braclong--identity.77086bc9-ce45-50c5-b4c4-ba940980a132"></a>

[AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) serves as a secure credential broker supporting multiple authentication methods. These methods include AWS Signature Version 4 (SigV4) signing for native AWS services and OAuth 2.0 with JWT bearer tokens for external APIs. AgentCore Identity maintains a protected [token vault](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html#secure-credential-storage) using AWS KMS encryption for credential storage.

Configure integration with enterprise identity providers including [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), Okta, and Microsoft Entra ID. AgentCore Identity ensures complete separation between ingress authentication (verifying user identity) and egress authorization (accessing tools), preventing customer credentials from being forwarded to target services.

### AWS Lambda
<a name="9999999999999999lamlong-.768f995d-a9a8-556a-afc0-f0dca5c47a55"></a>

[Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions serve as custom tools for AI applications, providing serverless compute for business logic execution. Create AWS Identity and Access Management (IAM) execution roles with permissions scoped to invoke only registered tools and access required AWS services.

Configure Lambda functions within virtual private clouds (VPCs) for network isolation and apply resource-based policies to control which principals can invoke functions. Use environment variable encryption with customer managed KMS keys for sensitive configuration data. Set appropriate timeout values and memory limits to prevent resource exhaustion.

### AWS Secrets Manager
<a name="9999999999999999asmlong-.158a7e65-4e5d-5d6c-820c-c9511e7e1bc6"></a>

[Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) provides secure storage and automatic rotation of authentication credentials for external tool access. Store API keys, OAuth tokens, and database credentials with encryption using customer managed KMS keys.

Configure automatic credential rotation where supported by external services. Use fine-grained IAM policies to control which AI applications can retrieve specific credentials. Enable CloudTrail logging for all secret access operations to maintain audit trails.

### Amazon Bedrock Guardrails
<a name="9999999999999999br--guardrails.c870959a-fb37-538e-836e-580355e88e63"></a>

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) enables content filtering and validation for tool inputs and outputs. Configure content filters to block harmful content across multiple categories: hate, insults, sexual, violence, misconduct, and prompt attacks. Set filter strength for each category based on your risk tolerance.

Define restricted topics to prevent AI applications from discussing sensitive subjects or internal systems. Create custom word filters tailored to your organization's sensitive terminology. Configure custom response messages that users see when content is blocked.

Apply guardrails consistently across all tool integration patterns by invoking them through the `InvokeModel` API with the `guardrailConfig` parameter. For AgentCore Gateway integrations, configure guardrails directly within gateway settings to filter both tool inputs and outputs before execution.

Use guardrail metrics in CloudWatch to monitor filtering effectiveness and identify potential security threats. Create alarms when guardrail activation rates exceed expected thresholds, which may indicate attack attempts or policy violations.
