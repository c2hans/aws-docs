---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/organizations_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
<a name="organizations_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section"></a>

The following code example shows how to This permission-based policy grant full access to Compute Optimizer Automation for standalone AWS accounts

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
               "aco-automation:*",
            "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

------
