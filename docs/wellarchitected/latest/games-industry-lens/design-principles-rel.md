---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/design-principles-rel.html
---

# Design principles
<a name="design-principles-rel"></a>

 In addition to the design principles in the AWS Well-Architected Framework whitepaper, the following are design principles that can increase reliability in the cloud for games workloads:
+  **Establish the baseline for the peak player concurrency and system scalability targets required to meet business projections:** Prior to launching a game and during live game operations, develop estimates for the number of concurrent players expected at peak to establish target goals for system scalability to meet these projections. This assists creating a baseline for your game's reliability. Define scaling policies to accommodate changes in demand automatically without impact availability by verifying that your scaling systems gracefully manage active player sessions.
+  **Measure your reliability and the impact on player experience:** Define key performance indicators (KPIs) that represent the health of your game. Monitor the impact of changes in infrastructure and game features on your reliability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
