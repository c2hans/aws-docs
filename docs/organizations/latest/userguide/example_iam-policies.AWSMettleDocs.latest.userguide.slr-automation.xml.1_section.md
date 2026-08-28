---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section.html
---

# Policy to grants service-linked role permissions for Compute Optimization Automation
<a name="example_iam-policies.AWSMettleDocs.latest.userguide.slr-automation.xml.1_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Organizations with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
