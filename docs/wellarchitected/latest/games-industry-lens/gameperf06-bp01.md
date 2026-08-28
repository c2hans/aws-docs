---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp01.html
---

# GAMEPERF06-BP01 Centralize log collection and storage
<a name="gameperf06-bp01"></a>

 Implement a centralized log collection and storage solution to gather logs from game server instances and GameLift.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-56"></a>

 Use services like Amazon CloudWatch Logs to collect, monitor, and store log data from your game servers and GameLift instances. CloudWatch Logs provides a scalable and fully managed solution for log management, facilitating efficient storage and retrieval of log data without impacting game server performance. If you are running the [CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), consider the various install types and configuration options like batch size, buffer duration to minimize impact to the game server. Consider the game server instances ephemeral and reduce dependency on localized logging where possible. Establish a centralized policy for implementation of [Logging best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.html).

### Implementation steps
<a name="implementation-steps-55"></a>
+  Use Amazon CloudWatch Logs to collect, monitor, and store log data from game server instances and GameLift, facilitating centralized and scalable log management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
