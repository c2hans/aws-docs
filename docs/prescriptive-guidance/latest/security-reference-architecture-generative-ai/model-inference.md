---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/model-inference.html
---

# Model Inference

An inference workload receives an application request, invokes a model, and returns a result. This page describes that flow for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html) managed model access and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html) hosted inference. It also covers the application controls common to both services and to models on compute you operate.

SageMaker AI can host models trained elsewhere. Teams using pre-trained models can follow this page without operating a training environment. [Model customization](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=model-customization) describes the additional controls for workloads that train or adapt a model.

## Security considerations
<a name="security-considerations"></a>

The inference design should address these risks:
+ An application role can invoke an unapproved model or replace a production endpoint.
+ Prompts, responses, or logs expose sensitive information to unauthorized readers.
+ Prompt injection changes model behavior, or generated output reaches a downstream system without validation.
+ An alternate API or network path bypasses required content or access controls.

## Infrastructure security
<a name="infrastructure-security"></a>

### Choose and isolate the hosting environment
<a name="choose-and-isolate-the-hosting-environment"></a>

The [AI inference account](https://dp8l2mfblnx2f.cloudfront.net/architecture/#map-account-roles-to-your-services) contains production model serving, including Bedrock model access and Amazon SageMaker AI production endpoints. Keeping experimentation in a development account separates test permissions and configuration changes from production requests.

### Amazon Bedrock: protect managed model access
<a name="amazon-bedrock-protect-managed-model-access"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html) manages model hosting. The application team configures access to the service and separates production invocation from model administration. For applications running in an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), invoke models through a [Bedrock Runtime interface endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) with private DNS enabled. Allow HTTPS connections from the application security group and restrict the endpoint policy to the intended roles, model resources, and invocation operations. An endpoint policy governs only requests through that endpoint. When private access is required, apply an explicit deny outside the approved endpoint. Follow the [endpoint policy and private-path examples](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#network-security), including the AWS service exceptions and permitted and denied tests.

The model service and your application have separate responsibilities. If you operate the application on containers or instances, maintain that compute even though Bedrock manages model hosting.

### Amazon SageMaker AI: protect hosted endpoints
<a name="amazon-sagemaker-ai-protect-hosted-endpoints"></a>

[SageMaker AI inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html) includes real-time, serverless, asynchronous, and batch options. The team operating inference governs the model artifact, serving image, execution role, and deployment configuration for the selected option. Deployment needs its own approval because approval of a training run does not grant permission to create or update a production endpoint.

For real-time inference, configure the model's [VPC access](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html) with private subnets and security groups limited to required resources. Use a [SageMaker Runtime interface endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html) for private invocation from the application. These are separate connections: the model's VPC configuration controls access to workload resources; the interface endpoint provides the caller's path to the service.

Enable [network isolation](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) for compatible serving containers that do not need outbound calls. SageMaker AI transfers model artifacts separately; the isolated container cannot call [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) or other VPC resources. If the serving code needs those connections, restrict its network access to the required destinations. [Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) does not provide VPC configuration or network isolation, so choose a different hosting option when those controls are required. Assign an owner for serving code and dependency updates.

### Shared application and self-hosted compute controls
<a name="shared-application-and-self-hosted-compute-controls"></a>

For models hosted on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html), or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html), your team owns the serving stack and its maintenance. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) provides applicable compute and image vulnerability scans, and [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) provides patching for managed nodes you operate. These controls address vulnerabilities in the serving software; model responses need the separate evaluations described later on this page.

Protect public application entry points with authentication, usage limits, request validation, and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) where the frontend resource permits it. Use [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-protections-by-resource-type.html) for additional distributed denial of service (DDoS) protection where required, selecting eligible frontend resources for protection. Use [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) for egress that requires inspection, and verify that the relevant traffic traverses it.

### Filter outbound DNS requests
<a name="filter-outbound-dns-requests"></a>

Use [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) to filter DNS queries from application and serving workloads in VPCs. Associate rule groups with each workload VPC. Block known unsafe domains, and use an allow list when you know the workload's required destinations. Enable [Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-resolver-query-logs-configuring.html) and test permitted and blocked lookups before rollout.

DNS Firewall filters queries sent through Route 53 Resolver. Combine it with network egress controls that restrict direct IP connections and alternate DNS services, including external DNS over HTTPS. DNS filtering can limit outbound communication from compromised dependencies; dependency review and artifact verification remain necessary.

## Identity and data security
<a name="identity-and-data-security"></a>

Authorize users and applications to invoke approved models, and limit access to retained content according to its classification.

### Amazon Bedrock: authorize approved model invocation
<a name="amazon-bedrock-authorize-approved-model-invocation"></a>

The application uses an [IAM role for Amazon Bedrock access](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html) to invoke its approved model resources. Limit the role to the operations the application needs, with separate permissions for model customization and guardrail administration. Use the [model and inference-profile policy examples](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#restrict-approved-models-and-regions) to define the permitted resources. For cross-Region inference, a destination Region can process prompts and responses. Review the profile's destinations against data residency requirements and apply the [geographic or global profile controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#review-cross-region-inference-permissions) before granting access.

AWS and third-party model providers [do not use Amazon Bedrock inputs or outputs to train Amazon Nova, Amazon Titan, or third-party models](https://repost.aws/knowledge-center/amazon-bedrock-model-data-use). Customer-requested [model customization](https://dp8l2mfblnx2f.cloudfront.net/answers/model-customization/) uses the training data you supply. Before approving a model, separately review its [data retention requirements](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) and [abuse detection terms](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html). Disabling application logs or setting `store=false` might not result in zero retention. Record whether the selected model and endpoint can process each data classification.

### Amazon SageMaker AI: separate invocation from deployment
<a name="amazon-sagemaker-ai-separate-invocation-from-deployment"></a>

Give the application role only the [invocation permissions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_sagemaker.html) required for its approved Amazon SageMaker AI endpoint Amazon Resource Names (ARNs). Configure a separate [hosting execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-createmodel-perms) with access to the required model artifacts, images, and other resources. Give the deployment workflow permission to create and update endpoints and pass that execution role; withhold those permissions from the application role. Test that the application can invoke its approved endpoint but cannot update it or invoke unrelated endpoints.

### Shared user identity and retained data controls
<a name="shared-user-identity-and-retained-data-controls"></a>

Select user sign-in using the [AI application access guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/). Authenticate the user and authorize their inference request before the backend uses its AWS role to call the model. Apply the [shared identity and data controls](https://dp8l2mfblnx2f.cloudfront.net/architecture/#apply-shared-network-and-identity-controls) to invocation roles, credentials, and retained content, then test permitted and rejected requests.

[Classify prompts, responses, conversation history, and caches](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html) by sensitivity and applicable legal requirements before retaining them. Have the data owner approve permitted uses, readers, and retention for each stored copy. Enforce those decisions with access policies and expiry settings; test unauthorized reads and removal when retention ends.

For supported text, [configure sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html) to block or mask selected personally identifiable information (PII) and patterns, then [test the deployed guardrail version](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-test.html) with representative sensitive and non-sensitive examples. Use [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) to discover sensitive data already stored in supported Amazon S3 objects. Neither detection nor masking grants permission to retain a record.

## AI application security
<a name="ai-application-security"></a>

Validate model inputs and outputs to reduce prompt injection and unsafe handling before responses reach users or downstream systems.

Include custom request handlers, model-serving code, and output-processing code in the [application code review workflow](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/#review-custom-application-code-with-aws-continuum). Test that requests remain bound to the authenticated user's session. For output handling, keep [HTML autoescaping](https://docs.aws.amazon.com/amazonq/detector-library/jsx/do-not-disable-html-autoescape/) enabled when displaying responses and pass generated data values as [SQL parameters](https://docs.aws.amazon.com/amazonq/detector-library/csharp/sql-injection/). Apply the model input, output, and behavior checks below alongside that review.

Use [Amazon Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html) or manage prompts in the application's version-control and release process. [Separate permissions to use and change prompts](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec04-bp01.html). Review and test changes before release, and record the prompt version used for each deployment.

### Amazon Bedrock: configure and test inference guardrails
<a name="amazon-bedrock-configure-and-test-inference-guardrails"></a>

Use [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to apply content policies to model inputs and outputs. Configure prompt attack, harmful content, denied topic, and sensitive information filters for the application's risks. Use the [organization policy](https://dp8l2mfblnx2f.cloudfront.net/architecture/#set-organization-wide-controls) for the centrally enforced baseline and add reviewed application guardrails where required. IAM policies using `bedrock:GuardrailIdentifier` can reject requests that omit or change a required application guardrail; they do not attach it. Follow the [Bedrock integration pattern](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#prompt-injection-protection) for enforcement and API coverage.

Applications using external model providers can call [ApplyGuardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html) to inspect content and act on the result. Verify that alternate callers cannot bypass required checks. Test prompts, responses, streaming, and alternate APIs. Use [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) with representative and adversarial prompts before release and after model changes.

### Check grounding and relevance
<a name="check-grounding-and-relevance"></a>

For summarization or question answering from reference material, configure [contextual grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html). Supply the reference source, user query, and response, and test grounding and relevance thresholds with representative data. These checks assess the response against the supplied source; they do not establish that the source itself is correct. Streaming relevance checks can identify an irrelevant response only after it has been streamed. When validation must precede disclosure, buffer the complete response, [evaluate it with ApplyGuardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html#guardrails-contextual-grounding-applyguardrail-api) within its input limits, and handle the findings before returning it.

### Validate policy-bound responses
<a name="validate-policy-bound-responses"></a>

Amazon Bedrock [Automated Reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html) assess responses against a policy you define. They return findings in detect mode, so the application team must review the policy and decide how to handle those findings. The checks require complete responses and cannot process streaming API requests. Complete required validation before returning a response or acting on it.

[Centrally enforced guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html) don't support Automated Reasoning policies. Use a supported application-request guardrail or a separate `ApplyGuardrail` call for these checks. Apply the [authorization controls](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#identity-and-data-security) and [prompt-injection defenses](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#prompt-injection-protection) separately.

### Amazon SageMaker AI: integrate input and output checks
<a name="amazon-sagemaker-ai-integrate-input-and-output-checks"></a>

A SageMaker inference application can call the independent [ApplyGuardrail API](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html) to assess text before sending it to the endpoint and before returning generated text to the user. The application implements this integration: it makes the guardrail calls and acts on their results. Amazon Bedrock Guardrails doesn't automatically apply to a SageMaker endpoint.

For this integration, check the input, invoke the endpoint only when the input is allowed, check the response, and return only the permitted result. Define a safe response when checks fail or are unavailable. Verify that streaming and alternate endpoint callers cannot bypass required checks. Evaluate model behavior and serving changes in your SageMaker release workflow. Content checks complement the endpoint's IAM and network controls.

### Shared output handling and investigation evidence
<a name="shared-output-handling-and-investigation-evidence"></a>

Your application can display generated output to a user or pass it to another component. Validate and encode it for that destination before use. Content filtering addresses content policies; factual accuracy and permission to run an action require separate checks. Set [limits on prompt size and request rate](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec04-bp02.html), and configure input and output token limits for the selected model. Verify that input and output checks cover the content types the application accepts. Provide a defined response for rejected requests and failed dependencies.

Enable [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) in each account and Region where investigation requires request and response records. Amazon Bedrock disables this logging by default. Select the permitted content types and an [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) or Amazon S3 destination in the same account and Region, then apply access and retention controls. Use Amazon S3 for large or binary content that you cannot retain inline in CloudWatch Logs.

Applications sharing an account and Region share this logging configuration. Use separate accounts when log-reader access, retention, ownership, or data classification requires a separate boundary. Shared logging alone does not require an account per application; assess the [account separation tradeoffs](https://dp8l2mfblnx2f.cloudfront.net/architecture/) with the content owners.

Invocation logging covers supported Bedrock Runtime calls, including the OpenAI-compatible Responses and Chat Completions APIs on that endpoint. Review logging coverage when changing endpoints or APIs. For SageMaker AI, collect endpoint logs and decide whether the investigation requires captured inputs and outputs before enabling [SageMaker AI Data Capture](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture-endpoint.html).

Correlate these records with application request IDs and [Amazon CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html). Set alarms for invocation errors, throttling, and unexpected usage. Configure [AWS CloudTrail event coverage](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html) for the APIs in use. Enable data events for `AWS::Bedrock::Guardrail` to record direct `ApplyGuardrail` calls and evaluations during model invocation, including request-level and organization-enforced guardrails. When multiple guardrails apply, the event does not identify which guardrail produced each assessment. CloudTrail audit records do not replace the content logging decision.

Apply the [shared threat detection](https://dp8l2mfblnx2f.cloudfront.net/architecture/#detect-threats-in-ai-workloads) and [configuration checks](https://dp8l2mfblnx2f.cloudfront.net/architecture/#keep-required-settings-enabled). Verify that findings reach an assigned response owner and identify the model, endpoint, or invocation path affected.

## Design considerations
<a name="design-considerations"></a>

The foundational controls and shared application controls address different parts of the request flow. Logging decisions need to balance investigation requirements with restrictions on retained prompt and response content. Add data and knowledge base controls when the application retrieves information, and agentic controls when it selects tools or takes actions.
