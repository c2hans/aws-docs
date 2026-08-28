---
source_url: https://docs.aws.amazon.com/marketplace/latest/userguide/set-aws-iam-cas-permissions.html
---

# AWS Marketplace Commerce Analytics Service account permissions
<a name="set-aws-iam-cas-permissions"></a>

Use the following IAM permissions policy to enroll in the AWS Marketplace Commerce Analytics Service.

For instructions on how to enroll, follow the [onboarding guide](https://docs.aws.amazon.com/marketplace/latest/userguide/commerce-analytics-service.html#on-boarding-guide).

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
                "iam:ListRoles",
                "iam:CreateRole",
                "iam:CreatePolicy",
                "iam:AttachRolePolicy",
                "aws-marketplace-management:viewReports"
            ],
            "Resource": "*"
        }
    ]
}
```

------

Use the following IAM permissions policy to allow a user to make requests to the AWS Marketplace Commerce Analytics Service.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "marketplacecommerceanalytics:GenerateDataSet",
            "Resource": "*"
        }
    ]
}
```

------

For more information about this feature, see [Accessing product and customer data with the AWS Marketplace Commerce Analytics Service](commerce-analytics-service.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
