---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/cost-optimization-design-principles.html
---

# Design principles
<a name="cost-optimization-design-principles"></a>

In addition to the lens-level design principles, the cost optimization best practices in this lens are represented by at least one of the following principles:
+ **Pay only for the reasoning the task requires:** Match model class, context length, and reasoning depth to task complexity instead of provisioning the largest model and longest context for the worst case.
+ **Enforce consumption ceilings at every layer:** Token budgets, iteration limits, time bounds, and concurrency caps live as policy at the gateway, runtime, and orchestration tiers so unbounded execution is rejected at the boundary rather than paid for and discovered later.
+ **Reuse before you recompute:** Caching of prompts, tool results, retrievals, and intermediate state turns repeat work into lookups. Inference is the most expensive operation in the system; build the architecture around that fact.
+ **Attribute spend to the unit that drives it:** Tag every invocation with agent, tenant, session, and workflow so reporting moves from infrastructure-level to per-decision accounting and over-provisioned components become visible.
+ **Close the loop between cost data and architecture:** Cost telemetry feeds back into model selection, prompt design, and orchestration choices on a regular cadence. Optimization is continuous, not a one-time review.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
