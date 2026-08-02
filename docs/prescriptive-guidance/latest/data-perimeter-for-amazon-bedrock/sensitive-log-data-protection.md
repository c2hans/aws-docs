---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/sensitive-log-data-protection.html
---

# Sensitive log data protection
<a name="sensitive-log-data-protection"></a>

## Control objective
<a name="control-objective.50fff6f3-a5c8-585e-b70a-41df652b6e29"></a>

***Identity Perimeter**** – ****Only trusted identities can access my resources***

AI workloads generate logs that may contain sensitive prompts, responses, or model parameters. Only trusted identities can access log resources by applying the following resource policy to Amazon CloudWatch log groups containing Amazon Bedrock logs:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOrganizationRead",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "logs:DescribeLogStreams",
        "logs:GetLogEvents",
        "logs:FilterLogEvents"
      ],
      "Resource": "arn:aws:logs:*:123456789012:log-group:/aws/bedrock/*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowOrganizationRead** - Only organization members can read Amazon Bedrock logs

### AWS KMS key policy for CloudWatch Logs encryption
<a name="aws-kms-key-policy-for-cloud-watch-logs-encryption"></a>

Encrypt Amazon Bedrockmodel invocation logs and restrict decryption to organization members only:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnableRootAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogsAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "logs.us-east-1.amazonaws.com"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "ArnEquals": {
          "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/bedrock/*"
        }
      }
    },
    {
      "Sid": "OrganizationOnlyDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        }
      }
    ]
}
```

**Policy explanation:**
+ **EnableRootAccess** – Grants full AWS KMS permissions to the account root for key administration and management
+ **CloudWatchLogsAccess** – Allows CloudWatch Logs service to encrypt and decrypt log data, with encryption context ensuring the key is only used for Amazon Bedrock log groups
+ **OrganizationOnlyDecrypt** – Restricts decryption access to principals within your AWS organization, preventing external entities from reading encrypted log data
