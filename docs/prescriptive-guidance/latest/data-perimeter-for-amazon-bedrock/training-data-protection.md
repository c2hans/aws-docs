---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/training-data-protection.html
---

# Training data protection
<a name="training-data-protection"></a>

## Control objective
<a name="control-objective.6b63135d-ea06-5106-a7e5-ac373bee8622"></a>

***Identity perimeter****: Only trusted identities can access my resources*

Custom model training requires uploading datasets to Amazon S3. Only trusted identities can access training data resources by applying the following policy to Amazon S3 buckets containing training data.

**Important – **Replace placeholder values:
+ `o-1234567890` with your AWS organization ID
+ `123456789012` with your AWS account IDs
+ `bedrock-training-data-bucket` with your actual bucket names

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyExternalAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::bedrock-training-data-bucket/*",
        "arn:aws:s3:::bedrock-training-data-bucket"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    },
    {
      "Sid": "PreventDataExfiltration",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete"
      ],
      "Resource": "arn:aws:s3:::bedrock-training-data-bucket/*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **DenyExternalAccess** - Blocks all Amazon S3 operations from principals outside your organization
+ **PreventDataExfiltration** - Specifically denies replication operations that could be used to copy training data to external buckets

**Enhanced training data protection:**

For highly sensitive training datasets, require encryption and restrict access to specific roles:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnauthorizedRoles",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::sensitive-training-data/*",
      "Condition": {
        "ForAllValues:StringNotEquals": {
          "aws:PrincipalArn": [
            "arn:aws:iam::123456789012:role/BedrockTrainingRole",
            "arn:aws:iam::123456789012:role/DataScientistRole"
          ]
        }
      }
    },
    {
      "Sid": "EnforceSecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::sensitive-training-data",
        "arn:aws:s3:::sensitive-training-data/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::sensitive-training-data/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **DenyUnauthorizedRoles** – Explicitly denies access to sensitive training data for any principal that is not one of the designated training and data science roles
+ **EnforceSecureTransport** – Denies all Amazon S3 actions when secure transport (HTTPS) is not used
+ **DenyUnencryptedUploads** – Enforces AWS KMS encryption for all uploads

**Key protections:**
+ Organizational boundary prevents external access
+ Replication blocked to prevent data exfiltration
+ AWS KMS encryption required for uploads
+ HTTPS transport enforced
+ Access limited to specific IAM roles

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
