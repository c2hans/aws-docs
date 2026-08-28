---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel02.html
---

# Network reliability
<a name="genrel02"></a>

| GENREL02: How do you maintain reliable communication among different components of your generative AI architecture? |
| --- |
|   |

Generative AI workloads often comprise several independent systems, including foundation models, databases, data processing pipelines, prompt catalogs, and APIs for agents. These systems communicate over a network and require reliable, secure, and performant connectivity.

**Topics**
+ [GENREL02-BP01 Implement redundant network connections among model endpoints and supporting infrastructure](genrel02-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
