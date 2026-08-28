---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/reliability-design-principles.html
---

# Design principles
<a name="reliability-design-principles"></a>

In addition to the lens-level design principles, the reliability best practices in this lens are represented by at least one of the following principles:
+ **Decouple agents through durable messaging:** Persistence, retry, and dead-letter handling absorb transient failures inside the messaging layer instead of cascading them through synchronous call chains.
+ **Constrain blast radius through atomic responsibilities:** Single-task agents with the minimum permissions and clear instructions limit how far any individual failure or misbehavior can propagate.
+ **Recover from the last known good state, not the beginning:** Checkpointed workflows, idempotent steps, and graceful degradation let work resume after a fault rather than restart from scratch.
+ **Make multi-agent coordination resilient by design:** Arbiter patterns, capability taxonomies, and fallback paths keep collaborative workflows running when individual agents become unavailable or unreliable.
+ **Ground reasoning in verifiable evidence:** Retrieval from authoritative sources, explicit citation, and hallucination detection keep agent outputs traceable to real data instead of fabricated content.
+ **Exercise failure paths regularly:** Inject faults, run degraded-dependency tests, and rehearse recovery procedures. The first time a failure mode occurs should not be in production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
