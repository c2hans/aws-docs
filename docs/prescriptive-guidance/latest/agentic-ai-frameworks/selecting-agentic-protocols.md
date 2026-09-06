---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/selecting-agentic-protocols.html
---

# Selecting agentic protocols
<a name="selecting-agentic-protocols"></a>

For most organizations building production agent systems, the Model Context Protocol (MCP) offers a comprehensive and well-supported foundation for agent-to-agent communication. MCP benefits from active development contributions from AWS and the open-source community.

Selecting the right agentic protocols is important for organizations looking to implement agentic AI effectively. Considerations differ based on organizational context.

## Agentic protocol selection considerations
<a name="agentic-protocol-selection-considerations.a89f891b-f3ae-5c58-aade-8944b017e0f3"></a>

Organizations should consider the following best practices when selecting protocols for agentic AI systems:
+ **Prioritize open standards** – Organizations should adopt open protocols such as the MCP to help ensure long-term interoperability, extensibility, and to reduce the risk of vendor lock-in.
+ **Balance speed and flexibility** – Startups and early adopters may begin with well-supported proprietary protocols for rapid development but should define a migration path to open standards as systems mature.
+ **Implement abstraction layers** – Enterprises should implement protocol abstraction to simplify migration, enable hybrid adoption, and future-proof integration strategies.
+ **Emphasize security and compliance** – Organizations in regulated industries should select protocols with robust authentication, encryption, and audit capabilities to meet governance and compliance requirements.
+ **Evaluate ecosystem maturity** – All organizations should assess the health, adoption, and community support of each protocol to ensure sustainability and minimize technical debt.
+ **Engage in standards development** – Organizations should participate in standards bodies or open-source communities to help shape protocol evolution and influence best practices.
+ **Account for data sovereignty** – Government and regulated sectors should ensure protocol choices align with data residency and sovereignty requirements across deployment regions.
+ **Leverage managed services** – Where possible, use managed or serverless implementations of agentic protocols to reduce operational complexity and accelerate deployment.
