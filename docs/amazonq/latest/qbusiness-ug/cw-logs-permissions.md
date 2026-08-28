---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cw-logs-permissions.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Permissions for monitoring Amazon Q Business with Amazon CloudWatch Logs
<a name="cw-logs-permissions"></a>

To set up Amazon CloudWatch Logs for Amazon Q Business, use the following IAM policy to grant the necessary permissions.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchLogsDeliveryPermissions",
            "Effect": "Allow",
            "Action": "logs:CreateDelivery",
            "Resource": [
                "arn:aws:logs:us-east-1:111122223333:delivery-source:*",
                "arn:aws:logs:us-east-1:111122223333:delivery:*",
                "arn:aws:logs:us-east-1:111122223333:delivery-destination:*"
            ]
        },
        {
            "Sid": "QBusinessLogDeliveryPermissions",
            "Effect": "Allow",
            "Action": "qbusiness:AllowVendedLogDeliveryForResource",
            "Resource": [
                "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}"
            ]
        }
    ]
}
```

------

For example IAM policies with all the required permissions for your specific logging destination, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
