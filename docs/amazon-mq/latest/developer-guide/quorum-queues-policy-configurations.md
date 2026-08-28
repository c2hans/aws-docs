---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues-policy-configurations.html
---

# Policy configurations for quorum queues for Amazon MQ for RabbitMQ
<a name="quorum-queues-policy-configurations"></a>

You can add specific policy configurations to quorum queues for your RabbitMQ broker on Amazon MQ.

 When you create a policy for quorum queues, you must do the following:
+ Remove all policy attributes that start with `ha`, such as `ha-mode`, `ha-params`, `ha-sync-mode`, `ha-sync-batch-size`, `ha-promote-on-shutdown`, and `ha-promote-on-failure`.
+ Remove `queue-mode`.
+  Change overflow when it is set to `reject-publish-dlx`

**Important**
 Amazon MQ for RabbitMQ applies all or none of the attributes within a policy. You cannot create a policy that applies to both classic mirrored queues and quorum queues. If you want your policy to only apply to quorum queues, you must set `--apply-to` to `quorum_queues`. If you are using classic mirrored queues and quorum queues, you must create a separate policy with `--apply-to`:`classic_queues` as well as a quorum queues policy.

You do not need to modify `AWS-DEFAULT` policies because they automatically adopt the new queue type in the “applies to” parameter. For more information on default policies for Amazon MQ for RabbitMQ, see [Configuring operator policies](configurable-values.md#configuring-operator-policies).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
