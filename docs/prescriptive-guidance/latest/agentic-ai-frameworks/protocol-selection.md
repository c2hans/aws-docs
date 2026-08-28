---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/protocol-selection.html
---

# Why protocol selection matters
<a name="protocol-selection"></a>

Protocol selection fundamentally shapes how you can build and evolve your AI agent architecture. By choosing protocols that support portability between agent frameworks, you gain the flexibility to combine different agent systems and workflows to meet your specific needs.

Open protocols enable you to integrate agents across multiple frameworks. For example, use LangChain for rapid prototyping and implement production systems with Strands Agents, communicating through a common protocol, such as MCP or the Agent2Agent (A2A) protocol. This flexibility reduces dependency on specific AI providers, simplifies integration with existing systems, and enables you to enhance agent capabilities over time.

Well-designed protocols also establish consistent security patterns for authentication and authorization across your agent ecosystem. Most importantly, protocol portability preserves your freedom to adopt new agent frameworks and capabilities as they emerge. Choosing open protocols protects your investment in agent development while maintaining interoperability with third-party systems.

## Advantages of open protocols
<a name="advantages-of-open-protocols.80a24122-ae4b-5815-884a-418198a62537"></a>

When implementing your own extensions or building custom agent systems, open protocols offer compelling advantages:
+ **Documentation and transparency** – Typically provide comprehensive documentation and transparent implementations
+ **Community support** – Access to broader developer communities for troubleshooting and best practices
+ **Interoperability guarantees** – Better assurance that your extensions will work across different implementations
+ **Future compatibility** – Reduced risk of breaking changes or deprecation
+ **Influence on development** – Opportunity to contribute to protocol evolution

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
