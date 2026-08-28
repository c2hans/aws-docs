---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/knowledge-base-network-controls.html
---

# Knowledge base network controls
<a name="knowledge-base-network-controls"></a>

## Control objective
<a name="control-objective.c390d2d2-91b0-5845-b740-ae521b5f050b"></a>

***Network perimeter**** – My resources can only be accessed from expected networks*

Knowledge base resources must enforce network-based access controls to ensure data access only occurs through approved network paths.

## OpenSearch domain network enforcement
<a name="9999999999999999opensearch--domain-network-enforcement.a3f3818b-efbd-5ff6-a4c3-d77456dbfef9"></a>

Apply the following resource-based policy to OpenSearch domains to enforce Amazon VPCendpoint access:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/BedrockKnowledgeBaseRole"
      },
      "Action": "es:*",
      "Resource": "arn:aws:es:us-east-1:123456789012:domain/bedrock-knowledge-base/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceVpce": "vpce-1234567890abcdef0"
        }
      }
    }
  ]
}
```

### Amazon S3 vector store network enforcement
<a name="amazon-s3-vector-store-network-enforcement"></a>

Apply this resource-based policy to Amazon S3 buckets containing vector store data:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowVPCEndpointAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/BedrockKnowledgeBaseRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::bedrock-vector-store-bucket",
        "arn:aws:s3:::bedrock-vector-store-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceVpce": "vpce-1234567890abcdef0"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **VPC endpoint enforcement** – Requires all knowledge base access through the specified Amazon VPC endpoint
+ **Network boundary** – Blocks direct internet access to knowledge base resources
+ **Private network access** – Ensures sensitive AI data flows only through trusted network paths

**Important**
Replace `vpce-1234567890abcdef0 `with your actual Amazon VPC endpoint ID for Amazon S3 and OpenSearch services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
