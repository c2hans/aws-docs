---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-iam-policies.html
---

# S3 Vectors identity-based policy examples
<a name="s3-vectors-iam-policies"></a>

IAM identity-based policies are JSON documents that you attach to IAM users, groups, or roles to define what actions they can perform on S3 Vectors resources. These policies are evaluated in the context of the identity making the request and provide a centralized way to manage permissions across your AWS environment. Identity-based policies provide a clear audit trail of who has what permissions and can be easily modified as your access requirements evolve.

When designing identity-based policies for S3 Vectors, consider the different types of users and applications that will interact with your vector data. Common patterns include data scientists who need to query vectors, data engineers who need to load and manage vector data, administrators who need full control over bucket configuration, and applications that need specific read or write access to particular vector indexes.

## Example policies
<a name="s3-vectors-iam-policies-examples"></a>

### Administrative access policy
<a name="s3-vectors-iam-policies-admin"></a>

This policy provides full administrative access to S3 Vectors resources, suitable for platform administrators or DevOps teams:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAdministrativeAccess",
            "Effect": "Allow",
            "Action": [
                "s3vectors:CreateVectorBucket",
                "s3vectors:PutVectorBucketPolicy",
                "s3vectors:DeleteVectorBucket",
                "s3vectors:DeleteVectorBucketPolicy",
                "s3vectors:GetVectorBucket",
                "s3vectors:GetVectorBucketPolicy",
                "s3vectors:ListVectorBuckets",
                "s3vectors:CreateIndex",
                "s3vectors:DeleteIndex",
                "s3vectors:GetIndex",
                "s3vectors:ListIndexes",
                "s3vectors:DeleteVectors",
                "s3vectors:GetVectors",
                "s3vectors:ListVectors",
                "s3vectors:PutVectors",
                "s3vectors:QueryVectors"
            ],
            "Resource": "*"
        }
    ]
}
```

### Application-specific access policy
<a name="s3-vectors-iam-policies-app"></a>

This policy is designed for applications that need to perform specific operations on designated vector indexes:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowApplicationVectorAccess",
            "Effect": "Allow",
            "Action": [
                "s3vectors:QueryVectors",
                "s3vectors:GetVectors",
                "s3vectors:PutVectors",
                "s3vectors:ListVectors"
            ],
            "Resource": [
                "arn:aws:s3vectors:{{{{aws-region}}}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}/index/product-recommendations",
                "arn:aws:s3vectors:{{{{aws-region}}}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}/index/content-similarity"
            ]
        },
        {
            "Sid": "AllowGetIndex",
            "Effect": "Allow",
            "Action": "s3vectors:GetIndex",
            "Resource": "arn:aws:s3vectors:{{{{aws-region}}}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}/index/*"
        },
        {
            "Sid": "AllowIndexInspection",
            "Effect": "Allow",
            "Action": "s3vectors:ListIndexes",
            "Resource": "arn:aws:s3vectors:{{{{aws-region}}}}:{{123456789012}}:bucket/{{amzn-s3-demo-vector-bucket}}"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
