---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_instances-subnet.html
---

# Amazon EC2: Allows launching EC2 instances in a specific subnet, programmatically and in the console
<a name="reference_policies_examples_ec2_instances-subnet"></a>

This example shows how you might create an identity-based policy that allows listing information for all EC2 objects and launching EC2 instances in a specific subnet. This policy defines permissions for programmatic and console access. To use this policy, replace the {{italicized placeholder text}} in the example policy with your own information. Then, follow the directions in [create a policy](access_policies_create.md) or [edit a policy](access_policies_manage-edit.md).

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
                "ec2:Describe*",
                "ec2:GetConsole*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:{{*}}:{{*}}:subnet/subnet-{{subnet-id}}",
                "arn:aws:ec2:{{*}}:{{*}}:network-interface/*",
                "arn:aws:ec2:{{*}}:{{*}}:instance/*",
                "arn:aws:ec2:{{*}}:{{*}}:volume/*",
                "arn:aws:ec2:{{*}}::image/ami-*",
                "arn:aws:ec2:{{*}}:{{*}}:key-pair/*",
                "arn:aws:ec2:{{*}}:{{*}}:security-group/*"
            ]
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
