---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/customer-managed-vendor.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Custom Policies for Migration Tools when using AWS Migration Hub
<a name="customer-managed-vendor"></a>

This is an example role for use by a integrated partner or developer when using the AWS Migration Hub API or CLI.

## Integrated Partner Role Policy
<a name="customer-managed-vendor-role"></a>

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "mgh:CreateProgressUpdateStream"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:mgh:us-west-2:{{111122223333}}:progressUpdateStream/vendor_name"
        },
        {
            "Action": [
                "mgh:AssociateCreatedArtifact",
                "mgh:DescribeMigrationTask",
                "mgh:DisassociateCreatedArtifact",
                "mgh:ImportMigrationTask",
                "mgh:ListCreatedArtifacts",
                "mgh:NotifyMigrationTaskState",
                "mgh:PutResourceAttributes",
                "mgh:NotifyApplicationState",
                "mgh:DescribeApplicationState",
                "mgh:AssociateDiscoveredResource",
                "mgh:DisassociateDiscoveredResource",
                "mgh:ListDiscoveredResources"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:mgh:us-west-2:{{111122223333}}:progressUpdateStream/vendor_name/*"
        },
        {
            "Action": [
                "mgh:ListMigrationTasks",
                "mgh:GetHomeRegion"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

## Integrated Partner Policy Trust Policy
<a name="customer-managed-vendor-trust"></a>

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
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
