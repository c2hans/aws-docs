---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section.html
---

# Policy to grant full access to Compute Optimizer Automation for a management account of an organization
<a name="example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.5_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Organizations with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
