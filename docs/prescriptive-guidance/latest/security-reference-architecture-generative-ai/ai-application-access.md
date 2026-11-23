---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/ai-application-access.html
---

# AI application access

User access has two parts: authenticating the person using the application and authorizing the data and actions available to them. The configuration depends on the application they sign in to. [Kiro](https://kiro.dev/docs/enterprise/identity-provider/) and [Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/identity.html) provide product-specific sign-in and administration options. For a **custom AI application**, your team chooses the identity provider and implements session and access controls.

|
|
| **Application** | **Sign-in path** | **What to configure** |
| --- |--- |--- |
| Kiro enterprise deployment | Connect an enterprise identity provider to Kiro, or integrate it through [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) | Approved users, enterprise entitlements, and supported model, file, and tool controls |
| Amazon Quick | Choose a Quick authentication method available for the subscription and Region | User and group access, application entitlements, dataset permissions, and sharing<br />Use permissions to restrict AI capabilities that read content, take actions, and run automated workflows. |
| Custom web or mobile application | Use your application's identity provider; [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) are one option | Sign-in, sessions, per-user authorization, and a separate backend [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) role for AWS access |

Managed product settings differ by client and subscription, so confirm where each product enforces each control. The guidance applies to both [model and knowledge base applications](https://dp8l2mfblnx2f.cloudfront.net/answers/) and [agentic AI](https://dp8l2mfblnx2f.cloudfront.net/acts/). Review the official Kiro [privacy and security](https://kiro.dev/docs/privacy-and-security/) documentation along with the Amazon Quick [security features](https://aws.amazon.com/quick/security/?trk=0ea79374-057c-4897-84f0-5fe792905a8f&sc_channel=ps) for additional controls.

The following diagram expands the [AI account architecture](https://dp8l2mfblnx2f.cloudfront.net/architecture/#place-ai-systems-within-the-account-structure) for a custom agentic application. It shows three authorization boundaries:

1. **User to agent:** The application authenticates the user, authorizes the requested task, and invokes the agent through its backend.

1. **Agent to tool:** The agent accesses approved tools through a gateway that evaluates the caller, requested tool, and parameters before execution.

1. **Tool to business resource:** The tool checks the user's authority and uses its own execution role to access the required records or perform the permitted action.

The example uses separate Application and AI inference accounts. The backend assumes an authorized role in the AI inference account and uses IAM authentication to invoke the agent. Consider [combining the accounts](https://dp8l2mfblnx2f.cloudfront.net/architecture/#application-and-inference-accounts) when their ownership, risk, and control requirements align. Managed products use their own sign-in and administration settings.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference - AI application access](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/f4bd67c4-6b08-477c-8b61-21aefeb9eb5f.png)

***Fig 5:*** ***AWS SRA of AI Security AWS OU and account structure with AWS service reference - AI application access***

## Security considerations
<a name="security-considerations"></a>
+ A valid sign-in must not grant access to another user's conversations, documents, or tools.
+ Generated code can introduce vulnerabilities in authentication, retrieval, and action handlers.
+ Integration credentials and retained prompts can expose data beyond the application's intended use.
+ Excessive requests and repeated tasks can exhaust capacity and incur model and tool charges.

## Infrastructure security
<a name="infrastructure-security"></a>

### Custom applications: protect the application boundary
<a name="custom-applications-protect-the-application-boundary"></a>

In a custom application, your team controls the frontend, backend, and connections to data stores. Separate that compute from unrelated workloads and restrict the network paths between components. [Amazon VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) control permitted traffic to associated resources. Select private service endpoints where the application's integration permits them. For a managed application, [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) controls the documented service connection; it does not place the product's user interface in your VPC.

[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works-resources.html) filters web requests at supported application entry points. Apply AWS WAF managed rule groups that address your application's risks, add rate-based rules, and check that alternate access paths cannot bypass required frontend controls. Confirm the resource is eligible before planning AWS WAF protection. [AWS Network Security Manager WAF policies](https://docs.aws.amazon.com/network-security-manager/latest/devguide/managing-waf-quick-create.html) cover eligible [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) REST API stages, and [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) distributions. Check the documented exclusions before including an entry point in the [central baseline](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls). Enforce per-user request limits and [cumulative task budgets](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#isolate-agent-and-tool-execution) in the application, alongside authentication, authorization, and model content validation.

Route outbound traffic requiring inspection through [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html). Review allowed destinations when adding an external model or integration. Apply the [DNS filtering baseline](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#filter-outbound-dns-requests) to application VPCs. For custom code and container images, use [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) within its supported scanning scope, and remediate findings through the release pipeline.

### Custom applications: govern application hosting
<a name="custom-applications-govern-application-hosting"></a>

[Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html) provides session isolation for hosted agents. Pair that isolation with a dedicated execution role and explicit application rules for assigning sessions to users. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) can run application workers; bound concurrency and scope each worker's role to its task. Use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to patch supported managed nodes you operate, with tested maintenance and recovery procedures.

## Identity and data security
<a name="identity-and-data-security"></a>

### Kiro: configure enterprise identity and development access
<a name="kiro-configure-enterprise-identity-and-development-access"></a>

[Kiro enterprise identity configuration](https://kiro.dev/docs/enterprise/identity-provider/) supports connecting an external identity provider directly or integrating through IAM Identity Center. Choose the documented path for your enterprise deployment and manage user provisioning and removal there. Apply the [Kiro governance controls](https://kiro.dev/docs/enterprise/governance/) for that deployment. Configure the supported model and tool restrictions and deploy managed permission policies for development machines. Review connected tools separately from a user's ability to sign in.

|
|
| **Product control** | **Where to configure it** | **Scope to verify** |
| --- |--- |--- |
| Kiro models and MCP servers | Kiro console **Settings > Shared settings**; configure **MCP Registry URL** with MCP enabled | [Model Context Protocol (MCP) governance](https://kiro.dev/docs/enterprise/governance/mcp/) applies to IAM Identity Center and API-key users, not Builder ID or social sign-in. A local administrator can bypass client enforcement. |
| Kiro file, shell, and web permissions | Deploy OS-protected `managed-settings.json` files to development machines | [Managed permission policies](https://kiro.dev/docs/enterprise/governance/permissions/) impose deny or ask rules on integrated development environment (IDE) and command line interface (CLI) clients. Test the deployed client and prevent users from altering the managed file. |
| Kiro Web | Review the organization's profile and [Web identity configuration](https://kiro.dev/docs/web/identity-center/) | Web does not apply the shared MCP, registry URL, customer managed key, or enterprise web-tool settings. Verify its supported controls separately. |

Document acceptable use requirements for Kiro and other managed AI products, including approved data, permitted uses, and when users must review generated output. Configure the available product controls to enforce these requirements. Retain the policy and its owner in the [implementation record](https://dp8l2mfblnx2f.cloudfront.net/conclusion/#implementation-record).

### Amazon Quick: configure product and dataset permissions
<a name="amazon-quick-configure-product-and-dataset-permissions"></a>

The available [Quick authentication methods](https://docs.aws.amazon.com/quick/latest/userguide/identity.html) depend on the subscription and Region. IAM Identity Center authentication requires [Quick Enterprise edition](https://docs.aws.amazon.com/quick/latest/userguide/setting-up-sso.html). You choose the authentication method during account setup because you can't change it after you create the Quick account.

After sign-in, configure the user's product entitlements, sharing permissions, and access to data. Use [row-level security](https://docs.aws.amazon.com/quick/latest/userguide/restrict-access-to-a-data-set-using-row-level-security.html) where required for datasets. Test with users who have different data entitlements; successful authentication alone must not expose every dataset.

|
|
| **Product control** | **Where to configure it** | **Scope to verify** |
| --- |--- |--- |
| Quick feature access | Enterprise administration: custom permissions at account, role, or user level | [Custom permissions](https://docs.aws.amazon.com/quick/latest/userguide/sec-agentic-security.html) restrict existing capabilities. User settings take precedence over role settings, then account settings. Use AI deny-by-default when new AI capabilities require review before use. |
| Quick blocked words | **Manage Quick > Customization > Chat agent customization > Guardrails and safety controls** | [Blocked-word guardrails](https://docs.aws.amazon.com/quick/latest/userguide/guardrails.html) perform exact matching for web chat agents and flows. They do not provide semantic detection of equivalent phrases. |
| Quick AI capabilities | For knowledge bases with document-level access control lists (ACLs), use custom permissions to restrict the AI capabilities available to each role. Use account-wide and organization-wide controls to set defaults. | Verify account-level and organization-level [AI and agent capability access](https://docs.aws.amazon.com/quick/latest/userguide/sec-agentic-security.html) for each role. |

### Custom applications: separate user sign-in from AWS access
<a name="custom-applications-separate-user-sign-in-from-aws-access"></a>

[Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) provide a user directory and sign-in for web and mobile applications, including identity provider federation. Configure multi-factor authentication (MFA) and prompt access removal in your chosen identity system. Your application must validate tokens and authorize access to conversations, documents, and actions.

Configure [Runtime inbound authentication](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html) with IAM or JSON Web Token (JWT) for the selected caller path.

Bind each [Runtime session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html) to the authenticated user and reject attempts to resume another user's session. Apply equivalent authorization to retained conversations and [AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-gateway-fgac.html) actors and namespaces. Session and memory identifiers do not establish ownership.

### Custom applications: preserve user authority through tools
<a name="custom-applications-preserve-user-authority-through-tools"></a>

Configure [AgentCore Gateway inbound authentication](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html) for the agent calling the gateway, and select [outbound credentials](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html) supported by each target. These credentials can permit operations the requesting user can't perform. Carry verified user and task context to the authorization decision, and don't accept an identity supplied by the model as evidence of permission.

[Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) can broker user-delegated OAuth credentials or machine credentials. Use delegated access when the tool must act on behalf of a user, and bind the [OAuth consent session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/oauth2-authorization-url-session-binding.html) to that user. Keep tokens out of prompts, tool results, and logs.

A Lambda function that serves as a tool uses its own [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) for downstream AWS access. Scope this role to the required resources and actions, and enforce per-user permissions before reading or changing a business record. Use [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) when these application permissions need centralized policy evaluation. The tool must enforce the returned decision. Apply the same [identity checks](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/#preserve-user-authority-across-tool-calls) to delegated calls, retries, and cached results.

### Apply retention and credential controls to the product in use
<a name="apply-retention-and-credential-controls-to-the-product-in-use"></a>

Classify user inputs, generated code, conversation history, and exports. Apply the [shared data controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls) to each retained copy, including diagnostic traces. Confirm which product stores accept customer managed keys, and configure retention, deletion, and reader permissions separately. Verify that credential rotation reaches running integrations and that removed users lose access to retained sessions.

## AI application security
<a name="ai-application-security"></a>

### Custom applications: enforce tool policies outside the agent
<a name="custom-applications-enforce-tool-policies-outside-the-agent"></a>

For MCP tool calls through AgentCore Gateway, use [Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to evaluate permissions before tool execution. Attach the policy engine in `ENFORCE` mode and set required policies to `ACTIVE`. Define permits for approved callers, tools, and parameter limits. The policy engine denies requests without a matching permit, and active forbid rules override permits. Test the policy engine in `LOG_ONLY` mode in a preproduction environment; this mode records decisions without blocking calls.

For [MCP requests](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/use-gateway-with-policy.html), policy evaluation covers tools, not prompts or resources. Protect those interfaces separately, and prevent direct target invocation from bypassing required gateway controls. Continue to authorize business records inside each tool. When policies depend on user identity, supply [verified caller context](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/#preserve-user-authority-across-tool-calls); the agent's machine identity alone does not establish the requesting user's permissions.

Require [independent approval](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#validate-actions-outside-the-model) for consequential actions and define [containment and recovery](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#design-for-containment-and-recovery). Test unauthorized tools, changed parameters, missing identity, cross-user sessions, and replayed approvals before release. Record the user, agent and tool versions, policy decision, and downstream result so an investigator can reconstruct the action.

### Secure coding agents and their tools
<a name="secure-coding-agents-and-their-tools"></a>

Coding agents such as [Claude Code and Codex](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/plugins.html) and [Kiro](https://kiro.dev/docs/enterprise/governance/) use project context and connected tools to complete development tasks. Restrict access to approved repositories, files, and data. Review the source, permissions, and updates of skills, plugins, and MCP servers before enabling them. Treat repository content and tool responses as untrusted input, and test attempts to read excluded files or secrets. Configure the controls available for each client; the [Kiro settings](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#kiro-configure-enterprise-identity-and-development-access) provide one example.

The [Agent Toolkit for AWS](https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/) provides agent skills and integrations with the AWS MCP Server. When using the [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html), select credentials for a task-scoped IAM role; downstream AWS services authorize requests against the role's permissions. Require [independent approval](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#validate-actions-outside-the-model) for consequential changes, and test that unapproved actions are blocked. Include generated changes in the [code review and testing process](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#review-custom-application-code-with-aws-continuum).

### Review custom application code with AWS Continuum
<a name="review-custom-application-code-with-aws-continuum"></a>

Include custom application code, including AI-generated code, in the [shared vulnerability management process](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/application.html#app-inspector).

[AWS Continuum for code vulnerabilities](https://docs.aws.amazon.com/continuum/latest/userguide/code-vulnerabilities.html) discovers, validates, and prioritizes code vulnerabilities and recommends remediation. Use it to review the application code that implements security boundaries across the three AI use cases:
+ **AI that answers:** Request handlers, session management, and code that invokes models or processes their responses. For [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) or self-hosted models, include model-serving code your team maintains.
+ **AI that connects:** Document ingestion, retrieval filters, and caches. Include the code that carries user identity to the data source and restricts which documents or records can be returned.
+ **AI that acts:** Agent orchestration, custom MCP servers, tool adapters, action executors, and approval callbacks. Include the code that checks permissions, constrains tool parameters, and handles retries or recovery, including for read-only tools.

These are code review targets. Continue to evaluate model behavior, retrieved content, and multi-step agent actions through the tests described in their respective sections.

### Supply context and verify remediation
<a name="supply-context-and-verify-remediation"></a>

Connect approved code through [GitHub or GitLab](https://docs.aws.amazon.com/continuum/latest/userguide/cv-getting-started.html) or [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and supply [infrastructure and business context](https://docs.aws.amazon.com/continuum/latest/userguide/cv-adding-context.html), including data, authorization rules, and deployment. Associate an [AWS Continuum Collector](https://docs.aws.amazon.com/continuum/latest/userguide/cv-adding-context.html) in the relevant account and Region. Record missing context when assessing reachability and impact.

Assign a remediation owner to review [issues and evidence](https://docs.aws.amazon.com/continuum/latest/userguide/cv-viewing-issues.html); an executable proof or unit test might be unavailable. Review [GitHub pull requests or S3 patch files](https://docs.aws.amazon.com/continuum/latest/userguide/cv-viewing-patches.html). Test the affected security boundary and regressions before release, then rescan. Retain findings, test results, approval, and the deployed revision.

Complement this review with [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) for first-party source, third-party dependencies, and infrastructure as code. Include applicable [package and image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html), [secret detection](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/scan-git-repositories-for-sensitive-information-and-security-issues-by-using-git-secrets.html), and [running-application tests](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_automate_testing_throughout_lifecycle.html). Verify deployed retrieval filters, approvals, and model safeguards through the [workload tests](https://dp8l2mfblnx2f.cloudfront.net/conclusion/#test-the-boundaries-that-apply).

### Test access and behavior for each application
<a name="test-access-and-behavior-for-each-application"></a>

Content safeguards depend on how the application integrates the model. For custom integrations, [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) provides configurable content protections. Managed AI applications expose their own safety and administrative settings, which can differ from Amazon Bedrock Guardrails settings. Configure the controls available for the product and test adversarial prompts, unauthorized context access, and unsafe generated output. Require review before generated code or recommendations enter workflows where an error could have significant consequences.

Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) for instrumented agents and product-specific usage records for managed applications. Correlate user requests with application activity while limiting sensitive content capture.

Use [Amazon CloudWatch Omni evaluations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-agents-evaluate.html) to assess agent responses against selected quality criteria, on demand or through configured online evaluations of sampled production traces. Configure the evaluators and the input and output capture they require. Approve the content available to evaluators, and review quality scores alongside operational metrics and traces.

Centralize [telemetry collection, investigation access, and configuration history](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html). For AI investigations, correlate the user request with the model invocation, retrieved sources, tool calls, and downstream result. Record the workload version and authorization decisions needed to explain what occurred, while limiting access to captured content.

Use configuration findings and application tests together. When a model, knowledge source, tool, permission, or deployed version changes, rerun the affected access and behavior tests and update the [implementation record](https://dp8l2mfblnx2f.cloudfront.net/conclusion/#implementation-record). Quality scores alone do not verify authorization. Follow the [shared configuration baseline](https://dp8l2mfblnx2f.cloudfront.net/architecture/#keep-required-settings-enabled) for drift checks and the [agent recovery guidance](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#design-for-containment-and-recovery) for approved restoration and changes that require review.

## Design considerations
<a name="design-considerations"></a>

A reusable baseline for identity, hosting, logging, and response ownership gives application teams a starting point for new deployments. Review new data sources, tools, models, and permissions against that baseline. Adding retrieval or actions changes what the application can access or modify, so the authorization tests must cover those capabilities. Before expanding adoption, test access removal, session separation, and investigation records with realistic user journeys.
