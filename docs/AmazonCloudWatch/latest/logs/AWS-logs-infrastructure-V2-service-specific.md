---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-service-specific.html
---

# Service-specific permissions
<a name="AWS-logs-infrastructure-V2-service-specific"></a>

In addition to the destination-specific permissions listed in the previous sections, some services require explicit authorization that customers are allowed to send logs from their resources, as an additional layer of security. It authorizes the `AllowVendedLogDeliveryForResource` action for resources that vend logs within that service. For these services, use the following policy and replace {{service}} and {{resource-type}} with the appropriate values. For the service-specific values for these fields, see those services' documentation page for vended logs. In the following example, the policy has been updated to enable vended logs from Amazon SES.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "ServiceLevelAccessForLogDelivery",
            "Effect": "Allow",
            "Action": [
                "{{ses}}:AllowVendedLogDeliveryForResource"
            ],
            "Resource": "arn:aws:{{ses}}:{{us-east-1}}:{{123456789012}}:{{resource-type}}/*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
