---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/cross-service-integration-controls.html
---

# Cross-service integration controls
<a name="cross-service-integration-controls"></a>

## Control objective
<a name="control-objective.02310980-ea76-56e7-9d2e-da84a30e8c60"></a>

***Resource perimeter****: My identities can access only trusted resources*

Amazon Bedrock integrates with numerous AWS services, each requiring specific resource perimeter controls. To enforce least privilege, explicitly allow only the needed actions on specific resources by applying this IAM policy to Lambda execution roles used with Amazon Bedrock agents.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOnlyTrustedResources",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Query",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
        "arn:aws:dynamodb:us-east-1:123456789012:table/bedrock-agent-tableName",
        "arn:aws:s3:::bedrock-agent-data/prod/*"
      ]
    },
    {
      "Sid": "DenyExternalOrganizationAccess",
      "Effect": "Deny",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::*/*",
      "Condition": {
        "StringNotEquals": {
          "s3:ResourceOrgID": "o-1234567890"
        },
        "Null": {
          "s3:ResourceOrgID": "false"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedUploads",
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::bedrock-agent-data-*/*",
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
+ **AllowOnlyTrustedResources** – Grants Lambda functions access to specific Amazon Bedrock models, Amazon DynamoDB tables, and Amazon S3 buckets using resource-based restrictions. This statement implements least privilege by limiting access to only resources with the bedrock-agent-\* prefix, preventing access to unrelated resources in the account.
+ **DenyExternalOrganizationAccess** – Prevents data exfiltration by explicitly denying Amazon S3 access to any bucket outside your AWS organization. The condition checks for the organization ID and denies access when the bucket belongs to a different organization or has no organization ID set.
+ **DenyUnencryptedUploads** – Enforces encryption-in-transit by denying any Amazon S3 `PutObject` operation that doesn't use AWS KMS encryption. This ensures all data written to Amazon S3 by Lambda functions is encrypted with customer-managed keys.
