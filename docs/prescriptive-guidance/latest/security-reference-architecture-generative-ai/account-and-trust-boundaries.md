---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/account-and-trust-boundaries.html
---

# Account and trust boundaries

AWS accounts separate workloads with different data access, deployment permissions, and operational owners. Organizational units (OUs) group accounts that need common governance policies. In this architecture, accounts contain the applications and AI resources, and OUs organize their governance.

This account separation provides two key benefits. First, it enforces security controls through OU-specific and account-specific service control policies. Second, it simplifies implementing least-privilege access by grouping services based on application type. The reference architecture also includes foundational accounts that apply to all application types: Org Management, Security Tooling, Log Archive, Network, and Shared Services. For more information about these accounts, see [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) in the [*AWS SRA – core architecture*](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) guide.

Start with the [organization and account foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html) in the core AWS Security Reference Architecture (AWS SRA), using [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) and, where applicable, [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to govern accounts consistently. Follow its [central logging and configuration guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html), using [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to record API activity and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to record supported resource configuration changes. For OU and account design, see [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html).

The reference pattern uses separate **Application** and **AI workloads** OUs under the Workloads OU, with separate accounts for application hosting and AI resources. This grouping lets teams apply [common governance policies](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/design-principles-for-your-multi-account-strategy.html) to accounts with similar control requirements. The **AI workloads** OU extends the SRA's *Generative AI* grouping to cover inference, training, retrieval, and agents across [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), and other AI hosting options.

## Place AI systems within the account structure
<a name="place-ai-systems-within-the-account-structure"></a>

The diagram adds an AI system to the [SRA account foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html). The Application account runs the business frontend and backend. The separate AI inference account contains model access through Amazon Bedrock or Amazon SageMaker AI endpoints, knowledge bases for retrieval, and AgentCore Runtime for agent execution. AgentCore Gateway and Policy control the agent's tool calls; each tool has separate permissions for business resources.

Security and Infrastructure accounts provide shared controls. Development uses approved non-sensitive data. The production Application, AI inference, and protected training accounts sit within the production security boundary. [Machine learning operations (MLOps)](https://aws.amazon.com/what-is/mlops/) is a set of practices that automate and simplify [machine learning (ML)](https://aws.amazon.com/what-is/machine-learning/?refid=1a84fd07-e681-41eb-8d84-062020330b11) workflows and deployments. MLOps describes the process across these AWS accounts, including evaluation and release; it does not imply a separate or less trusted environment.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/9015d43d-2324-43ff-91b5-bc7366955a92.png)

***Fig 2: AWS SRA of AI Security AWS OU and account structure with AWS service reference***

|
|
| **OU in this example** | **Accounts inside it** | **Responsibility** |
| --- |--- |--- |
| Security | Security Tooling; Log Archive | Operate shared detection, investigation, and protected evidence storage. |
| Infrastructure | Network; Shared Services | Operate shared connectivity, inspection, directory, and delivery services. |
| Application / Development | Application development account | Build and test the application with approved non-sensitive data. |
| Application / Production | Application account | Run the business frontend and backend; access AI resources through authorized roles. |
| AI workloads / Development | AI development account | Experiment and test with approved non-sensitive data. |
| AI workloads / Production | AI inference account | Run approved model access, retrieval, agents, and tools. |
| AI workloads / Production, when training is needed | AI training account | Protect training data and model development with production controls; release evaluated artifacts through a separate approval path. |

The Application and AI workloads OUs are peers under Workloads in this example. Adapt the OU hierarchy to existing governance requirements, and keep development and production in separate accounts. Apply the organization's service control policies (SCPs) to these accounts, and grant workload permissions through [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) roles. For an example of an SCP that prevents users from using unapproved Amazon Bedrock models, see the [example SCP](https://github.com/aws-samples/service-control-policy-examples/blob/main/Service-specific-controls/Amazon-Bedrock/Deny-Bedrock-model-invocation-except-approved-models.json). You can apply this SCP to your whole organization or to an OU. Create additional accounts when data ownership or deployment authority needs a separate boundary. Create a new OU only when accounts need different governance.

Place an [organization-scoped AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the central account whose team owns agent discovery and approvals. Use the Shared Services account when its team owns this function, or a dedicated account when ownership or isolation requirements differ. Register the selected account as the delegated administrator.

**Design considerations**:
+ Merge the Application and AI accounts if your architecture requires hosting both workloads in one account, or if your generative AI usage spans your entire organization.
+ Use multiple accounts when different user communities have distinct risk profiles, when customized models contain sensitive training data, or when regulatory requirements mandate data isolation.
+ Use a single account when you only use pre-trained foundation models, when users have a consistent risk profile, or when IAM roles meet your access control requirements.

## Set organization-wide controls
<a name="set-organization-wide-controls"></a>

Define the approved services, models, inference profiles, and processing Regions. Use [service control policies (SCPs)](https://github.com/aws-samples/service-control-policy-examples/tree/main/Service-specific-controls/Amazon-Bedrock) to restrict Amazon Bedrock permissions for member accounts. Workload IAM roles grant the access each application needs within that limit. Apply the [model and Region policy examples](bedrock-integration.md#restrict-approved-models-and-regions) to the approved invocation paths.

Use an [AWS Organizations Amazon Bedrock policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html) to enforce a centrally managed guardrail for all model inference calls to Amazon Bedrock within the policy's scope. Grant the organization access through the guardrail's resource-based policy and give calling roles permission to apply it. Check [enforcement requirements](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html): organization enforcement excludes guardrails with Automated Reasoning policies. Test the versioned guardrail Amazon Resource Name (ARN) in a small set of test accounts before expanding the policy; an invalid identifier can cause model calls to fail. Verify the effective policy for each account; parent and child attachments resolve to one guardrail configuration.

Use temporary IAM role credentials for production workloads. Restrict long-term key creation and use with the [Amazon Bedrock API key permissions guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-permissions.html). Apply the documented service-name and long-term token conditions to avoid blocking unrelated service credentials or short-term keys.

Apply [Amazon GuardDuty organization policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) and [Amazon Inspector organization policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html) to require the selected protections and scan types in governed accounts and Regions, including new accounts. Include [Amazon GuardDuty AI Protection](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html) where applicable. Member accounts cannot disable settings managed by these policies. For more information, see [What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) and [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/)

Apply [SCPs, resource control policies (RCPs), and declarative policies](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html) to the accounts and resources that host AI workloads. Use the [data perimeter guidance](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) to constrain access to training data, knowledge sources, and model artifacts. Check service and action coverage and test required service integrations before rollout.

Keep ownership and data classification in the workload record and, where supported, resource tags. Check for missing or inconsistent values. Where required, use [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_all.html) to restrict the use of your content for service improvement by the supported AI services.

Align backup retention and restore procedures with deletion requirements. Revalidate restored datasets before ingestion or training so that restores do not reintroduce removed or poisoned content.

## Review cross-Region inference permissions
<a name="review-cross-region-inference-permissions"></a>

For [geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html), authorize the inference profile in the source Region and the model resources in the source and all possible destination Regions. A service control policy (SCP) that denies a destination Region can cause the request to fail, even when other destinations are allowed. Allow the required Regions or use the documented exception scoped by `bedrock:InferenceProfileArn`, while retaining the source Region restriction.

For [global inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html), AWS evaluates the Region-agnostic foundation-model resource with `aws:RequestedRegion` set to `unspecified`. A Region-deny SCP must accommodate this value or the approved profile exception. Denying named destination Regions does not constrain global routing, which can use commercial Regions across the globe. Choose geographic or single-Region inference when processing must remain within a defined geography.

For SCP and AWS Control Tower examples, see [Enable Amazon Bedrock cross-Region inference in multi-account environments](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/).

## Map account roles to your services
<a name="map-account-roles-to-your-services"></a>

The account roles describe stages in the workload's lifecycle. You can use both Amazon Bedrock and Amazon SageMaker AI in development, inference, or training accounts. For example, place a SageMaker AI production endpoint in the inference account, and place a SageMaker AI training job in the training account.

|
|
| **Account role** | **Amazon Bedrock example** | **Amazon SageMaker AI example** |
| --- |--- |--- |
| AI development | Test model calls, prompts, and retrieval using approved test data. | Use [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html), experiments, test training jobs, and test endpoints. |
| AI inference | Provide application access to approved models, guardrails, and knowledge bases. | Host approved models on inference endpoints or run batch inference. |
| AI training, optional | Run permitted model customization jobs with approved input and output stores. | Run training jobs and pipelines; govern model versions and release approvals. |

An inference account can host a pretrained model even when the organization does not operate a training environment. You can use SageMaker AI to deploy models trained elsewhere. For more information, see [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-get-started.html). Similarly, a knowledge base retrieves information for a model request without training the foundation model. That workload needs the inference and retrieval controls described in this guide.

## Application and inference accounts
<a name="application-and-inference-accounts"></a>

Use [separate application and inference accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/bedrock-integration.html) as the starting pattern. This separates deployment authority and permissions when ownership, data sensitivity, or required controls differ. The AI inference account can contain models, knowledge bases, agents, and tools that share an owner and data boundary. Give agents least-privilege [execution roles and authorized actions](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp02.html).

**Design considerations**
+ Consider [combining application hosting and AI inference](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html) when ownership, risk, and required controls align and IAM roles provide sufficient access control. Apply organizational unit (OU) policies that cover both workloads.
+ Separate development, test, and production accounts, using [environment OUs](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html) to apply their controls.
+ Use separate accounts for [user communities with different risks, sensitive customized-model data, or required regulatory isolation](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html). Keep protected training in its separate account within the [production security boundary](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-model-inference.html).
+ Assess [external tool and data access](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02.html) before consolidating agents that use pre-trained models. Their permissions and actions can create risks beyond model inference.
+ In either pattern, use distinct agent identities, [authorize tool actions before execution](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp01.html), and [restrict outbound traffic](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html) to required destinations.

Shared application or AI services can use dedicated accounts in the [Workloads OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/application-ous.html#workloads-ou). Choose their placement according to ownership and isolation requirements.

In a cross-account Amazon Bedrock design, the application assumes an authorized role to invoke the model in the inference account. The "Integrating a traditional workload" section of this guide explains that request flow and the role trust, invocation permissions, resource access, and network configuration that you must establish.

## Development account
<a name="development-account"></a>

The development account gives teams an environment for experimentation with approved services and non-sensitive test data. Use synthetic or de-identified data, and prevent development roles from accessing protected training datasets or modifying production resources. Perform work that requires protected data in the governed training account. Give developers access through federated roles, set spending alerts, and remove unused notebooks, endpoints, and other test resources.

## Training account and model promotion
<a name="training-account-and-model-promotion"></a>

The training account holds the datasets, notebooks, jobs, and artifacts used to train or customize production models. [Treat it as part of the production security boundary](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-model-inference.html), including during model development. Apply production access, encryption, network, logging, and data-handling controls.

Training can require high-fidelity protected data. Minimize or de-identify it where the training objective permits, and evaluate privacy techniques that fit your use case. These techniques do not replace the account boundary or dataset access controls. Grant data scientists access only to the specific datasets that they need inside the training environment. Keep training execution, model approval, and production inference deployment permissions separate so that completing a training job cannot authorize a release.

Model promotion moves an evaluated and approved version into the inference environment. In the release record, identify the dataset and model versions, evaluation results, and approval. Protect those records along with input data, checkpoints, and model artifacts. The sharing or deployment mechanism depends on the selected service and model. Refer to the "Model Customization" section of this guide.

Training and production inference can both process sensitive data. Set additional controls based on the data classification and the operations that you permit in each account.

## Review the boundaries before deploymen
<a name="review-the-boundaries-before-deploymen"></a>

Use the [boundary tests](https://dp8l2mfblnx2f.cloudfront.net/conclusion/#test-the-boundaries-that-apply) to verify these decisions. The worked examples cover [model and Region restrictions](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#restrict-approved-models-and-regions) and [retrieval authorization](https://dp8l2mfblnx2f.cloudfront.net/bedrock-integration/#enforce-retrieval-scope-in-the-backend).

|
|
| **Boundary** | **Decision to record** | **Verification** |
| --- |--- |--- |
| User to application | Sign-in method and the user's allowed conversations, data, and actions | Another user's session or document remains inaccessible. |
| Application to model | Execution role, approved model or endpoint, and request path | The application rejects unapproved model access. |
| Application to knowledge base | Dataset ownership, retrieval authorization, and permitted ingestion | Retrieval cannot return documents outside the caller's entitlement. |
| Agent to tool | Tool identity, permitted operation, and approval conditions | The tool rejects unauthorized actions independently of the model. |
| Training to inference | Artifact provenance, evaluation, approval, and deployment authority | An unapproved model cannot enter production. |
| Workload to security operations | Required logs, content handling, retention, and response owner | You can trace and investigate an allowed test event. |

IAM roles, resource policies, AWS KMS keys, and network configuration enforce the access rules between these accounts. Review them together with the account structure. Content safeguards address model inputs and outputs; authorization determines whether a caller can access data or perform an operation.

## Reuse shared security controls
<a name="reuse-shared-security-controls"></a>

Centralize [detection, investigation, and telemetry](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html), including [Amazon CloudWatch Unified Data Store](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) and [Amazon CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html). Application teams provide the model, retrieval, and tool records that you need to investigate their workloads. Configure CloudTrail coverage for the APIs in use and correlate those audit events with the application records. CloudTrail audit events alone do not provide a conversation transcript.

|
|
| **Record** | **Collection and access** |
| --- |--- |
| API activity | Configure CloudTrail coverage for the required management and data events. Use [central archive and investigation roles](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html). |
| Amazon Bedrock prompts and responses | Configure [model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) for supported Amazon Bedrock Runtime requests in each account and Region. Model invocation logging first delivers logs to destinations in that account and Region, so configure forwarding or replication for a central archive. Grant content access only to approved investigators. |
| Retrieval and tool decisions | Instrument the application to record verified caller identity, authorization decisions, source or tool versions, and outcomes. Exclude credentials and unnecessary content. |

Separate archive administration from workload execution. Prevent workload roles from deleting audit records or shortening retention, and test that approved investigators can correlate these records without gaining unnecessary access to workload data.

## Detect threats in AI workloads
<a name="detect-threats-in-ai-workloads"></a>

Enable [GuardDuty AI Protection](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html) for supported Bedrock, AgentCore, and Amazon SageMaker AI activity. GuardDuty collects the relevant CloudTrail data events through its own service-linked channel; configure your own trails separately for audit and investigation. Select additional protections according to the resources in the workload: [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) for supported compute, and [Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) for objects awaiting ingestion. Neither establishes that a model response or tool action is authorized.

Enable [GuardDuty S3 Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) in each relevant Region to detect suspicious access to training data, knowledge sources, and model artifacts in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). It analyzes S3 data events; Malware Protection for S3 scans object contents.

Use [central finding aggregation](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) and assign response ownership. Keep application authorization failures and unsafe-action tests alongside service findings.

Use [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) to prioritize posture, vulnerability, and threat findings. Use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) for configuration checks. Enable the required Amazon Inspector and GuardDuty capabilities separately. Enable [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) separately for sensitive data discovery. Security Hub [unused access findings](https://docs.aws.amazon.com/securityhub/latest/userguide/unused-access-findings.html) identify unused IAM roles, user credentials, and permissions. Configure external-access analysis separately.

## Inventory AI resources
<a name="inventory-ai-resources"></a>

Maintain an approved workload record of models, knowledge bases, agents, and tools, as outlined in the "Implementation record" subsection of the "Verification and next steps" section of this guide. Record the owner, business purpose, data classification, and permitted access. Compare discovered resources and external AI activity with that record. Investigate unapproved resources, unapproved activity, and missing ownership.

Use AWS Config for [recorded configuration and compliance history](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html). Use [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/supported-resource-types.html) to search supported resource types across the configured accounts and Regions. Review [indexing and view coverage](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html) when resources are missing from search results.

Use the [Security Hub AI inventory](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-ai-inventory.html) to review supported Bedrock, AgentCore, and Amazon SageMaker AI resources and detected self-hosted AI components. Self-hosted discovery uses supported Inspector scanning on [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances and [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) images. Amazon EC2 instances require enhanced agent-based, agentless, or hybrid scanning. GuardDuty DNS activity identifies supported external AI endpoints contacted from Amazon EC2 instances. Coverage is limited to supported resources and detection criteria, and excludes self-hosted AI on [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and other compute types. Assign separate discovery checks to those gaps, because an empty inventory doesn't confirm that no unapproved AI is in use.

Enable the [AI Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-ai-security.html) in AWS Security Hub CSPM for applicable configuration checks. Keep application behavior tests alongside those findings. For workloads that extend to Microsoft Azure, assess the supported resources and prerequisites of the [Security Hub Azure integration](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-azure.html) separately from this guide's AWS controls.

## Catalog approved agents and tools
<a name="catalog-approved-agents-and-tools"></a>

Use [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) to catalog agents, Model Context Protocol (MCP) servers and their tools, agent skills, and custom resources. Record ownership and data classification as [custom metadata](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-custom-metadata-schema.html). People and agents can discover approved records through keyword and semantic search or the [Registry MCP endpoint](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-mcp-endpoint.html). Configure IAM or JSON Web Token (JWT) for search and MCP access; registry and record management use IAM.

Grant discovery access only to consumers who may see the full catalog: [search and list permissions expose every approved record](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-iam-permissions.html). Keep credentials out of discovery metadata. [Validate referenced packages, repositories, and endpoints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-data-protection.html#registry-consumer-validation) before use; schema validation does not establish their security.

Auto-detection in the [organization-scoped registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) catalogs supported AgentCore Runtimes and Gateways from member accounts in the registry's Region. Assign curators to approve records for discovery and review subsequent revisions as outlined in "Govern configuration changes" in the "Agent execution and actions" section of this guide. Give the Security Tooling account read-only access through [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-account-sharing.html) for inventory review. Grant curation permissions only when that team owns approvals. Registry publication and approval do not grant permission to invoke the underlying agent or tool.

## Apply account baseline configuration
<a name="apply-account-baseline-configuration"></a>

Configure required logging and detection when provisioning accounts, and apply the same baseline to existing accounts. Check Bedrock model invocation logging, required guardrails, [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) policy enforcement, and runtime endpoint versions against that baseline. Verify the effective settings in each governed account and Region, alert the owner to drift, and confirm that logs reach their destination.

Use [central AWS Config rule management](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) for supported configuration checks. Check current [resource coverage](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html) and managed rules before adding a custom check. Assign settings that AWS Config does not record to service API checks or an explicit review.

Use [CloudWatch telemetry enablement rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-rules.html) for supported sources, including AgentCore logs and traces. Verify existing resources after rule changes; updated rules apply only to new matching resources. Configure Bedrock model invocation logging separately; telemetry enablement rules do not cover it. Include Gateway policy enforcement in configuration checks for agent workloads, as described in "Authorize downstream actions" in the "Agent execution and actions" section of this guide. Record coverage gaps and assign an owner.

Recheck configuration and application behavior when models, knowledge sources, tools, permissions, or deployed versions change. Record the approved change, test results, and any exceptions in the implementation record. A configuration check does not establish that retrieval authorization or agent actions still behave as intended.

## Apply shared network and identity controls
<a name="apply-shared-network-and-identity-controls"></a>

For shared network paths, use the [perimeter security guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/introduction.html). Use [AWS Firewall Manager DNS Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/dns-firewall-policies.html) to manage [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/vpc/latest/userguide/resolver-dns-firewall.html) rule group associations across in-scope accounts and [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) networks. The DNS filtering baseline describes workload configuration and testing.

Use [AWS Network Security Manager](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html) to manage a central [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) baseline and applicable [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) protections for AI application entry points. Check resource and Regional coverage separately for each protection type. Enable automatic remediation when you want the service to restore the approved baseline, and review how it handles existing web ACL associations. Use Firewall Manager for DNS Firewall policies; [existing Firewall Manager policies](https://docs.aws.amazon.com/network-security-manager/latest/devguide/firewall-manager.html) continue to operate. Where their scopes overlap, Network Security Manager takes precedence during remediation.

For identity and retained data, use the [identity management](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/introduction.html) and [privacy](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/introduction.html) guidance. Restrict encryption-key and secret access to the workload roles that need it, and separate those roles from administrators. [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) provides policy validation and reviews of supported external and unused access. Use those findings to reduce workload permissions, then test application authorization separately.

For AI datasets, use [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) to discover sensitive data in eligible S3 objects, accounting for sampling and coverage. [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html) can detect or redact personally identifiable information (PII) in supported text. Validate the results before admitting data to training, retrieval, or logs; classification and redaction do not replace access controls. Component pages describe the service-specific controls.

## Continue with your workload
<a name="continue-with-your-workload"></a>
+ [Model inference](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/): choose the Bedrock or Amazon SageMaker AI path.
+ [Data and retrieval](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=knowledge-bases-ai-that-connects): place knowledge bases and authorize retrieval.
+ [Agent execution and actions](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=agentic-ai-and-actions-ai-that-acts): constrain agent identity, tools, runtime behavior, and recovery.
+ [AI application access](https://apg-library.amazonaws.com/edit/a349f18f-a9fd-43a3-9a48-27534bf6412a#contents?section=ai-application-access): distinguish managed-product and custom-app access.
