---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/public/public-registry-settings-iam.html
---

# Required IAM permissions for Amazon ECR public registries
<a name="public-registry-settings-iam"></a>

When editing your Amazon ECR public registry settings, the IAM principal must have permission to call the `ecr-public:PutRegistryPolicy` API for registry-level operations.

**Note**
Setting a **Display name** for your Amazon ECR public registry doesn't require any additional permissions.

The following IAM policy can be added as an inline policy to the principal performing the public registry edit. Replace the example AWS account ID in this example with your own account ID.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ecr-public:PutRegistryCatalogData",
            "Resource": "arn:aws:ecr-public::{{123456789012}}:registry/*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
