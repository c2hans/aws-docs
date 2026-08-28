---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.10_section.html
---

# Allows the AWS Compute Optimizer Automation feature to apply recommended actions
<a name="iam_example_iam-policies.AWSMettleDocs.latest.userguide.managed-policies.xml.10_section"></a>

The following code example shows how to This permission-based policy allows the AWS Compute Optimizer Automation feature to apply recommended actions

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "aco-automation.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
