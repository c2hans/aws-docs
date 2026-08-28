---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-FlinkKafkaConsumer.html
---

# FlinkKafkaConsumer issue with stop with savepoint
<a name="troubleshooting-FlinkKafkaConsumer"></a>

When using the legacy FlinkKafkaConsumer there is a possibility your application may get stuck in UPDATING, STOPPING or SCALING, if you have system snapshots enabled. There is no published fix available for this [issue](https://issues.apache.org/jira/browse/FLINK-28758), therefore we recommend you upgrade to the new [KafkaSource](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kafka/#kafka-source) to mitigate this issue.

If you are using the `FlinkKafkaConsumer` with snapshots enabled, there is a possibility when the Flink job processes a stop with savepoint API request, the `FlinkKafkaConsumer` can fail with a runtime error reporting a `ClosedException`. Under these conditions the Flink application becomes stuck, manifesting as Failed Checkpoints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
