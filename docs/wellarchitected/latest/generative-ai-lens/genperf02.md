---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf02.html
---

# Maintaining model performance
<a name="genperf02"></a>

| GENPERF02: How do you verify your generative AI workload maintains acceptable performance levels? |
| --- |
|   |

 Foundation models are inherently non-deterministic. They introduce an element of randomness into systems. This randomness can be difficult to account for, especially when traditional performance evaluation techniques rely on a determinism. Furthermore, while they are flexible, broadly applicable, and capable performing multiple tasks, foundation models are compute-intensive resources that may require tuning and customization to meet your organization AI requirements.

 Developing a methodology for maintaining consistent model performance in a rapidly evolving environment of available models requires well-understood minimum performance thresholds, clear requirements for each model task, and a suite of remediation actions in the case of performance degradation or new model availability.

**Topics**
+ [GENPERF02-BP01 Load test model endpoints](genperf02-bp01.md)
+ [GENPERF02-BP02 Optimize inference parameters to improve response quality](genperf02-bp02.md)
+ [GENPERF02-BP03 Select and customize the appropriate model for your use case](genperf02-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
