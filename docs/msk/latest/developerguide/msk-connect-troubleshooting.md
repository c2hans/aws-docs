---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-troubleshooting.html
---

# Troubleshoot issues in Amazon MSK Connect
<a name="msk-connect-troubleshooting"></a>

The following information can help you troubleshoot problems that you might have while using MSK Connect. You can also post your issue to the [AWS re:Post](https://repost.aws/).

**Connector is unable to access resources hosted on the public internet**
See [Enabling internet access for Amazon MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access.html).

**Connector's number of running tasks is not equal to the number of tasks specified in tasks.max**
Here are some reasons a connector may use fewer tasks than the specified tasks.max configuration:
+ Some connector implementations limit the number of tasks the can be used. For example, the Debezium connector for MySQL is limited to using a single task.
+ When using autoscaled capacity mode, Amazon MSK Connect overrides a connector's tasks.max property with a value that is proportional to the number of workers running in the connector and the number of MCUs per worker. If you have configured the optional `maxAutoscalingTaskCount` parameter, the `tasks.max` value will not exceed this limit. For more information, see [Understand maximum autoscaling task count](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html#msk-connect-max-autoscaling-task-count).
+ For sink connectors, the level of parallelism (number of tasks) cannot be more than the number of topic partitions. While you can set the tasks.max larger than that, a single partition is never processed by more than a single task at a time.
+ In Kafka Connect 2.7.x, the default consumer partition assignor is `RangeAssignor`. The behavior of this assignor is to give the first partition of every topic to a single consumer, the second partition of every topic to a single consumer, etc. This means that the maximum number of active tasks for a sink connector using `RangeAssignor` is equal to the maximum number of partitions in any single topic being consumed. If this doesn't work for your use case, you should [create a Worker Configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html#msk-connect-create-custom-worker-config) in which the `consumer.partition.assignment.strategy` property is set to a more suitable consumer partition assignor. See [Kafka 2.7 Interface ConsumerPartitionAssignor: *All Known Implementing Classes*](https://kafka.apache.org/27/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
