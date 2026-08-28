---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp04.html
---

# GAMEPERF07-BP04 Regularly monitor networking performance
<a name="gameperf07-bp04"></a>

 For competitive games, it is important to have a consistent player experience.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-64"></a>

 A game that is reliably 50ms for a larger player base is fairer and more fun than a match where one player has 10ms ping and another who has 70ms ping. ISP routing changes may impact part of the player population, and your matchmaking system will need to adapt. [Amazon CloudWatch Network Monitoring](https://aws.amazon.com/cloudwatch/features/network-monitoring/) assists in determining whether the issue is with your game or the player internet provider.

### Implementation steps
<a name="implementation-steps-57"></a>
+  Use Amazon Cloudwatch Network Monitoring to track network performance and identify routing issues.
+  Use VPC Flow Logs to identify abnormal traffic patterns or dropped packets, which can indicate network congestion, ISP issues, or misconfigurations impacting player latency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
