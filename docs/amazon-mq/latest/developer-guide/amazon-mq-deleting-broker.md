---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-deleting-broker.html
---

# Deleting an Amazon MQ broker
<a name="amazon-mq-deleting-broker"></a>

If you don't use an Amazon MQ broker (and don't foresee using it in the near future), it is a best practice to delete it from Amazon MQ to reduce your AWS costs.

The following example shows how you can delete a broker using the AWS Management Console.

## Deleting an Amazon MQ broker
<a name="deleting-broker-console"></a>

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/).

1. From the broker list, select your broker (for example, **MyBroker**) and then choose **Delete**.

1. In the **Delete {{MyBroker}}?** dialog box, type `delete` and then choose **Delete**.

   Deleting a broker takes about 5 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
