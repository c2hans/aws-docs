---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles-start-vej-perms.html
---

# `StartVectorEnrichmentJob` API: Execution role permissions
<a name="sagemaker-roles-start-vej-perms"></a>

For an execution role that you can pass in a `StartVectorEnrichmentJob` API request, you can attach the following minimum permissions policy to the role:

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
                "s3:AbortMultipartUpload",
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::*SageMaker*",
                "arn:aws:s3:::*Sagemaker*",
                "arn:aws:s3:::*sagemaker*"
            ]
        },
        {
        "Effect": "Allow",
        "Action": "sagemaker-geospatial:GetVectorEnrichmentJob",
        "Resource":  "arn:aws:sagemaker-geospatial:*:*:vector-enrichment-job/*"
        }
    ]
    }
```

------

If your input Amazon S3 bucket is encrypted using server-side encryption with an AWS KMS managed key (SSE-KMS), see [Using Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
