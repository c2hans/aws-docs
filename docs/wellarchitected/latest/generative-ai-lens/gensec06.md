---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec06.html
---

# Data poisoning
<a name="gensec06"></a>

| GENSEC06: How do you detect and remediate data poisoning risks? |
| --- |
|   |

 Data poisoning is a type of exploit that can occur during model training or customization. This happens when data not meant for model training or customization is used for training or customization, resulting in potentially undesirable effects for the finished model. Data poisoning can be difficult to detect and can be challenging to remediate.

**Topics**
+ [GENSEC06-BP01 Implement data purification filters for model training workflows](gensec06-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
