---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/resources.html
---

# Resources
<a name="resources"></a>

The primary reason for the existence of both AWS CloudFormation and Terraform is the creation and maintenance of cloud resources. But what exactly is a cloud resource? And are CloudFormation resources and Terraform resources the same thing? The answer is… yes and no. To illustrate this, this guide provides an example of using CloudFormation and then Terraform to create an Amazon Simple Storage Service (Amazon S3) bucket.

The following CloudFormation code example creates a sample Amazon S3 bucket.

```
{
    "myS3Bucket": {
        "Type": "AWS::S3::Bucket",
        "Properties": {
            "BucketName": "my-s3-bucket",
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "ServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": true,
                "BlockPublicPolicy": true,
                "IgnorePublicAcls": true,
                "RestrictPublicBuckets": true
            },
            "VersioningConfiguration": {
                "Status": "Enabled"
            }
        }
    }
}
```

The following Terraform code example creates an identical Amazon S3 bucket.

```
resource "aws_s3_bucket" "myS3Bucket" {
  bucket = "my-s3-bucket"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucketencryption" {
  bucket = aws_s3_bucket.myS3Bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "publicaccess" {
  bucket                  = aws_s3_bucket.myS3Bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.myS3Bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

For Terraform, a provider defines the resource, and then developers declare and configure those resources. Providers are a concept that this guide discusses in the next section. The Terraform example creates completely separate resources for several of the S3 bucket's settings. Creating separate resources for settings is not necessarily typical of how the Terraform AWS Provider treats AWS resources. However, this example shows an important distinction. While a CloudFormation resource is strictly defined by the [CloudFormation resource specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html), Terraform has no such requirement. In Terraform, the concept of a resource is a bit more nebulous.

Although the tools might differ regarding the exact guardrails that define what a single resource is, generally speaking, a *cloud resource* is any particular entity that exists in the cloud and that can be created, updated, or deleted. So regardless of how many resources are involved, the two previous examples both create the exact same thing with the exact same settings within an AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
