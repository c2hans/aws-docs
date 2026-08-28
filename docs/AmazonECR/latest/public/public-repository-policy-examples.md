---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policy-examples.html
---

# Public repository policy examples in Amazon ECR Public
<a name="public-repository-policy-examples"></a>

The following examples show policy statements that you use to control the permissions that users have to your public repositories.

**Note**
All public repositories are visible on the Amazon ECR Public Gallery. Using a repository policy to deny access to view or pull from a public repository is not supported.

**Important**
Amazon ECR requires that users have permission to make calls to the `ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they can authenticate to a registry and push any images to an Amazon ECR repository.

## Example: Allow an IAM user within your account
<a name="IAM_within_account"></a>

The following repository policy allows users within your account to push images.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPush",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:user/{{push-pull-user-1}}",
                    "arn:aws:iam::{{111122223333}}:user/{{push-pull-user-2}}"
                ]
            },
            "Action": [
                "ecr-public:BatchCheckLayerAvailability",
                "ecr-public:PutImage",
                "ecr-public:InitiateLayerUpload",
                "ecr-public:UploadLayerPart",
                "ecr-public:CompleteLayerUpload"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Example: Allow another account
<a name="IAM_allow_other_accounts"></a>

The following repository policy allows a specific account to push images.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCrossAccountPush",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": [
                "ecr-public:BatchCheckLayerAvailability",
                "ecr-public:PutImage",
                "ecr-public:InitiateLayerUpload",
                "ecr-public:UploadLayerPart",
                "ecr-public:CompleteLayerUpload"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
