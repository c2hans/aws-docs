---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-kinesis.html
---

# Sending AWS Network Firewall logs to Amazon Data Firehose
<a name="logging-kinesis"></a>

To send logs to Amazon Data Firehose, you first need to set up a Firehose delivery stream. As part of that process, you choose a destination for storing your logs. After you enable logging for your firewall, AWS Network Firewall delivers logs to the destination through the HTTPS endpoint of Amazon Data Firehose. One AWS Network Firewall log corresponds to one Amazon Data Firehose record.

Configure an Amazon Data Firehose delivery stream for your firewall as follows.
+ Create it using the same account as you use to manage the firewall.
+ Create it in the same Region as the firewall.
+ Configure it for direct put, which allows applications to access the delivery stream directly. In the Amazon Data Firehose console, for the delivery stream **Source** setting, choose **Direct PUT or other sources**. Through the API, set the delivery stream property `DeliveryStreamType` to `DirectPut`.

For information about how to create an Amazon Data Firehose delivery stream and review the stored logs, see [Creating an Amazon Data Firehose delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) and [What is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

When you successfully enable logging to an Amazon Data Firehose data stream, Network Firewall creates a service linked role with the necessary permissions to write logs to it. For more information, see [Using service-linked roles](using-service-linked-roles.md).

## Permissions to publish logs to Amazon Data Firehose
<a name="logging-kinesis-permissions"></a>

You must have the following permissions to configure your firewall to send logs to an Amazon Data Firehose delivery stream.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:CreateLogDelivery",
                "logs:GetLogDelivery",
                "logs:UpdateLogDelivery",
                "logs:DeleteLogDelivery",
                "logs:ListLogDeliveries"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow",
            "Sid": "FirewallLogging"
        },
        {
            "Sid": "FirewallLoggingFH1",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Sid": "FirewallLoggingFH2",
            "Action": [
                "firehose:TagDeliveryStream"
            ],
            "Resource": "arn:aws:firehose:{{us-east-1}}:{{123456789012}}:deliverystream/{{delivery-stream-name}}",
            "Effect": "Allow"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
