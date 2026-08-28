---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-what-changes.html
---

# What changes with Next generation Resilience Hub
<a name="next-gen-what-changes"></a>

Next generation Resilience Hub introduces a new application modeling hierarchy, GenAI-powered assessments, and automatic dependency discovery. This section summarizes the key changes.
+ **New hierarchy** – The v1 concept of an "application" maps to a "service" as the primary unit of assessment. Services are grouped within systems, and user journeys describe the paths through them.
+ **GenAI-powered failure mode assessments** – Static rule-based checks are replaced by generative AI analysis that produces detailed failure mode findings with reasoning specific to your architecture.
+ **Dependency discovery** – Next generation Resilience Hub automatically discovers dependencies between services and external resources, a capability not available in v1.
+ **Modular resilience policies** – Policies are now composable. You can combine disaster recovery (DR), availability SLO, and data recovery conditions in a single policy, rather than a single RTO/RPO pair.
+ **Full AWS Organizations integration** – Organization-wide governance from a single delegated administrator account replaces the limited multi-account support in v1.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
