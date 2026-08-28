---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-instance-change-alarm.html
---

# Amazon MQ for RabbitMQ: Instance type change alarm
<a name="troubleshooting-action-required-instance-change-alarm"></a>

 `RABBITMQ_CLUSTER_DISK_USAGE_TOO_HIGH_FOR_INSTANCE_CHANGE` is an indication that a requested broker instance type change cannot proceed due to high disk usage on the current RabbitMQ node. Amazon MQ for RabbitMQ will raise this alarm when when the current disk usage exceeds what would be available on the requested instance type, as identified by the CloudWatch metric `RabbitMQDiskFree`.

 RabbitMQ brokers that enter `RABBITMQ_CLUSTER_DISK_USAGE_TOO_HIGH_FOR_INSTANCE_CHANGE` state will continue to be available for your applications, but the requested instance type change will not proceed. Amazon MQ allows broker restarts in this state, but you cannot change the instance type while the disk usage remains above the threshold for the requested instance type. The broker will return an exception for `ModifyBroker` API operations that attempt to change the instance type while in this state.

## Diagnosing and addressing instance type change alarm
<a name="w2aac40c27b7"></a>

 Amazon MQ enables metrics for your broker by default. You can view your broker metrics by accessing the CloudWatch console or by using the CloudWatch API. `MessageCount` and `RabbitMQDiskFree` metrics can be used to diagnose `RABBITMQ_CLUSTER_DISK_USAGE_TOO_HIGH_FOR_INSTANCE_CHANGE`.

 To resolve the quarantine state and allow your instance type change to proceed, use the Amazon MQ Management Console to:
+  Create a new connection to consume messages published to the queues.
+  Purge messages from queues.
+  Delete the queues from your broker.

**Note**
It may take up to several hours for the `RABBITMQ_CLUSTER_DISK_USAGE_TOO_HIGH_FOR_INSTANCE_CHANGE` status to clear after you take the required actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
