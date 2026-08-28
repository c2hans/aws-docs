---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/delete-crdr-broker.html
---

# Deleting an Amazon MQ cross-Region data replication broker
<a name="delete-crdr-broker"></a>

 To delete a primary or replica cross-Region data replication (CRDR) broker, you must first unpair then reboot the brokers. The following instructions show how you can unpair and reboot the brokers using the AWS Management Console.

1.  On the **Brokers** page, select the CRDR broker you want to unpair, then choose **Edit**.

1.  On the broker **Edit** page in the **Data replication** section, choose **Unpair brokers**.

1.  Enter "confirm" in the pop-up window to confirm your choice. Then choose **Unpair brokers**.

1.  Next, reboot the unpaired primary broker. This will also reboot the replica broker. For instructions on rebooting your broker, see [Rebooting an Amazon MQ broker](amazon-mq-rebooting-broker.md). After the primary broker is rebooted, both brokers are unpaired and can be individually deleted. To delete your broker, see [Deleting an Amazon MQ broker](amazon-mq-deleting-broker.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
