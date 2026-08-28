---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp04.html
---

# GAMEPERF06-BP04 Implement log rotation and retention policies
<a name="gameperf06-bp04"></a>

 Establish log rotation and retention policies to manage the growth of log data and optimize storage utilization.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-59"></a>

 Configure your game servers to automatically rotate logs based on size or time intervals. Define log retention policies in Amazon CloudWatch Logs to automatically archive or delete older log data that is no longer needed for active analysis or troubleshooting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
