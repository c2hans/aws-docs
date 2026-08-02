---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/network-resource-access-controls.html
---

# Network resource access controls
<a name="network-resource-access-controls"></a>

## Control objective
<a name="control-objective.f8399713-22eb-5159-a748-355a418d3ca9"></a>

***Resource perimeter**** – Only trusted resources can be accessed from my network*

Prevent your network from accessing resources outside your trusted organizational boundary by implementing Amazon VPC endpoint policies that restrict access to resources within your AWS organization. This ensures that even if identities are compromised, network traffic can only reach approved resources.

**Amazon Bedrock VPC endpoint policy:**

Apply this policy to your Amazon Bedrock VPC endpoint to ensure only organizational resources can be accessed:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowApprovedModelsInTrustedOrg",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
        "arn:aws:bedrock:*::foundation-model/amazon.titan-text-express-v1"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-example123456"
        }
      }
    },
    {
      "Sid": "AllowModelListing",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "bedrock:GetFoundationModel",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-example123456"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowApprovedModelsInTrustedOrg** – Permits access only to specific approved models (Claude Sonnet, Titan Text Express) within your organization, blocking unauthorized foundation models
+ **AllowModelListing** – Allows listing and getting model information for organizational resources while maintaining the organizational boundary

### Amazon S3 VPC endpoint policy for AI data
<a name="s3-vpc-endpoint-policy-for-ai-data"></a>

Apply this policy to your Amazon S3 VPC endpoint to restrict access to training data and knowledge base documents:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTaggedBedrockBuckets",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::*",
        "arn:aws:s3:::*/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-example123456"
        },
        "ForAnyValue:StringEquals": {
          "aws:ResourceTag/Purpose": [
            "BedrockTraining",
            "BedrockKnowledgeBase"
          ]
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowTaggedBedrockBuckets** – Restricts access to Amazon S3 buckets within your organization that are tagged with `Purpose=BedrockTraining` or `Purpose=BedrockKnowledgeBase`, preventing access to unrelated Amazon S3 resources

### OpenSearch VPC endpoint policy
<a name="opensearch-vpc-endpoint-policy"></a>

Apply this policy to your OpenSearch VPC endpoint to restrict knowledge base vector storage access:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOpenSearchInTrustedOrg",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "es:ESHttpGet",
        "es:ESHttpPost",
        "es:ESHttpPut",
        "es:ESHttpDelete"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-example123456"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowOpenSearchInTrustedOrg** – Restricts OpenSearch access through VPC endpoints to clusters within your organization, preventing knowledge base queries from reaching external vector databases

**Important**
Replace `o-example123456` with your actual AWS organization ID. Find your organization ID using: `aws organizations describe-organization --query 'Organization.Id'`
