---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Policy to grants service-linked role permissions for Compute Optimization Automation
<a name="iam_example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section"></a>

The following code example shows how to This permission-based policy grants service-linked role permissions for Compute Optimization Automation

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        }
    ]
}
```

------
