---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp03.html
---

# GAMEPERF06-BP03 Enable efficient log formatting and batching
<a name="gameperf06-bp03"></a>

 Configure your game server processes to generate logs in a structured and in a format that can be parsed, such as JSON.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-58"></a>

 Implement log batching techniques to minimize the frequency of log data transfers from your game servers to the centralized log storage. Batching logs reduces network overhead and improves game server performance. Use verbose or debug level logs as an exception and not a default, as they can incur a performance and cost penalty that should be avoided when possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
