---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03.html
---

# Prompt remediation and recovery actions
<a name="genrel03"></a>

| GENREL03: How do you implement remediation actions for generative AI workload loops, retries, and failures? |
| --- |
|   |

 Generative AI workloads can be susceptible to logical loops, retries, and potentially even failures. Addressing these through the appropriate best practice helps to keeping your application reliable and improves user experience.

**Topics**
+ [GENREL03-BP01 Use logic to manage prompt flows and gracefully recover from failure](genrel03-bp01.md)
+ [GENREL03-BP02 Implement timeout mechanisms on agentic workflows](genrel03-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
