---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp05.html
---

# GAMEPERF06-BP05 Use monitoring and visualization tools
<a name="gameperf06-bp05"></a>

 Use monitoring and visualization tools to gain insights into your game server performance and identify optimization opportunities.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-60"></a>

 Use Amazon CloudWatch to monitor key metrics and set up alarms for proactive notifications. Utilize tools like Amazon Managed Service for Prometheus and Amazon Managed Grafana to collect, query, and visualize metrics from your game servers and infrastructure. Create informative dashboards to track performance, identify bottlenecks, and make data-driven optimizations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
