---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/implementing-security-rai.html
---

# Implementing security and responsible AI
<a name="implementing-security-rai"></a>

Building generative AI (gen AI) models involves complex technical and business decisions. To speed up experimentation, some [responsible AI (RAI)](https://aws.amazon.com/ai/responsible-ai/) evaluations might be overlooked initially. However, conducting an RAI review *before *moving to inference helps organizations strengthen risk assessment and resource management through a structured evaluation process. This pre-release review serves as the final controlled stage where organizations can thoroughly assess models for potential harm. For example, organizations can assess models for bias amplification, privacy violations, safety risks, or misalignment with organizational values.

The RAI review consists of two phases:
+ Before moving to inference
+ After inference deployment

## Before moving to inference
<a name="before-moving-to-inference"></a>

To establish a foundation for responsible deployment, implement a model registry to track lineage, versions, and artifacts, ensuring traceability throughout the model's lifecycle. The model evaluation report provides a detailed assessment that quantifies robustness, fairness across demographic groups, and potential failure modes. This assessment offers visibility into unexpected behavior and supports informed trade-off discussions. These evaluations guide the creation of comprehensive governance structures, including formal approval workflows, stakeholder sign-offs, and escalation paths that maintain organizational awareness of potential risks and impacts.

To complement these governance mechanisms, implement technical safeguards such as multi-layered defensive controls for input validation, output filtering, and personally identifiable information (PII) sanitization. Finally, practical access controls—including API key authentication, identity-based authorization, and network isolation—protect inference endpoints from unauthorized use, abuse, and resource exhaustion.

### Model assessment
<a name="model-assessment.4e0838c1-fbb0-5a79-acff-7003cc26ae30"></a>

During the model assessment phase, the evaluation report helps the organization understand the model's robustness and explainability through quantitative and qualitative analyses. This analysis includes evaluating accuracy metrics, fairness scores, and error distributions, complemented by human-in-the-loop reviews and A/B testing to validate real-world performance. The report should also provide visibility into unexpected behavior, foster trade-off discussions, and guide the team in incorporating mechanisms for exception management.

### Documentation preparation
<a name="documentation-preparation.7546dbea-a613-52a3-bf5c-3f4ab1320170"></a>

With the model assessment report, the team can now develop internal documentation to record trade-offs and decisions made during the process. This documentation provides valuable context for future development iterations. When the documentation is revisited, it helps the team understand the limitations and requirements of the previous project timeframe.

A model card should include detailed specifications of the model architecture, training methodology, and hyperparameter configurations, along with performance metrics across diverse datasets and demographic groups. It must also explicitly outline both intended use cases and scenarios where the model should not be applied, establishing clear boundaries for appropriate deployment.

### Technical safeguards
<a name="technical-safeguards.2d487637-bd90-5937-b072-59fed390afcf"></a>

Technical safeguards protect the system from potential harm through engineering controls and architectural design choices. Before model deployment, developers must establish multi-layered defensive mechanisms, including the following:
+ Input validation to detect and reject adversarial prompts
+ Output filtering systems to identify and block harmful, misleading, or biased content
+ Thorough sanitization processes for PII

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) provides safeguards that you can configure for your generative AI applications based on your use cases and responsible AI policies.

### Governance setup
<a name="governance-setup.cdc5aa5a-0b7d-5e0a-be34-afa9e75f5254"></a>

Before deploying a model, organizations should establish formal deployment approval workflows. These procedures help to ensure that all stakeholders review evaluation reports and have access to shared documentation such as model cards and decision records. This approach fosters organizational awareness of potential risks and impacts associated with deployment. A structured approval process should be completed before release. Governance execution must align with previously documented requirements and include technical controls with clear purposes, such as configuring access permissions and rate limits to prevent resource abuse.

It's essential to control access to inference endpoints to prevent abuse, unauthorized use, and excessive consumption—particularly for public- or customer-facing systems. The following complementary access control methods are commonly used:
+ **API key authentication** – API keys provide a simple form of authentication that is natively supported by most popular frameworks and API specifications such as the [OpenAI API](https://github.com/openai/openai-openapi). Managed platforms such as Amazon Bedrock and open source frameworks such as [LiteLLM](https://github.com/BerriAI/litellm) provide options for issuing API keys to users through the UI and programmatically. API keys are associated with allowed models and usage limits. API keys should be securely loaded from an environment variable or key management service on the server and not be exposed to client-side code. Furthermore, API keys should only be valid short-term and rotated frequently, to prevent abuse in case of accidental leakage.
+ **Identity-based authentication** – Identity-based authentication relies on short-lived credentials and signed requests instead of shared secrets like API keys. Within AWS, callers assume AWS Identity and Access Management (IAM) [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Authorization is enforced through IAM [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) that scope allowed models, endpoints, and actions (for example, invoke, batch, and embeddings). In public- and customer-facing applications, end users typically authenticate through OAuth2/OIDC (for example, through [Amazon Cognito](https://aws.amazon.com/cognito/)). Then, identities are mapped to their respective IAM roles.
+ **Network isolation** – For company-internal inference endpoints, network isolation can be enforced by only exposing access with internal load balancers within a [virtual private cloud (VPC)](https://aws.amazon.com/vpc/) and by scoping access with [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) and [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html). If public ingress is unavoidable, use IP allowlists where possible. Also in that situation, the inference endpoint should be fronted by services such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [AWS WAF](https://aws.amazon.com/waf/). These AWS services prevent distributed denial of service (DDoS) attacks and other common exploits. Network isolation complements API keys and identity-based authentication so that even leaked credentials can't reach an endpoint directly.

In addition to access control, request payloads should always be encrypted in transit by enforcing SSL/TLS.

## After inference deployment
<a name="after-inference-deployment"></a>

A gen AI model deployment guided by RAI practices integrates three key elements to ensure models remain safe, effective, and aligned with organizational values:
+ Continuous monitoring provides observability through real-time tracking of performance metrics such as latency, throughput, and error rates. It also observes contextual metadata that enables analysis across dimensions like criticality, business domain, compliance, and resource use.
+ When issues arise, incident response mechanisms act as a rapid intervention system. Predefined procedures and clear roles and responsibilities help stakeholders access information and resources quickly to minimize impact.
+ Complementing these systems, feedback mechanisms capture user experiences that automated metrics might overlook. These mechanisms provide early warnings for hallucinations, bias, or harmful outputs while incorporating diverse perspectives to better reveal model limitations in real-world contexts.

### Continuous monitoring
<a name="continuous-monitoring.3cf56331-3785-5fde-b577-76a7330b680c"></a>

Continuous monitoring provides real-time visibility into model behavior and system performance across the inference lifecycle. Amazon SageMaker AI enables this observability through components such as [Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) for detecting data and concept drift, [SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) for bias detection and explanations, and [SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) for real-time performance tracking. These tools, combined with tagging model interactions by use case, generate contextual metadata that supports deeper analysis and operational insights. For example, critical versus non-critical workload tags enable prioritization during incident response. Business domain tags support performance comparisons. Compliance tags facilitate automated policy enforcement. Cost center tags improve resource tracking and financial accountability.

### Incident response mechanisms
<a name="incident-response-mechanisms.ee1f1d7e-3bd8-51db-9575-401e1e601d59"></a>

Establishing incident response mechanisms helps to mitigate potential harm and keep deployed gen AI models reliable. Address incidents as quickly as possible to minimize their impact on end users. These systems must also be designed for accessibility, so that response stakeholders and subject owners have immediate access to relevant information and resources.

### Feedback collection mechanisms
<a name="feedback-collection-mechanisms.1afcfa2f-3672-5cef-96bc-13ca97e427ca"></a>

The nondeterministic nature of gen AI models can still lead to unexpected behavior for your customers. Customer feedback serves as an early warning system, identifying hallucinations, biases, or harmful responses that automated quality metrics may miss. Incorporating feedback from diverse user groups helps organizations better understand model limitations and real-world data distributions. By systematically collecting, categorizing, and analyzing both positive and negative feedback, organizations can continuously refine their understanding of use cases, user values, and expectations.
