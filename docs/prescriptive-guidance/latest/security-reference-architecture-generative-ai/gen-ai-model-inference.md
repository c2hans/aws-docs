---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-model-inference.html
---

# Capability 1. Providing developers and data scientists secure access to generative AI FMs (model inference)
<a name="gen-ai-model-inference"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

Organizations building AI-powered applications must understand the fundamental differences between traditional AI systems and generative AI foundation models (FMs). Traditional AI systems perform classification, prediction, or optimization tasks with consistent outputs. Generative AI creates new content (text, images, code, or other media) based on learned patterns from training data. FMs are large-scale neural networks trained on vast datasets that generate probabilistic outputs, meaning identical inputs can produce different responses across invocations. This non-deterministic behavior requires security architectures that account for output variability while maintaining consistent protection.

Building applications that integrate generative AI FMs and agent capabilities enables advanced functionality, including natural language processing (NLP), image generation, automated reasoning, and intelligent decision support. This integration drives organizational innovation by allowing developers to build solutions that improve productivity and competitive positioning. However, the probabilistic nature of AI outputs demands security controls that function effectively regardless of model response variability.

## Rationale
<a name="model-inference-rationale"></a>

This use case corresponds to Scope 3 of the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/). In Scope 3, your organization builds an application or feature that integrates generative AI by using pre-trained FMs, such as those offered on Amazon Bedrock. You control your application and any customer data used by your application, whereas the FM provider controls the pre-trained model and its training data. For data flows pertaining to various application scopes and information about the shared responsibility between you and the FM provider, see [Securing generative AI: Applying relevant security controls](https://aws.amazon.com/blogs/security/securing-generative-ai-applying-relevant-security-controls/) (AWS blog post).

Organizations can also implement custom AI solutions using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) for model development, training, and deployment. This approach introduces additional security considerations including secure model development environments, protection of training data and model artifacts, and governance of the entire machine learning lifecycle.

Custom models require enhanced monitoring for model drift, bias detection, and performance degradation that could indicate security issues or model compromise. When you customize FMs with your own training data (Scope 4) or train models from scratch (Scope 5), training data security becomes critical. Malicious or poisoned training data can compromise model behavior, introduce bias, or cause models to leak sensitive information during inference. For detailed guidance on securing model customization and training data, see Capability 2.

The security architecture must address both the non-deterministic nature of AI systems and the autonomous capabilities of AI agents. The security architecture must implement layered defenses that maintain effectiveness across the spectrum of possible AI behaviors and outputs.

## Security considerations
<a name="model-inference-security"></a>

AI workloads introduce unique attack vectors and operational risks that traditional security controls don't address. Unlike conventional applications with predictable input-output relationships, AI systems process natural language and generate probabilistic responses that attackers can influence through carefully crafted inputs.

### Model-specific risk
<a name="model-specific-risk.12c2ed34-0ab5-578d-8411-6e217aac5513"></a>

These risks target the AI model itself, exploiting the probabilistic nature of neural networks and their training methodologies. Attackers can manipulate model behavior without traditional code injection, instead using carefully crafted natural language inputs to achieve malicious outcomes. Risks include the following:
+ Resource exhaustion through crafted prompts that trigger excessive token generation
+ Data exfiltration through prompt engineering techniques that extract training data or fine-tuning information
+ Model behavior manipulation through adversarial inputs designed to bypass safety mechanisms

### Application layer risks
<a name="application-layer-risks.4cf036ff-1257-5e20-923d-1d05985c6498"></a>

AI applications face unique challenges in validating and securing the interface between human users, AI models, and downstream systems. Traditional application security assumes deterministic behavior with predictable input-output relationships, but AI outputs require dynamic validation strategies that can assess content quality, safety, and appropriateness in real-time. Applications must handle scenarios where models generate syntactically valid but semantically problematic outputs. Examples of such outputs include hallucinated information presented as fact, biased responses that reflect training data patterns, or outputs that inadvertently reveal system architecture details.

The integration of AI into existing application workflows introduces risks when downstream systems consume model outputs without proper validation. This situation can potentially lead to automated execution of flawed recommendations or propagation of incorrect information through business processes. Additionally, conversational AI applications maintain complex session state across multiple interactions, creating opportunities for session manipulation, context poisoning, and unauthorized access to conversation history containing sensitive information.

A systems-thinking approach reveals deeper interdependencies where AI application risks cascade across system boundaries. Model outputs influence not just immediate application behavior but also training data for future models, decision-making processes, and user trust relationships. Security failures at the application layer can create feedback loops where compromised outputs become trusted inputs, gradually degrading system integrity over time.

The temporal nature of AI interactions means that security decisions must account for both immediate threats and long-term systemic impacts. These impacts include how model behaviors evolve through user interactions and how application-level vulnerabilities might be exploited across multiple sessions or user contexts, such as:
+ Unvalidated model outputs being passed to downstream systems
+ Context injection where malicious content in Retrieval Augmented Generation (RAG) sources influences model behavior
+ Session hijacking in conversational AI applications with inadequate state management
+ Missing rate limiting enabling resource exhaustion and denial of service attacks
+ Inadequate authentication and authorization for model access endpoints
+ Insecure storage of conversation history and user interaction data
+ Cascading failures when AI-generated content triggers errors in downstream business logic
+ Model output caching creating stale or contextually inappropriate responses
+ Feedback loop contamination where AI outputs become training data without validation
+ Compound security issues where multiple minor issues combine to create potential security issues

### Data governance risks
<a name="data-governance-risks.66a01742-c91c-5cfc-878a-38766d810ca3"></a>

AI systems process and generate data in ways that challenge traditional data classification and protection mechanisms. Models can inadvertently memorize and reproduce sensitive information from training data, while their outputs may contain synthetic but realistic personal information. Risks include the following:
+ Sensitive data leakage through model memorization and regurgitation from custom foundation models
+ Compliance violations when personal data is processed without proper controls such as overly permissive agents
+ Data poisoning in fine-tuning scenarios where malicious training data affects model behavior
+ Cross-tenant data exposure in multi-tenant AI applications

## Multi-account architecture for AI workloads
<a name="model-inference-architecture"></a>

Organizations implementing AI at scale should adopt a multi-account strategy that provides clear separation of concerns, enhanced security boundaries, and simplified governance across different AI lifecycle phases. As shown in the following diagram, this architectural approach isolates inference workloads from training activities while maintaining centralized security oversight and cross-account collaboration capabilities:
+ **AI development account** – Sandbox for experimentation and prototyping with non-sensitive data
+ **AI inference account** – Production environment for AI model consumption and application hosting
+ **AI training account** – Secured environment for handling sensitive training data and production model development

![Multi-account architecture for AI workloads.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/9eb62ad9-5711-4135-8ee2-912542d0655d.png)

### AI development account
<a name="ai-development-account.b32ad59a-0a72-5805-9a61-f2ed4ad1d323"></a>

The development account provides a sandbox environment for AI experimentation, prototyping, and initial model development using non-sensitive data. This account enables data scientists and developers to explore AI capabilities, test new approaches, and develop proof-of-concept solutions without access to production or sensitive training datasets.

Deploy Amazon Macie [automated data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) to help security and data science teams identify and classify data in development environments. Configure Macie to scan Amazon Simple Storage Service (Amazon S3) buckets regularly and alert when sensitive data appears in the development account. This approach enables teams to remediate data classification issues before they reach production.

Structure this account with permissive development policies that encourage experimentation while maintaining clear boundaries that prevent access to sensitive data or production systems. Implement cost controls and resource limits to manage experimental workloads and use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor spending on development activities.

Deploy [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) for collaborative development environments, with shared notebooks and experiment tracking capabilities. Configure automated cleanup policies that remove unused resources and temporary datasets, maintaining a clean development environment while controlling costs.

### AI inference account
<a name="ai-inference-account.e67c5ff3-896d-57a5-8ad1-28c6da0d109a"></a>

The inference accounts serve as production environments for AI model consumption and application hosting. Organizations typically deploy multiple inference accounts to maintain workload isolation, for example, separate accounts for different business units, applications, or security boundaries. Each inference account contains Amazon Bedrock endpoints, agent orchestration services, and user-facing applications that consume foundation models or custom models deployed from the training account. Security controls in these accounts focus on runtime protection, user access management, and real-time monitoring of AI interactions.

Configure each inference account with restrictive IAM policies that prevent model training activities, while enabling comprehensive inference capabilities. Implement [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) or [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) for user authentication, and with fine-grained permissions that control access to specific models. Deploy [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to filter inputs and outputs, ensuring that AI interactions meet organizational security standards.

Establish cross-account trust relationships that allow inference accounts to access approved model artifacts from the training account through secure, audited mechanisms. Use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) endpoints to maintain private connectivity to AI services while implementing comprehensive logging through [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor all inference activities.

Use Amazon GuardDuty [Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) to scan untrusted files that users submit for processing, such as document uploads, images, or data files that AI workloads analyze. This protection is particularly important for applications that process user-submitted content like mortgage documents, resumes, or customer support attachments.

### AI training account
<a name="ai-training-account.4766ced7-ff7d-5d1c-b0ef-ad209d68432e"></a>

The training account serves as a highly secured staging environment specifically designed for handling sensitive training data and production model development. This account implements the strictest security controls because of the potential presence of personally identifiable information (PII), proprietary datasets, and other sensitive information used in model training processes. Models developed in the development account are promoted to the training account for production-grade training with real datasets before deployment to inference accounts.

Establish secure model promotion workflows that move models from development through training to inference environments with appropriate security validations at each stage. Implement automated security scanning of model artifacts and comprehensive approval processes before any model deployment to production inference systems.

Implement enhanced data protection measures including mandatory encryption at rest and in transit. Use AWS Key Management Service (AWS KMS) [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) that provide granular access control over sensitive training datasets. Deploy Amazon Macie with continuous monitoring to identify and classify sensitive data, to help make sure that all training materials are properly protected and access is appropriately restricted. If possible, redact sensitive data before using it for training to minimize exposure risk.

Configure Amazon SageMaker with private VPC deployments that eliminate internet access for training jobs, using VPC endpoints for necessary AWS service communication. Implement strict IAM policies that limit access to authorized personnel only, with multi-factor authentication requirements and session-based access controls for all training activities.

Establish secure data ingestion pipelines that validate and sanitize incoming training data while maintaining comprehensive audit trails of all data access and processing activities. Use Amazon S3 with [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) and versioning to help ensure training data integrity and provide immutable audit records of all training dataset modifications.

Implement temporary elevated access management for access to training data when feasible, granting time-limited permissions that automatically expire after use. Log all user activity through CloudTrail and configure CloudWatch alarms to detect anomalous access patterns to sensitive training datasets.

### Cross-account security and governance
<a name="cross-account-security-and-governance.71bba4f5-80f5-5888-a681-586fc80e302d"></a>

Implement centralized security monitoring through [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) and Amazon GuardDuty deployed across all three account types, with findings aggregated in a dedicated security account. Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to enforce consistent security baselines while allowing account-specific security enhancements, particularly for the training account's heightened security requirements.

Configure cross-account logging aggregation that forwards all AI-related logs to a centralized log archive account, with enhanced retention and protection for training account logs due to their potential sensitivity. Use [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to orchestrate security responses across all accounts while maintaining appropriate isolation between environments.

## Defense in depth
<a name="model-inference-defense"></a>

As shown in the following diagram, a defense-in-depth strategy implements security controls at different layers within each account to protect AI workloads. This section details security controls in the Application, Data, and Network layers.

### Application security layer
<a name="application-security-layer.56e5a625-6b71-5f45-9748-84de6b13f58e"></a>

Deploy [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) as the first line of defense against malicious requests targeting your AI applications. Configure rate limiting to prevent resource exhaustion attacks and implement AWS Managed Rules for the [Core rule set](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-crs) and [Known bad inputs](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-known-bad-inputs) managed rule groups. Create custom AWS WAF rules to detect common prompt injection patterns such as instruction override attempts, delimiter manipulation, and context escape sequences. For applications handling critical business functions or experiencing high request volumes, enhance this protection with [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) to guard against DDoS attacks.

Implement comprehensive input validation through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) request validators. Configure validators to enforce JSON schema requirements and establish appropriate character limits for prompts and metadata fields. This validation prevents malformed requests from reaching your AI models and helps mitigate prompt injection attacks.

Strengthen authentication and authorization by deploying [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) authorizers that validate user context and session state. Alternatively, implement [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) for policy-based authorization that evaluates fine-grained permissions dynamically based on user attributes, resource context, and request parameters before model invocation. This approach enables centralized policy management and consistent authorization decisions across your AI applications.

Configure response transformation to strip sensitive metadata from model outputs, helping to ensure that internal system information never reaches end users. This approach includes removing debug information, internal identifiers, and system prompts that could reveal application architecture or security controls.

Monitor the effectiveness of these controls through CloudWatch [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) that track prompt characteristics, response times, and error rates. Create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to identify anomalous patterns that potentially indicate attacks or system degradation, enabling rapid response to emerging threats.

### Data security
<a name="data-security.9975cb43-87cf-5e32-bd3b-893b264db8d9"></a>

Deploy Amazon Macie [automated data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) to identify and classify sensitive data in your AI inference workloads. Configure Macie to scan Amazon S3 buckets that contain the following:
+ User prompts and conversation logs
+ Model responses and generated content
+ RAG knowledge base documents
+ Agent memory and session data
+ Application configuration and prompt templates

Enhance detection capabilities with custom data identifiers that recognize your organization's specific sensitive data patterns. Review Macie findings regularly and establish automated remediation workflows using EventBridge to alert security teams when sensitive data appears in unexpected locations.

Implement encryption using AWS KMS with customer managed keys for all inference-related data at rest. Organize your encryption strategy by using separate keys for the following:
+ Conversation history and session data
+ RAG knowledge base documents
+ Agent memory and context storage
+ Application logs and audit trails
+ Cached model responses, if applicable

Establish key rotation policies that balance security requirements with operational efficiency. Implement cross-region key replication to support disaster recovery scenarios without compromising data protection.

Extend your data protection to real-time processing by deploying Amazon Comprehend [PII detection](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html) or [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) on both model inputs and outputs. Configure automatic redaction capabilities that operate in real time for interactive applications or in batch mode for stored conversations.

Amazon Comprehend detects common PII types including names, addresses, credit card numbers, and Social Security numbers. Amazon Bedrock Guardrails provides additional capabilities including custom regex patterns for organization-specific sensitive data and contextual filtering based on conversation flow.

Monitor PII detection rates through CloudWatch metrics to identify potential data handling issues and help ensure compliance with privacy regulations. Create CloudWatch alarms when PII detection rates exceed expected baselines, which may indicate users attempting to share sensitive information or applications inadvertently processing restricted data.

Configure Amazon S3 bucket policies that enforce encryption requirements, restrict access appropriately, and require multi-factor authentication for critical operations such as bucket deletion or policy modification. Implement Amazon S3 [access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) with VPC endpoints to provide role-based access control for different workload types. For example, create separate access points for application workloads accessing RAG knowledge bases, security teams reviewing conversation logs, and compliance auditors accessing audit trails.

Enable [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) for conversation logs and knowledge base documents to support audit requirements and incident investigation. Enable Amazon S3 data [event logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.html) through CloudTrail to maintain comprehensive access records, capturing who accessed what data, when, and from which source. For applications with data retention requirements, configure [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) policies to archive or delete conversation logs automatically after appropriate retention periods. This approach balances compliance needs with data minimization principles.

### Network security enhancement
<a name="network-security-enhancement.351d32fa-4e40-551a-97d8-5dbfff10edeb"></a>

Design your network security architecture around the principle of defense in depth. Begin with restrictive virtual private cloud (VPC) security groups that allow only necessary traffic between application tiers. Structure these security groups to create clear boundaries between web, application, and data tiers, with controlled inter-tier communication flowing only through designated ports and protocols. This segmented approach limits the potential impact of any security breach while maintaining operational functionality.

Architect your network topology using dedicated subnets for AI workloads. Design routing carefully so that traffic is directed through NAT gateways for secure outbound internet access and VPC endpoints for efficient AWS service communication. Implement network ACLs as an additional defensive layer, using explicit allow rules for required traffic while maintaining a default-deny posture for all other communications.

Enhance your network defenses by deploying [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html). Use its intrusion detection and prevention capabilities for east-west traffic between application tiers, north-south traffic for ingress and egress, and lateral movement detection within your VPC. Configure rules that identify unusual request characteristics, detect high-frequency automated attacks, and recognize other indicators of malicious activity targeting AI systems. This deep packet inspection capability provides visibility into threats that might bypass application-layer controls.

Deploy [Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-overview.html), a feature of Amazon Route 53 Resolver, to block malicious domain queries and enforce DNS-level security policies for your AI infrastructure. Configure DNS Firewall to block known malicious domains, prevent data exfiltration through DNS tunneling, and alert on suspicious DNS patterns that may indicate compromised systems or command-and-control communications.

Maintain comprehensive network visibility through [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) configured with custom formats that capture relevant metadata for security analysis. Enable VPC Flow Logs for all subnets hosting AI workloads. Configure VPC Flow Logs to capture accepted traffic, rejected traffic, and all traffic to provide complete visibility into network communications.

Integrate VPC Flow Logs with your security information and event management (SIEM) solution for automated pattern analysis and threat detection. You can use [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) for log aggregation and analysis, or integrate with third-party SIEM platforms that support AWS log ingestion. Configure your SIEM to detect anomalous patterns including unusual traffic volumes, connections to unexpected destinations, or communication patterns that deviate from established baselines.

Connect your threat detection system to EventBridge for orchestrated incident response. Configure EventBridge rules to trigger automated responses when security events are detected such as the following:
+ Invoke AWS Lambda functions to isolate compromised resources.
+ Execute [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runbooks to remediate common security issues.
+ Send notifications to security teams through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (Amazon SNS) for manual investigation.

This approach creates a closed-loop security monitoring and response system that reduces time to detection and response.

## Model evaluation and validation
<a name="model-inference-eval"></a>

Model evaluation represents a critical security checkpoint in AI implementations, requiring comprehensive assessment of model behavior, output quality, and adherence to organizational policies before deployment. Evaluate foundation models (FMs) in the context of your specific use cases to ensure they meet security and quality requirements.

Before deploying an FM to production, establish evaluation frameworks that test model behavior against your security requirements. Use Amazon Bedrock model evaluation to compare different FMs and select the one that best meets your needs. Create standardized [evaluation datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets.html) that include adversarial examples to test model robustness against prompt injection, jailbreak attempts, and other manipulation techniques.

Test models against your organization's responsible AI policies by evaluating outputs for bias, toxicity, and alignment with ethical guidelines. Use [Amazon SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) to analyze model outputs for potential bias across different demographic groups or use cases. Document evaluation results and obtain appropriate approvals before deploying models to production environments.

Implement continuous monitoring through CloudWatch to identify performance degradation or unusual output patterns in production environments. Configure CloudWatch metrics to track model invocation rates, response latencies, error rates, and token usage patterns. Create CloudWatch alarms that trigger when metrics deviate from established baselines, which may indicate security issues, service degradation, or unexpected usage patterns.

Monitor [Amazon Bedrock Guardrails metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html) to track how frequently content is filtered or blocked, providing visibility into potential security threats or policy violations. Analyze trends in guardrail activations to identify emerging attack patterns or areas where additional security controls may be needed.

Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to establish automated pipelines that orchestrate regular security assessments, performance benchmarks, and compliance validation. Configure these pipelines to run on a schedule or trigger based on specific events such as significant changes in usage patterns or the availability of new model versions.
