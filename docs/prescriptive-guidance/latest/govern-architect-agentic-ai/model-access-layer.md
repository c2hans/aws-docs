---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/model-access-layer.html
---

# Core services: model access
<a name="model-access-layer"></a>

Organizations must make a fundamental architectural decision regarding how agents access foundation models. This choice shapes security enforcement, operational governance, and the overall system architecture.

![Architecture diagram core services model access](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/d67af5cc-4c84-4325-aa12-ab2f7df11dfb.png)

Two primary patterns exist for model access, each with advantages and disadvantages:
+ Cloud native
+ LLM gateway

## Cloud native pattern
<a name="cloud-native-pattern.e21ae631-022c-53c4-89ef-2298d24991b9"></a>
+ Direct access to cloud provider model services
+ Native tool integrations and action frameworks deeply tied to cloud ecosystems
+ Managed identity and access management specific to each platform
+ Orchestration and memory management services optimized for cloud-native architectures
+ Enterprise-grade observability, security and governance features embedded in managed services

## LLM gateway pattern
<a name="llm-gateway-pattern.ff7522bb-ad37-50a7-b2e8-bb7629bce1d1"></a>
+ Unified API interfaces across multiple model providers through a controlled intermediary
+ Uniform and centralized policy enforcement across model providers for security and compliance
+ Consistent monitoring, cost management, and API normalization

### Decision factors
<a name="decision-factors"></a>

When choosing between these patterns, consider:
+ Governance maturity – organizations with strict compliance requirements or in highly regulated industries typically benefit from centralized control
+ Performance requirements – use cases requiring minimal latency may favor direct access
+ Multi-provider strategy – plans to use models from multiple providers benefit from the gateway's abstraction layer
+ Operational capacity – teams with limited resources may prefer cloud-native simplicity; those with established API management can leverage gateway benefits
+ Innovation velocity – direct access provides faster adoption of new model capabilities
+ Performance requirements – direct access avoids the additional routing layer latency introduced by gateways, though this overhead is often negligible compared to LLM inference time
+ Features of managed services - the rise of agentic AI and managed services (such as Amazon Bedrock Knowledge Bases) introduces platform-specific capabilities that are bringing value but are difficult to abstract

Organizations may also adopt a hybrid approach–implementing the gateway pattern for selected production applications while enabling cloud-native access for innovation workloads.

### AWS implementation approaches
<a name="aws-implementation-approaches"></a>

AWS supports both model access patterns through complementary services:

#### Cloud native pattern
<a name="cloud-native-pattern.57ea9b3c-18ec-578e-9445-68dd11601365"></a>
+ [Amazon Bedrock](https://aws.amazon.com/bedrock/) – managed foundation model service providing unified API access to multiple models with built-in guardrails, security controls, and enterprise features
+ [Amazon SageMaker](https://aws.amazon.com/sagemaker/) – platform for deploying and hosting custom or third-party models with full control over infrastructure and model serving

#### Gateway pattern
<a name="gateway-pattern.c677a545-2098-5306-b591-7c8e4ac4dfc6"></a>
+ [AWS Guidance for Multi-Provider Generative AI Gateway](https://aws.amazon.com/solutions/guidance/multi-provider-generative-ai-gateway-on-aws/) - reference architecture providing centralized access layer across [Amazon Bedrock](https://aws.amazon.com/bedrock/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), and third-party model providers with unified usage tracking, cost management, rate limiting, model routing, and governance controls

### Guardrails implementation
<a name="guardrails-implementation"></a>

Regardless of pattern, organizations must implement guardrails that filter inappropriate content, enforce compliance requirements, validate inputs and outputs to prevent prompt injection, and support domain-specific customization.

[Amazon BedrockGuardrails](https://aws.amazon.com/bedrock/guardrails/) provides managed capabilities for content filtering, denied topics, word filters, and sensitive information redaction.
