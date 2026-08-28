---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NW-permissions.html
---

# IAM permissions for Network Synthetic Monitor
<a name="CloudWatch-NW-permissions"></a>

To use Network Synthetic Monitor users must have the correct permissions.

For more information about security in Amazon CloudWatch, see [Identity and access management for Amazon CloudWatch](auth-and-access-control-cw.md).

## Permissions required to view a monitor
<a name="CloudWatch-IM-permissions.ViewMonitor"></a>

To view a monitor for Network Synthetic Monitor in the AWS Management Console, you must be signed in as a user or role that has the following permissions:

------
#### [ JSON ]

****

```
{
"Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData",
                "networkmonitor:Get*",
                "networkmonitor:List*"
                ],
            "Resource": "*"
        }
    ]
}
```

------

## Permissions required to create a monitor
<a name="CloudWatch-NW-permissions.CreateMonitor"></a>

To create a monitor in Network Synthetic Monitor, users must have permission to create a service-linked role that is associated with Network Synthetic Monitor. To learn more about the service-linked role, see [Using a service-linked role for Network Synthetic Monitor](monitoring-using-service-linked-roles-nw.md).

To create a monitor for Network Synthetic Monitor in the AWS Management Console, you must be signed in as a user or role that has the permissions included in the following policy.

**Note**
If you create an identity-based permissions policy that is more restrictive, users with that policy won't be able to create a monitor.

------
#### [ JSON ]

****

```
{
"Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "networkmonitor:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/networkmonitor.amazonaws.com/AWSServiceRoleForNetworkMonitor",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "networkmonitor.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:GetRole",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/networkmonitor.amazonaws.com/AWSServiceRoleForNetworkMonitor"
        },
        {
            "Action": [
                "ec2:CreateSecurityGroup",
                "ec2:CreateNetworkInterface",
                "ec2:CreateTags"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
