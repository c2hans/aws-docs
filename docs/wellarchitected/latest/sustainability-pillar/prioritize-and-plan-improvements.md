---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/prioritize-and-plan-improvements.html
---

# Prioritize and plan improvements
<a name="prioritize-and-plan-improvements"></a>

 Prioritize your identified improvements based on the greatest anticipated impact with the lowest costs and acceptable risk.

 Decide which improvements to focus on initially, and include them in your resource planning and development roadmap.

 Applying this step to the [Example scenario](improvement-process.md#example-scenario), you prioritize the target improvements as follows:

|  **Priority**  |  **Improvement**  |  **Potential**  |  **Cost**  |  **Risk**  |
| --- | --- | --- | --- | --- |
|  1  |  Implement more effective compression mechanisms  |  High  |  Low  |  Low  |
|  2  |  Implement predictive scaling  |  Medium  |  Low  |  Low  |

 The high potential, low cost, and risk of updating file compression make it a high-value target for your company and a priority over implementing predictive scaling. You determine that implementing predictive scaling with its medium potential impact, low cost, and low risk should be the priority improvement after file compression is complete.

 You assign a team member to implement improved file compression and add predictive scaling to your backlog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
