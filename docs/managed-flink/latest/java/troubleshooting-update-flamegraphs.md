---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-update-flamegraphs.html
---

# Apache Flink Flame Graphs
<a name="troubleshooting-update-flamegraphs"></a>

Flame Graphs are enabled by default on applications in Managed Service for Apache Flink versions that support it. Flame Graphs may affect application performance if you keep the graph open, as mentioned in [Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15//docs/ops/debugging/flame_graphs/).

 If you want to disable Flame Graphs for your application, create a case to request it to be disabled for your application ARN. For more information, see the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
