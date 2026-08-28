---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/knowledge-base-data-isolation.html
---

# Knowledge base data isolation
<a name="knowledge-base-data-isolation"></a>

## Control objective
<a name="control-objective.beeb268a-fe56-5dcf-a747-9602af69eec4"></a>

***Identity perimeter**** – Only trusted identities can access my resources*

Knowledge bases often contain the most sensitive organizational data. Only trusted identities can access knowledge base resources by establishing controls that restrict access to authorized services only.

For OpenSearch-backed knowledge bases, apply the following domain access policy to the OpenSearch domain resource:

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
      "Resource": "arn:aws:es:us-east-1:123456789012:domain/bedrock-knowledge-base/*"
    }
  ]
}
```

**Policy explanation:**
+ OpenSearch** domain access**: Restricts OpenSearch access to the Amazon Bedrock Knowledge Base role only

### Amazon S3 vector store access control
<a name="s3-vector-store-access-control"></a>

For Amazon S3-backed vector stores, control access through bucket policies that enforce organizational boundaries:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockKnowledgeBaseAccess",
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
      ]
    },
    {
      "Sid": "DenyExternalAccountAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::bedrock-vector-store-bucket",
        "arn:aws:s3:::bedrock-vector-store-bucket/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalAccount": "123456789012"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **Authorized service access** – Restricts Amazon S3bucket access to the designated Amazon Bedrock Knowledge Base role only
+ **Cross-account boundary** – Denies access from external AWS accounts

**Note**
For network-based access controls (VPC endpoint enforcement), see the [Network Perimeter](network-perimeter.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
