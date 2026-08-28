---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec02.html
---

# Response validation
<a name="gensec02"></a>

| GENSEC02: How do you stop generative AI applications from generating harmful, biased, or factually incorrect responses? |
| --- |
|   |

 It is possible for foundation models to generate harmful, biased, or factually incorrect responses, particularly when guardrails are not implemented appropriately or at all. This risk creates additional considerations for generative AI applications before they are put into a production environment. This question addresses the best practices associated with mitigating risk of harmful, biased or factually incorrect responses.

**Topics**
+ [GENSEC02-BP01 Implement guardrails to mitigate harmful or incorrect model responses](gensec02-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
