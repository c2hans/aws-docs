---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel01.html
---

# Manage throughput quotas
<a name="genrel01"></a>

| GENREL01: How do you determine throughput quotas (or needs) for foundation models? |
| --- |
|   |

Foundation models perform complex tasks over detailed input, and they have limited throughput on the amount of inference requests they can service at a time. This is particularly true for managed and serverless model hosting paradigms. Understanding and managing these quotas is crucial for maintaining reliable service levels and optimal performance.

**Topics**
+ [GENREL01-BP01 Scale and balance foundation model throughput as a function of utilization](genrel01-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
