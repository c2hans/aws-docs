---
source_url: https://docs.aws.amazon.com/partner-central/latest/crm/s3-iam-perms.html
---

# Setting Amazon S3 permissions for the IAM user
<a name="s3-iam-perms"></a>

The IAM user created for an AWS Marketplace configuration must have permissions to interact with Amazon S3. The Amazon S3 policy shown below grants the IAM user permission to view a bucket, list its contents, upload objects to the bucket, and generate pre-signed URLs for objects in the bucket. The connector requires these permissions because it must upload a custom EULA to an Amazon S3 bucket and generate a pre-signed URL to pass to the AWS Marketplace Catalog API.

The following policy uses the ${amzn-s3-demo-bucket} fictitious name. Replace it with the name of the your bucket, then attach the policy to your IAM user.

------
#### [ JSON ]

****

```
{
"Version":"2012-10-17",
          "Statement": [
                  {
                            "Sid": "S3ListBucket",
                           "Effect": "Allow",
                           "Action": [
                           "s3:ListBucket"
                           ],
                           "Resource": [
                                   "arn:aws:s3:::${amzn-s3-demo-bucket}"
                           ]
                  },
                  {
                            "Sid": "AllowS3PutObject",
                           "Effect": "Allow",
                           "Action": [
                           "s3:PutObject"
                           ],
                           "Resource": [
                           "arn:aws:s3:::${amzn-s3-demo-bucket}/"
                           ]
                  },
                  {
                            "Sid": "AllowCreatePresignedUrl",
                           "Effect": "Allow",
                           "Action": [
                           "s3:PutObject",
                           "s3:PutObjectAcl",
                           "s3:GetObject",
                           "s3:GetObjectAcl"
                           ],
                           "Resource": [
                           "arn:aws:s3:::${amzn-s3-demo-bucket}/"
                           ]
                  }
         ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
