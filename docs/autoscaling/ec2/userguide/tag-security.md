---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/tag-security.html
---

# Tags for security
<a name="tag-security"></a>

Use tags to verify that the requester (such as an IAM user or role) has permissions to create, modify, or delete specific Auto Scaling groups. Provide tag information in the condition element of an IAM policy by using one or more of the following condition keys:
+ Use `autoscaling:ResourceTag/{{tag-key}}: {{tag-value}}` to allow (or deny) user actions on Auto Scaling groups with specific tags.
+ Use `aws:RequestTag/{{tag-key}}: {{tag-value}}` to require that a specific tag be present (or not present) in a request.
+ Use `aws:TagKeys [{{tag-key}}, ...]` to require that specific tag keys be present (or not present) in a request.

For example, you could deny access to all Auto Scaling groups that include a tag with the key `environment` and the value `production`, as shown in the following example.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:UpdateAutoScalingGroup",
                "autoscaling:DeleteAutoScalingGroup"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {"autoscaling:ResourceTag/{{environment}}": "{{production}}"}
            }
        }
    ]
}
```

------

For more information about using condition keys to control access to Auto Scaling groups, see [How Amazon EC2 Auto Scaling works with IAM](control-access-using-iam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
