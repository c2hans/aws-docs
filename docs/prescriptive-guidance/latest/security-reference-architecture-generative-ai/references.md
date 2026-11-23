---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/references.html
---

# References

For operational practices and cost governance, consult the [AWS Well-Architected Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html). This guide focuses on security decisions and their verification.
+ [AWS AI Security Framework](https://aws.amazon.com/blogs/security/the-aws-ai-security-framework-securing-ai-with-the-right-controls-at-the-right-layers-at-the-right-phases/), for use cases, security layers, and implementation phases.
+ [Multi-account security foundation](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html), for organization and shared account controls.
+ [Security in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html), for service-specific responsibilities and configuration.
+ [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/) and [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/), for architecture reviews.
+ [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/) and [Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/), for ownership and agency considerations.
+ [Security for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html), prescriptive guidance that provides practical security recommendations for developing [hosted agentic AI systems](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/agent-hosting-considerations.html) that follow the [perceive, react, act layer](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/generative-ai-agents.html) architecture.
+ [OWASP Top 10 for LLM Applications](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) and [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), for application risk scenarios and mapping of [OWASP Top 10 for LLM applications to AWS agentic AI service controls](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/owasp-top-ten.html).
+ [MITRE ATLAS](https://atlas.mitre.org/), for adversary techniques to consider in AI threat modeling.

## AWS AI Security Framework
<a name="aws-ai-security-framework"></a>

The [AWS AI Security Framework](https://aws.amazon.com/blogs/security/the-aws-ai-security-framework-securing-ai-with-the-right-controls-at-the-right-layers-at-the-right-phases/) organizes security controls by what an AI application can do, the security layers it needs, and the phases of implementation. Use this reference to map the architecture and controls from your review to the framework. The [introduction](https://dp8l2mfblnx2f.cloudfront.net/#how-to-use-this-guide) provides the reading path through the guide.

### Map the workload's behavior
<a name="map-the-workloads-behavior"></a>

|
|
| **What the application can do** | **Framework use case** | **Guidance in this guide** |
| --- |--- |--- |
| Generate a response from a model without external retrieval or tools | AI that answers | [Model inference](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/) and optional [model customization](https://dp8l2mfblnx2f.cloudfront.net/answers/model-customization/) |
| Retrieve enterprise information to ground model responses | AI that connects | [Data and knowledge bases](https://dp8l2mfblnx2f.cloudfront.net/connects/) |
| Use agents to choose tools, delegate tasks, or take actions | AI that acts | [Agentic AI and actions](https://dp8l2mfblnx2f.cloudfront.net/acts/), including [read-only tool access](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) |

These protections build on one another where the corresponding capability exists. A ticket-writing agent needs model controls and action authorization. If it also retrieves documents, it needs retrieval controls.

Classify the application by its capabilities. Applications using either [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) or [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) can generate answers, retrieve data, or drive actions. Model training introduces responsibilities for datasets and artifacts. Agent permissions introduce responsibilities for the operations an agent can perform.

Agent tool use, including Model Context Protocol (MCP) tools and Agent-to-Agent (A2A) interactions, belongs to AI that acts. Within that use case, distinguish read-only tools from tools that change systems. Both need authorization; changes also need approval and recovery controls appropriate to their consequences.

### Review three security layers
<a name="review-three-security-layers"></a>

Each component page uses the same three headings. Review all three for the services you deploy.

|
|
| **Framework layer** | **Design question** | **Example** |
| --- |--- |--- |
| Layer 1: Infrastructure security | Where does the workload run, and which network and execution boundaries contain it? | Restrict the application's network path to a model endpoint. |
| Layer 2: Identity and data security | Who may access the model, information, or tool? | Authorize retrieval against the requesting user's document permissions. |
| Layer 3: AI application security | How do you constrain and evaluate model-driven behavior? | Validate model output before displaying it or using it in a tool call. |

Governance and compliance span these layers. Identify the AI resources and data in use, apply the controls for their capabilities, and verify that those controls remain effective as the workload changes. Record a control owner, acceptance criteria, and test evidence for each relevant boundary. Enforce authorization independently of the model; a content filter does not grant permission to read data or perform an action.

### Use phases to plan improvements
<a name="use-phases-to-plan-improvements"></a>

The framework describes three implementation phases:
+ **Phase 1: Foundational.** Establish identity, access, and content controls while prototyping.
+ **Phase 2: Enhanced.** Add threat detection, data classification, and AI monitoring as the workload prepares for production.
+ **Phase 3: Advanced.** Automate governance, compliance, and response as the workload scales, and use operational findings to improve controls.

These phases organize the implementation plan. They do not replace a production risk decision. Data sensitivity or the consequences of an action can require a control earlier in the plan.

Keep one [implementation record](https://dp8l2mfblnx2f.cloudfront.net/conclusion/#implementation-record) that captures controls already in place, gaps, owners, and verification evidence. Use the framework phases to group the remaining work and plan improvements.

### Consult the scoping matrices when defining responsibility
<a name="consult-the-scoping-matrices-when-defining-responsibility"></a>

The scoping matrices help with a separate assessment question: how much of the application, model, data, and agent behavior does your organization control?
+ Use the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/) when defining responsibilities for a managed application, a pre-trained model, or a model you customize or train.
+ Add the [Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/) when defining an agent's authority and human oversight.

For example, an application using a pre-trained model can still have permission to issue refunds. The model ownership assessment and the refund authorization assessment address different boundaries. Record both, then apply the relevant service and action guidance.
