---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/performance-efficiency-design-principles.html
---

# Design principles
<a name="performance-efficiency-design-principles"></a>

In addition to the lens-level design principles, the performance efficiency best practices in this lens are represented by at least one of the following principles:
+ **Set targets per agent class, not per platform:** Streaming, task-oriented, and batch agents have different primary KPIs (time-to-first-token, completion time, throughput). Commit to the right ones for each class instead of a single platform-wide SLA.
+ **Design and tune the reasoning pipeline against the latency budget:** End-to-end latency is the sum of inference, retrieval, tool calls, and handoffs. Profile where time actually goes, allocate per-phase budgets, and optimize the proven critical path rather than the assumed one.
+ **Move work off the synchronous path:** Asynchronous messaging, streaming responses, parallel tool invocation, and event-driven coordination decouple user-perceived latency from total work performed.
+ **Tier memory and retrieval to access patterns:** Hot context near the agent, warm in nearby caches, cold in durable stores. Retrieval cost (latency, compute, tokens) should match the recency and frequency of access, not the maximum.
+ **Isolate tenants without serializing them:** Multitenant agent platforms need per-tenant throttling, quotas, and capacity reservations so heavy workloads cannot starve neighbors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
