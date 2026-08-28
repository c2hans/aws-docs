---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/appendix-sample-policies.html
---

# Appendix: Sample profile and role policies
<a name="appendix-sample-policies"></a>

## Sample policies for Application 1
<a name="appendix-sample-policies-app-1"></a>

The sample policy for **Profile 1** allows some actions for **Bucket 1** in Amazon Simple Storage Service (Amazon S3):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            ]
        }
    ]
}
```

The sample policy for **Role 1** allows the `DescribeInstances` action for an Amazon Elastic Compute Cloud (Amazon EC2) instance and allows some actions on **Bucket 1** and **Bucket 2** in Amazon S3:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances"
            ],
            "Resource": [
                "arn:aws:ec2:us-east-1:123456789012:instance/i-01234567890abcdef"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectLegalHold",
                "s3:PutObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            ]
        }
    ]
}
```

The **Profile 1** policy limits the permissions granted by the **Role 1** policy. It is applied to the role session when the role is assumed through IAM Roles Anywhere. An application that assumes **Role 1** has access to only **Bucket 1**. It cannot access **Bucket 2** or perform any Amazon EC2 actions because the **Profile 1 **policy doesn't grant these permissions.

## Sample policies for Application 2
<a name="appendix-sample-policies-app-2"></a>

The sample policy for **Profile 2** allows some actions for **Bucket 2** in Amazon S3:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            ]
        }
    ]
}
```

The sample policy for **Role 2** allows the `DescribeInstances` action for an Amazon EC2 instance and allows some actions on **Bucket 1** and **Bucket 2** in Amazon S3:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances"
            ],
            "Resource": [
                "arn:aws:ec2:us-east-1:567890123456:instance/i-05678901234ghijk"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectLegalHold",
                "s3:PutObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            ]
        }
    ]
}
```

The policy for **Profile 2** limits the permissions granted by **Role 2**. It is applied to the role session when the role is assumed through IAM Roles Anywhere. An application that assumes **Role 2** has access to only **Bucket 2**. It cannot access **Bucket 1** or perform Amazon EC2 actions because the **Profile 2 **policy doesn't grant these permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
