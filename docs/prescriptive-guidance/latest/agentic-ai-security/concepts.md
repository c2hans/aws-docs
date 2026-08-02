---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/concepts.html
---

# Key security concepts for agentic AI on AWS
<a name="concepts"></a>

By understanding the key functions within each agent, you can understand how to address the range of threats to it. An individual agent's function can be divided into three aspects: [perceive, reason, act](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/perceive-reason-act.html). This process is the cognitive cycle that is at the core of every agent's autonomous operation.

Securing agentic AI systems requires a hybrid approach that combines traditional distributed systems practices with AI-specific mitigations across the perceive, reason, and act layers. The perception and action layers can largely rely on conventional security frameworks that were developed for microservices architectures, including strong application, data, infrastructure, and operational controls. However, the reasoning layer introduces unique challenges due to the probabilistic nature of AI decision-making. It demands specialized threat-mitigation strategies. This architectural similarity to modern microservices helps organizations to use existing security frameworks to address the distinct risks introduced by agentic AI systems.

The comprehensive security posture for agentic AI systems must acknowledge that, unlike deterministic systems that produce consistent outputs, AI components exhibit probabilistic behavior. This creates new attack vectors and requires enhanced threat modeling that incorporates both traditional distributed system risks and emerging AI-specific threats, as outlined in the [OWASP Top Ten for LLM Applications](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/). Success depends on implementing defense-in-depth strategies across all three layers. This strategy should assume potential compromise at any level, and it should maintain operational effectiveness. This helps you implement security controls that are proportionate to the unique risks each layer presents while preserving the system's ability to achieve its intended goals through AI-driven reasoning and coordination.

This section includes the following topics:
+ [Threats at the perception layer](#concepts-perception)
+ [Threats at the reasoning layer](#concepts-reasoning)
+ [Threats at the act layer](#concepts-act)

## Threats at the perception layer
<a name="concepts-perception"></a>

The perception layer serves as the primary interface for data ingestion and interpretation. It processes diverse inputs, including user prompts, documents, sensor data, API responses, and inter-agent communications. This layer's role in forming the agent's worldview makes it a high-value target for adversaries who seek to influence system behavior through data manipulation.

Primary threat vectors include:
+ *Data poisoning*, where inputs are subtly modified to bias reasoning processes
+ *Prompt injection attacks*, where malicious instructions are concealed within seemingly benign data sources

The expanding diversity of data sources compounds the challenge of maintaining input integrity and provenance tracking.

## Threats at the reasoning layer
<a name="concepts-reasoning"></a>

The reasoning layer represents the cognitive core of agentic AI systems. It consolidates planning, knowledge retrieval, decision-making, and memory management functions. Its central role in system decision-making makes compromise of this layer particularly damaging because it can undermine the integrity of the entire system.

Critical threats include:
+ Input and context manipulation through information flooding attacks
+ *Logic manipulation* that exploits agent biases toward efficiency or urgency
+ *Memory poisoning* that introduces persistent false data or policies
+ *Multi-agent collusion scenarios*, where spoofed communications disrupt coordination or propagate misinformation across the system.

For greater outcome control, the reasoning layer should have focused goals rather than broad decision-making capability. [Amazon Bedrock guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html) provide automated reasoning validation capabilities. They can cross-check outputs against predefined policies and domain knowledge to support detection of anomalous behavior.

## Threats at the act layer
<a name="concepts-act"></a>

The act layer translates reasoning outputs into concrete system interactions through API calls, database updates, and infrastructure changes. This layer presents the highest operational risk because security failures directly impact production systems and sensitive data through legitimate agent capabilities.

Key risk areas include:
+ *Tool misuse*, where adversaries use legitimate agent capabilities for unauthorized operations
+ *Privilege compromise* through credential exposure or misconfiguration
+ *Cascading failures*, where single compromised actions propagate across interconnected agent networks and dependent services
