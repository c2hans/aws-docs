---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/bedrock-integration.html
---

# Integrating a traditional cloud workload with Amazon Bedrock

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This example connects an existing business application to [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) across two production accounts: the **Application account** and the **AI inference account**. These are the accounts in the Production OU in [Account and trust boundaries](https://dp8l2mfblnx2f.cloudfront.net/architecture/). Training and customization remain in a separate training account within the production security boundary.

## The account interaction
<a name="the-account-interaction"></a>

The Application account runs the frontend and backend. Its backend assumes an approved invocation role in the AI inference account, then calls Bedrock using that role's temporary credentials. An [Amazon VPC endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) provides private connectivity to the service, and [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) role trust and permissions authorize the cross-account request. The endpoint controls the network path, and the IAM role controls authorization. Configure each control separately.

The [Bedrock integration diagram](https://dp8l2mfblnx2f.cloudfront.net/images/bedrock-integration-accounts.png) shows the application backend, private service endpoint, and invocation role across the Application and AI inference accounts. Choose the components your application uses. A simple model call does not require a knowledge base, tool gateway, or agent runtime.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference - cross account AI application integration](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/37d6317e-f8d9-47cd-adc8-6ee8e6837d2d.png)

***Fig 7:*** ***AWS SRA of AI Security AWS OU and account structure with AWS service reference - cross account AI application integration***

This guidance follows the Bedrock path. For a workload using an [Amazon SageMaker AI endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html), follow the [SageMaker AI inference guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-sagemaker-ai-protect-hosted-endpoints) and use that service's invocation and network configuration.

### Application account
<a name="integration-app-account"></a>

The Application account hosts the web frontend, application backend, and application data stores. The application team manages user sessions and decides which requests may reach Bedrock. Apply the account's [shared security controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) to the application's use of Bedrock.

#### Identity propagation and access control¶
<a name="identity-propagation-and-access-control"></a>

The backend uses an IAM role to call Bedrock in the AI inference account. Grant the application role `sts:AssumeRole` on the invocation role, and configure the invocation role's trust policy to trust that application role. Grant the invocation role only the Bedrock actions and model resources the application needs. The backend signs requests with the assumed role's temporary credentials. See [cross-account role access](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) for the role configuration.

The role authorizes the backend's use of AWS services. The application must also enforce each user's data permissions. For retrieval-augmented generation (RAG) with [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), apply the user's permitted document scope in the backend before calling the knowledge base.

Agents that call tools on behalf of users need the same connection between the authenticated user and downstream permissions. [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) manages identities and credentials for these calls. Keep the incoming user's authentication separate from the credentials used to access each tool, and bind user-delegated credentials to a verified user identifier. Verify that the target data source or API enforces the user's permitted operations and data scope. Follow the [tool access guidance](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/#preserve-user-authority-across-tool-calls) for this authorization path.

#### Restrict approved models and Regions¶
<a name="restrict-approved-models-and-regions"></a>

Use the [Bedrock model-selection service control policy (SCP) example](https://aws.amazon.com/blogs/security/implementing-least-privilege-access-for-amazon-bedrock/) to deny invocation of unapproved models. Replace its illustrative model ARNs with the approved resources and cover each API the application can call. For inference profiles, include the profile and model resources required by the [geographic and global profile configuration](https://dp8l2mfblnx2f.cloudfront.net/architecture/#review-cross-region-inference-permissions).

Apply the [Region-deny SCP example](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-condition) using the organization's approved Regions. Preserve required global-service exceptions. For cross-Region inference, a source-Region allowance alone is insufficient.

Test an approved model call, an unapproved model, and a call from a disallowed source Region. Expect the approved call to succeed and the other calls to fail with an access denied error. Test each approved inference profile separately, including its destination permissions.

#### Enforce retrieval scope in the backend¶
<a name="enforce-retrieval-scope-in-the-backend"></a>

The knowledge base `filter`[ parameter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.html) is optional. A caller with retrieval permission can omit it. Grant retrieval permission only to the trusted backend when users require different document scopes, and prevent direct calls that bypass its authorization.

For a knowledge base partitioned by tenant, the backend can construct this part of a `Retrieve` request from the verified session. Replace the example value with the authorized tenant identifier; do not take it from user input or a model response.

```
{
  "retrievalConfiguration": {
    "vectorSearchConfiguration": {
      "filter": {
        "equals": {
          "key": "tenant_id",
          "value": "tenant-from-verified-session"
        }
      }
    }
  }
}
```

Protect the document metadata during ingestion. Reject a request with missing or unauthorized tenant context before calling Bedrock. Test that changing a client-supplied tenant value cannot change the backend's filter. If permissions differ within a tenant, apply those document entitlements too; a tenant filter alone is insufficient.

#### Application security¶
<a name="application-security"></a>

Requests to the web application can trigger billable model calls. Protect the web entry point with [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works-resources.html) rules for common exploits, including SQL injection and cross-site scripting. Add a rate-based rule to limit excessive requests. Combine these request controls with authentication and IAM authorization to reduce unauthorized use and unexpected inference costs.

#### Prompt injection protection¶
<a name="prompt-injection-protection"></a>

Prompt injection can use natural-language instructions that web exploit rules do not detect. Assess prompt injection defenses separately from AWS WAF coverage.

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) can filter prompt attacks and harmful content. Enable prompt attack detection, select filter strengths based on the application's risks, and deploy a versioned guardrail to production.

Use an [organization-enforced guardrail](https://dp8l2mfblnx2f.cloudfront.net/architecture/#set-organization-wide-controls) for the shared baseline. For an additional application guardrail, the `bedrock:GuardrailIdentifier` condition key can reject requests that omit or change the required guardrail; it does not attach one. Follow the documented API compatibility and version-qualified ARN examples for [requiring a specific guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions-id.html).

|
|
| **Invocation path** | **Configure and test** |
| --- |--- |
| `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, `ConverseStream` | Supply the required guardrail identifier and version. Test that requests that omit or change them fail with an access denied error. |
| Chat Completions on Bedrock Runtime | Supply the guardrail identifier and version through the [documented request headers](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions.html). Test enforcement for this API separately. |
| `RetrieveAndGenerate` | Set `generationConfiguration.guardrailConfiguration` for the knowledge base request. Guardrails do not evaluate retrieved references. |
| `InvokeAgent` | [Associate the guardrail with the agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html) and test the deployed agent version. |
| `InvokeFlow` | Configure guardrails on [supported prompt and knowledge base nodes](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-guardrails.html). Knowledge base nodes require response generation. |

The IAM condition guidance explicitly covers `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, and `ConverseStream`. Higher-level operations can make internal model calls without guardrail parameters and fail under the same deny policy, even when a guardrail is configured for the operation. Test each path with its execution role and follow the documented limitations before sharing roles across these paths.

Construct prompt tagging in the trusted backend. The condition does not prevent callers from using guardrail input tags to exclude prompt content from evaluation. Include attempts to alter that tagging in the application tests.

Review [guardrail coverage](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-configure-and-test-inference-guardrails) when changing the invocation path.

Validate inputs in the application before passing them to a model or agent. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions can perform this preprocessing. Test the validation and guardrail configuration with adversarial inputs, including attempts to bypass filters or manipulate model behavior.

#### Data protection¶
<a name="data-protection"></a>

The application can retain sensitive information in prompts, conversation logs, and cached responses. Classify this data and define what the application may send to a model or store. Apply the [shared encryption and data controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls) to application data stores, conversation logs, and caches. Redact information that the application is not permitted to send or retain before further processing or storage.

#### Network security¶
<a name="network-security"></a>

The backend can reach Bedrock over a private network path from its virtual private cloud (VPC). Place application tiers that do not need internet access in private subnets. Create an interface endpoint for `bedrock-runtime` using [AWS PrivateLink](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html). Apply the [shared network controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls) to the application tiers.

**Restrict the endpoint.** The [Bedrock endpoint-policy example under Model adaptation](https://aws.amazon.com/blogs/security/implementing-least-privilege-access-for-amazon-bedrock/) restricts the principal and model resources. Substitute the assumed invocation role's account and role ARN, approved model ARNs, and required inference actions. Include the required profile resources for cross-Region inference. Test that the intended role can invoke the approved model through the endpoint and that another role or model is denied.

**Require the private path.** An endpoint policy does not restrict calls that bypass it. Adapt the [explicit-deny condition example](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html#example-bucket-policies-restrict-accesss-vpc-endpoint) for the invocation role: deny the selected Bedrock Runtime actions and resources when `aws:SourceVpce` does not equal the approved endpoint ID. That example is an S3 resource policy; replace its actions and resources and omit `Principal` when using a role policy. `aws:SourceVpce` is absent outside endpoint requests. Apply the documented service-principal and forward access session exceptions required by the workload. Test the approved endpoint, the public endpoint, and each required service integration; only the approved paths should succeed.

#### Logging and monitoring¶
<a name="logging-and-monitoring"></a>

The response team needs records of who invoked the model and, where permitted, the content of those invocations. [AWS CloudTrail](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html) records Bedrock API activity and available identity, request, and response metadata. Forward these logs to the Log Archive account for centralized analysis.

Model invocation logging captures prompts and completions separately from CloudTrail. Configure it with `PutModelInvocationLoggingConfiguration`, selecting destinations in the invocation account and Region and the content types required for investigation.

|
|
| **Logging choice** | **Configuration** |
| --- |--- |
| [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) destination | `cloudWatchConfig` with `logGroupName` and `roleArn` |
| [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) destination, alone or alongside CloudWatch Logs | `s3Config` with `bucketName` |
| Content types to retain | Enable the required options: `textDataDeliveryEnabled`, `imageDataDeliveryEnabled`, `embeddingDataDeliveryEnabled`, `videoDataDeliveryEnabled`, and `audioDataDeliveryEnabled` |

For example, this request enables text logging to an existing S3 bucket. Replace the bucket name and configure the [destination permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) before applying it. The setting applies across the account and Region.

```
{
  "loggingConfig": {
    "s3Config": {
      "bucketName": "DOC-EXAMPLE-BUCKET",
      "keyPrefix": "bedrock/"
    },
    "textDataDeliveryEnabled": true,
    "imageDataDeliveryEnabled": false,
    "embeddingDataDeliveryEnabled": false,
    "videoDataDeliveryEnabled": false,
    "audioDataDeliveryEnabled": false
  }
}
```

Invocation logs can contain sensitive user content. Encrypt the destination with a customer managed key and apply the access and retention controls defined for that data.

Use [Amazon CloudWatch](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html) to monitor invocation rates, response latency, errors, and token usage. Set alarms for changes from expected usage. Review Bedrock Guardrails metrics alongside these alarms to identify increases in guardrail interventions.

Enable [Amazon GuardDuty AI Protection](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html) in the AI inference account. It analyzes CloudTrail data events for Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker AI, together with management events. GuardDuty collects the data events through its own service-linked channel; you do not need to configure a trail for this analysis. Configure your own CloudTrail coverage separately for audit and investigation requirements.

The security team can aggregate logs in [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) or an existing security information and event management (SIEM) solution. Correlate model calls with application and network activity to investigate unexpected traffic volumes or destinations.

For analysis across accounts and Regions, CloudWatch can normalize selected logs with its `parseToOCSF`[ transformation](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParseToOCSF.html). Supported sources include CloudTrail, [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [Amazon Route 53 Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html), [Amazon EKS audit logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), and AWS WAF logs. Configure the [Amazon S3 Tables integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/s3-tables-integration.html) and associate the required log sources to make newly ingested logs available in managed Apache Iceberg tables. The integration does not require every source to use Open Cybersecurity Schema Framework (OCSF). Bedrock model invocation logs are not a supported `parseToOCSF` source. Retain them as a separate stream and correlate records by request identifier.

### AI inference account
<a name="ai-inference-account"></a>

The AI inference account owns production model access and the retrieval or agent resources assigned to this workload. Use separate roles for model invocation, retrieval, and tool execution.

|
|
| **Component in this account** | **Apply this guidance** |
| --- |--- |
| Bedrock model inference | [Bedrock inference controls](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-protect-managed-model-access) |
| Knowledge bases and RAG | [Data and retrieval](https://dp8l2mfblnx2f.cloudfront.net/connects/data-and-retrieval/) |
| Read-only tools | [Tool access and user authority](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) |
| Agents | [Runtime isolation](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#isolate-agent-and-tool-execution); add [action controls](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#validate-actions-outside-the-model) when tools can change systems |
| User access | [Custom application identity and authorization](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#custom-applications-separate-user-sign-in-from-aws-access) |

#### Foundation model inference
<a name="foundation-model-inference"></a>

The inference account owns the approved model access and guardrail configuration. Use Amazon Bedrock Guardrails to filter harmful input and output content, select filter strengths for the application's risks, and define restricted topics. The Application account helps protect the web entry point and invokes these approved resources through its assumed role.

Apply the [Bedrock inference controls](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-protect-managed-model-access) to this configuration.

#### Knowledge bases and RAG
<a name="knowledge-bases-and-rag"></a>

A knowledge base adds a path from the user's request to organizational documents. Protect the source data and index with encryption at rest, using customer managed [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) keys where supported, and use TLS for data in transit. Configure ingestion encryption and retrieval metadata filters for the user's authorized document scope.

Validate documents before ingestion, including malware checks and required redaction. Optional components shown in the diagram include [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html), and [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html). The [data and retrieval guidance](https://dp8l2mfblnx2f.cloudfront.net/connects/data-and-retrieval/) covers source permissions, ingestion, and retrieval checks.

#### Tool integration
<a name="tool-integration"></a>

Tools connect the application to data sources and business systems. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) centralizes tool discovery and invocation through the Model Context Protocol (MCP). Configure IAM or JSON Web Token (JWT) inbound authorization as described in [Set up inbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html), and use AgentCore Identity to manage the credentials used for downstream access.

For private application access, create [interface VPC endpoints for Gateway and Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc.html) and restrict their security groups. Configure Gateway-to-target connectivity separately. [Connect a Lambda function to your VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) when it needs private resources. This controls the function's network access; private access to the [Lambda invocation API](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html) requires its own interface endpoint.

Identity-level rate limits and quotas help control excessive tool calls. [AgentCore Gateway rate limits](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-rate-limits.html) are fail-open by default: the gateway allows requests if the rate limit service is unavailable or a dimension cannot be resolved. Keep authorization that denies by default independent of these rate limits.

Apply [agent execution controls](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/) when an agent selects tools. Use [read-only tool access](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) for information requests and add approval and recovery controls when tools can change systems.

#### Authorize a specific Gateway tool
<a name="authorize-a-specific-gateway-tool"></a>

Use [Policy in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to authorize tool calls. Attach a policy engine to the gateway in `ENFORCE` mode and set required policies to `ACTIVE`. For a JWT-authorized gateway, this Cedar example permits one tool when the verified token contains the required role claim. Adapt the action name and gateway Amazon Resource Name (ARN) to the deployed target and use a claim controlled by the trusted identity provider.

```
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI___get_contract",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance-gw-a1b2c3d4e5"
)
when {
  principal.hasTag("role") &&
  principal.getTag("role") == "claims-reader"
};
```

The [principal policy examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/example-policies-principal.html) describe how JWT claims become principal tags. Review the complete policy set: another permit can grant additional access. Test a permitted caller, a missing claim, a different role, and a different tool. The tool must still enforce which contracts that caller may read. This policy does not replace downstream data authorization.

#### Agent execution and permissions
<a name="agent-execution-and-permissions"></a>

Use the [central discovery catalog](https://dp8l2mfblnx2f.cloudfront.net/architecture/#catalog-approved-agents-and-tools) to review agents and tools before adoption. Apply the [agent controls](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/) to the components you deploy, including optional [Amazon Bedrock AgentCore harness](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html), [Amazon Bedrock AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html), [Amazon Bedrock AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html), [Amazon Bedrock AgentCore payments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html), [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluators.html), and [Amazon Bedrock AgentCore optimization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/optimization.html).

[Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-how-it-works.html) isolates sessions in dedicated microVMs or, with the Instances compute type, Amazon EC2 instances. Within a session, agent code can use its assigned permissions. Restrict credentials and network destinations as described in [agent and tool execution controls](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/#isolate-agent-and-tool-execution).

Define authentication and authorization at each step: the user invokes the agent, the agent calls a tool, and the tool accesses a downstream system. Give each execution role the minimum permissions for its task. Enable [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to trace agent activity across these steps.

Stored agent data also needs protection. Configure customer managed KMS keys for [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-create-a-memory-store.html), Identity token vaults, and Gateway configuration where supported. Review the encryption settings and key requirements for [Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-create-a-memory-store.html), [Identity token vaults](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-encryption.html), and [Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-encryption.html).

Apply [read-only tool controls](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) for retrieval. Add [action authorization and recovery](https://dp8l2mfblnx2f.cloudfront.net/acts/agents/) when the agent can change records, run code, or affect devices, including when those operations require human approval.

#### End-user AI applications
<a name="end-user-ai-applications"></a>

User sign-in and session management remain part of the application design. Federate internal users with the corporate identity provider, using [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) where appropriate for the application. For external users, use [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) or another identity provider that meets the application's requirements. Isolate each user's sessions and results, and monitor for unusual activity.

The [custom application access guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#custom-applications-separate-user-sign-in-from-aws-access) describes how user authentication relates to backend authorization. Use the [four-step reading path](https://dp8l2mfblnx2f.cloudfront.net/#how-to-use-this-guide) to review the model, retrieval, and action controls for the components in this application.

The diagram's other optional components are [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html) for the application entry point, and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html), and [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) for the shared security and evidence architecture. Follow the [account controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/) when adopting them.

### Optional customization in the training account
<a name="optional-customization-in-the-training-account"></a>

If this application uses a customized model, run its governed customization workflow in the [training environment](https://dp8l2mfblnx2f.cloudfront.net/architecture/#training-account-and-model-promotion). Protect the datasets and artifacts, evaluate the resulting model, and promote it through an approved deployment path. Use [Bedrock customization guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/model-customization/#amazon-bedrock-isolate-managed-customization-jobs) for the job and [inference controls](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/) for production serving.
