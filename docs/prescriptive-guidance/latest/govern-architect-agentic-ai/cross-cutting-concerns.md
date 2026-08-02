---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/cross-cutting-concerns.html
---

# Cross-layer concerns
<a name="cross-cutting-concerns"></a>

Observability and security span all layers of the agentic AI architecture, ensuring that AI operations are monitored, auditable, and compliant with enterprise policies. These foundational elements must be integrated throughout the entire system rather than treated as isolated components.

![Architecture diagram cross layer concerns](http://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/0719c216-63d8-4292-b66e-87ddf6dc22c4.png)

## Observability
<a name="observability"></a>

Comprehensive observability enables organizations to understand agent behavior, track performance, diagnose issues, and validate compliance across the complete agentic system through end-to-end request tracing across agents, LLMs, tools, and knowledge bases; performance monitoring of response times, success rates, and resource utilization; cost tracking with granular attribution to business units or applications; quality monitoring for response accuracy, hallucination rates, and guideline compliance; and usage analytics providing insights into adoption patterns and business value delivery.

Supporting infrastructure includes:
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) - observability providing out-of-the box monitoring and tracing of AgentCore services and support for export in OpenTelemetry format for interoperability with third-party observability solutions.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) - centralized metrics, logs, and alarms with custom dashboards for operational visibility
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) - advanced log analytics and visualization for complex pattern detection
+ Amazon EventBridge - event-driven alerting and response automation
+ [AWS Cost Explorer Service](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) - detailed cost allocation and management across all agentic AI infrastructure components including model inference, compute, storage, and data transfer

## Security
<a name="security"></a>

Comprehensive security ensures that agentic AI systems maintain:
+ Data protection, access control, compliance with regulations, and protection against AI-specific threats through identity and access management with proper authentication and authorization
+ Data protection safeguarding sensitive information in inputs, outputs, and knowledge bases
+ Prompt security preventing injection attacks and manipulation
+ Supply chain security validating models and dependencies
+ Network isolation controlling communication paths between components.

Supporting infrastructure includes:
+ [IAM](https://aws.amazon.com/iam/) and[ IAM Identity Center](https://aws.amazon.com/iam/identity-center/) - enterprise identity management with fine-grained access control and federated authentication
+ [Amazon BedrockGuardrails](https://aws.amazon.com/bedrock/guardrails/) - content filtering, topic constraints, and PII protection for model interactions
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Identity - Secure identity propagation across agent interactions and tool invocations
+ [AWS KMS key](https://aws.amazon.com/kms/)- encryption key management for data at rest and in transit
+ [Amazon Macie](https://aws.amazon.com/macie/) - automated discovery and protection of sensitive data in knowledge bases
+ [AWS WAF (Web Application Firewall)](https://aws.amazon.com/waf/) - protection against web-based attacks for exposed agent interfaces
+ [Amazon Virtual Private Cloud(VPC)](https://aws.amazon.com/vpc/) and [AWS PrivateLink](https://aws.amazon.com/privatelink/) - network isolation and private connectivity between components
+ [AWS Security Hub](https://aws.amazon.com/security-hub/) - centralized security posture management across the AI ecosystem
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) - comprehensive API activity logging for compliance and audit
