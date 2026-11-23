---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/read-only-tool-access.html
---

# Read-only tool access

Tools connect an AI application to current information through APIs, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) functions, or Model Context Protocol (MCP) servers. For example, an account-status tool reads a customer record from another system. The tool needs permission to query that system, and the system must restrict the result to information the requesting user may read.

This page covers read-only tools. It complements [model inference](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=model-inference) and, where results come from indexed documents, [data and retrieval](https://dp8l2mfblnx2f.cloudfront.net/connects/data-and-retrieval/). The classification depends on what the tool and its downstream calls can do. A lookup can still disclose information if it sends data to an external destination. Tools that change records, send messages, run unrestricted commands, or delegate those permissions also need the [agent execution and action controls](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agent-execution-and-actions).

An agent that selects read-only tools still needs the [agent execution controls](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agent-execution-and-actions). Read-only permissions limit what a tool can change; they do not remove the risks of agent execution.

## Security considerations
<a name="security-considerations"></a>
+ A tool's service credentials can expose more data than the requesting user is authorized to read.
+ Unverified identity or tenant parameters can turn a permitted lookup into cross-user access.
+ Tool descriptions, responses, and dependencies can introduce unauthorized instructions.
+ Alternate invocation paths or newly added write permissions can bypass the intended controls.

## Infrastructure security
<a name="infrastructure-security"></a>

### Gateway and execution boundaries
<a name="gateway-and-execution-boundaries"></a>

An application invokes a tool through a gateway or another configured entry point. The tool's execution environment then uses its credentials to access the downstream system. Gateway configuration controls access to the tool interface; executor permissions limit what the tool can do after invocation.

[Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides a common discovery and invocation interface for connected tools. Register reviewed targets and restrict who can change their endpoints, schemas, and credentials. Select [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) or [JSON Web Token (JWT) inbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html) and authorize each caller's permitted tools. `NONE` permits unauthenticated access; `AUTHENTICATE_ONLY` validates identity without providing tool authorization. Where the design depends on Gateway enforcement, protect the underlying service from alternate invocation paths. For applications in [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), use [AWS PrivateLink](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc.html) endpoints for private access to AgentCore. Configure outbound connectivity to each tool target separately; private access to Gateway does not make every downstream connection private.

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) runs custom tool logic with a function execution role. Scope that role to the records and operations the tool requires, and control invocation through caller permissions and applicable function policies. Use VPC connectivity when the tool needs private resources, with restricted routes and security groups. Set timeout and concurrency limits that match the downstream system's capacity.

For self-hosted tools on [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html), or [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html), assign workload-specific identities and maintain the applicable container or host isolation. Review images, dependencies, patching responsibilities, and administrative access. Limit egress to required systems; permitted destinations still need controls on the data sent to them.

### Public API protection
<a name="public-api-protection"></a>

[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) can expose a tool's REST API, with IAM, a Lambda authorizer, or an [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) user pool authorizer controlling access. Usage-plan API keys identify clients for metering and traffic management; they do not authenticate or authorize requests. Throttles and quotas are best-effort traffic controls, so the application needs separate budget and backend limits.

Use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works-resources.html) on a supported frontend, for example an API Gateway REST API, to filter unwanted web requests. Restrict bypass routes to the backend. Web filtering does not establish permission to read a customer's record or determine whether a model-selected tool call is appropriate.

## Identity and data security
<a name="identity-and-data-security"></a>

### Preserve user authority across tool calls
<a name="preserve-user-authority-across-tool-calls"></a>

A tool's service credentials can allow access to more records than an individual user may read. The application must carry verified user and tenant identity into the authorization decision to preserve the user's restrictions. Before execution, authorize the tool, requested resource, and permitted result fields. Reject requests that lack this identity context. Apply the same checks to retries, caches, and chained tool calls. For Gateway tools, use the [Policy enforcement guidance](agent-execution-and-actions.md#authorize-downstream-actions) for read permissions as well as action permissions.

For JSON Web Token (JWT) callers, validate the issuer, audience, signature, and expiry before using identity claims. If the integration forwards context through [Gateway headers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-headers.html), add only the required headers to an allow list and verify their origin at the receiving service. A forwarded header is not proof of identity. Use [on-behalf-of token exchange](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/on-behalf-of-token-exchange.html) when the identity integration supports it. For a custom signed context, define and verify its issuer, audience, expiry, and authorized scope. Do not accept a user or tenant identity supplied by the model as authorization evidence.

For custom tools, use [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) when application permissions need centralized policy evaluation. Pass the authenticated principal, requested action, resource, and relevant context to the authorization service. The tool must enforce the returned decision before accessing the resource or returning its data.

[Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) brokers credentials for downstream integrations. Inbound authentication identifies the caller; outbound credentials let the tool access the target service. Bind user-delegated OAuth access to the verified user, and review provider scopes and revocation behavior. The application must also keep tokens out of model context, tool results, and logs.

Apply the [shared identity and credential controls](account-and-trust-boundaries.md) to each executor. Verify that running executors adopt rotated credentials and that revoking a user's access prevents subsequent reads, including through caches and retries.

## AI application security
<a name="ai-application-security"></a>

### Discovery and tool contracts
<a name="discovery-and-tool-contracts"></a>

Use the central discovery catalog to publish and review approved agents, Model Context Protocol (MCP) servers, and tools. Registry approval establishes what consumers can discover; enforce invocation permissions at the tool boundary. Reassess endpoint, schema, description, and credential changes before adopting them.

Validate model-proposed arguments against the tool contract and authorized resource scope. Reject unapproved URLs, excessive result sizes, and malformed requests. Treat descriptions and returned content as untrusted inputs that can contain prompt injection. Apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) where content inspection fits the integration, verifying which content is evaluated. Guardrails inspection does not establish tool safety, replace authorization, or guarantee inspection of every tool exchange.

Include custom tool handlers and MCP server code in the [application code review workflow](ai-application-access.md#review-custom-application-code-with-aws-continuum). Include adapters that translate tool arguments into database queries, outbound requests, or operating system commands. Test proposed fixes against cross-user access, unapproved destinations, malformed arguments, and the tool's permitted downstream operations before release.

### Evidence and operational control
<a name="evidence-and-operational-control"></a>

Correlate caller identity, tool version, authorization outcome, and result status through [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and, if you use it, [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Configure [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) to log management events and the data events for the resources your tools access, and capture application decisions as separate evidence. Use the shared configuration checks to detect changes to the approved tool configuration. Investigate anomalous access and repeated denials, and exclude sensitive arguments and credentials from routine logs.

## Design considerations
<a name="design-considerations"></a>

The tool's deployment and permissions determine the controls it needs. Test cross-user access, untrusted responses, credential revocation, and resource exhaustion from repeated calls. Operators need a way to stop access at the executor or target because removing a discovery entry leaves existing callers able to invoke it.

When a tool gains write permissions, review its executor role and permitted operations, validate the resource and parameters of each change, and add independent approval where required. Define retry, duplicate-action, and recovery behavior before enabling the new operation. Test these [action controls](agent-execution-and-actions.md#validate-actions-outside-the-model) through the complete tool path; changing a tool description does not establish the new authorization boundary.
