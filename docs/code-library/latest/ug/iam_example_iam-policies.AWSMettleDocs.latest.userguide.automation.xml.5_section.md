---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Policy to grant full access to Compute Optimizer Automation for a management account of an organization
<a name="iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section"></a>

The following code example shows how to This permission-based policy grants full access to Compute Optimizer Automation for a management account of an organization

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
               "ec2:DescribeVolumes",
               "organizations:ListAccounts",
               "organizations:DescribeOrganization",
               "organizations:DescribeAccount",
               "organizations:EnableAWSServiceAccess",
               "organizations:ListDelegatedAdministrators",
               "organizations:RegisterDelegatedAdministrator",
               "organizations:DeregisterDelegatedAdministrator"
            ],
            "Resource": "*"
        }
    ]
}
```

------
