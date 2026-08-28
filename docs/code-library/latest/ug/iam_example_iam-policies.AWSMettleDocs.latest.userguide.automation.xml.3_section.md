---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
<a name="iam_example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
