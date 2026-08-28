---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-iam-access.html
---

# Controlling access using IAM
<a name="ce-iam-access"></a>

You can use AWS Identity and Access Management (IAM) to manage access to your Cost Management preferences for individual users. You can then grant or revoke access on an individual level for each IAM role or user. You’ll need to add the following actions in order to be able to view and edit preferences: `ce:GetPreferences`, `ce:UpdatePreferences`, `ce:GetDimensionValues`, and `ce:GetApproximateUsageRecords`.

The following is a sample IAM policy with the relevant actions that would provide you with access to view and edit your Cost Management preferences in order to enable multi-year and granular data:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ce:GetPreferences",
                "ce:UpdatePreferences",
                "ce:GetDimensionValues",
                "ce:GetApproximateUsageRecords"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
