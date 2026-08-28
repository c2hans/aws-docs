---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dns-failure-handling.html
---

# Handle connector creation failures
<a name="msk-connect-dns-failure-handling"></a>

This section describes possible connector creation failures associated with DNS resolution and suggested actions to resolve the issues.

| Failure | Suggested action |
| --- | --- |
| Connector creation fails if a DNS resolution query fails, or if DNS servers are unreachable from the connector. | You can see connector creation failures due to unsuccessful DNS resolution queries in your CloudWatch logs, if you've configured these logs for your connector.<br />Check the DNS server configurations and ensure network connectivity to the DNS servers from the connector. |
| If you change the DNS servers configuration in your VPC DHCP option set while a connector is running, DNS resolution queries from the connector can fail. If the DNS resolution fails, some of the connector tasks can enter a failed state. | You can see connector creation failures due to unsuccessful DNS resolution queries in your CloudWatch logs, if you've configured these logs for your connector.<br />The failed tasks should automatically restart to bring the connector back up. If that does not happen, you can contact support to restart the failed tasks for their connector or you can recreate the connector. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
