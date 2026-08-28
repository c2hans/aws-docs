---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/view-and-explore.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# View and explore discovered data
<a name="view-and-explore"></a>

Both Application Discovery Service Agentless Collector (Agentless Collector) and AWS Discovery Agent (Discovery Agent) provide system performance data based on average and peak utilization. You can use the system performance data that's collected to perform a high-level total cost of ownership (TCO). Discovery Agents collect more detailed data including time series data for system performance information, inbound and outbound network connections, and processes running on the server. You can use this data to understand network dependencies between servers and group the related servers as applications for migration planning.

In this section you'll find instructions on how to view and work with data discovered by Agentless Collector and Discovery Agent from both the console and the AWS CLI.

**Topics**
+ [View collected data using the Migration Hub console](view-data.md)
+ [Exploring data in Amazon Athena](explore-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
