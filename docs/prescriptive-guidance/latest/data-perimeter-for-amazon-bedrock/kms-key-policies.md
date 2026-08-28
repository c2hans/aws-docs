---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/kms-key-policies.html
---

# AWS KMS key policies
<a name="kms-key-policies"></a>

## Control objective
<a name="control-objective.016f042c-3b4b-5d8d-bc94-3238e1ecc2ea"></a>

***Identity perimeter**** – Only trusted identities can access my resources*

AWS KMS key policies ensure only trusted identities can access encrypted resources. These policies complement other controls and act as a critical enforcement point for encrypted resources.

**Knowledge Base encryption architecture**

Amazon Bedrock Knowledge Bases encrypts data at multiple layers:
+ Amazon S3** documents** – Documents uploaded to Amazon S3 buckets (used by Knowledge Base data sources) can be encrypted with customer-managed AWS KMS keys
+ **Transient processing** – During data ingestion, Amazon Bedrock encrypts temporary data with a customer-managed key you specify
+ **Vector storage** – Amazon OpenSearch Serverless collections orAmazon S3 Vectors can use customer-managed keys
+ **Retrieval sessions** – `RetrieveAndGenerate `API calls can encrypt session context with a customer-managed key

### Knowledge Base Amazon S3 documents encryption key
<a name="knowledge-base-amazon-s3-documents-encryption-key"></a>

Apply the followingAWS KMS key policy to keys used for Amazon S3 buckets containing documents for Knowledge Base data sources:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "KMSAdminAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/KMSAdminRole"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "BedrockKnowledgeBaseAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012",
          "kms:ViaService": "s3.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "DocumentUploadRoleAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789012:role/KnowledgeBaseDocumentUploadRole",
          "arn:aws:iam::123456789012:role/DataIngestionRole"
        ]
      },
      "Action": [
        "kms:Encrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyExternalAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **KMSAdminAccess** – Grants full AWS KMS permissions to a dedicated administrative role rather than the account root. This follows the principle of least privilege by restricting key management to specific roles.
+ **BedrockKnowledgeBaseAccess** – Allows Amazon Bedrock service to decryptAmazon S3 objects for Knowledge Base operations. The condition restricts access to your account and ensures the request comes throughAmazon S3 , preventing direct key usage.
+ **DocumentUploadRoleAccess** – Grants specific IAM roles permission to encrypt documents when uploading to Amazon S3. Limited to encryption operations only, preventing these roles from accessing existing encrypted data.
+ **DenyExternalAccess** – Explicitly denies all access from principals outside your AWS organization. This creates an organizational boundary that prevents external access even if other conditions are met.

### Knowledge Base Data store transient data encryption key
<a name="knowledge-base-data-store-transient-data-encryption-key"></a>

Apply the following AWS KMS key policy to keys used for transient data storage during ingestion and retrieval sessions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "KMSAdminAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/KMSAdminRole"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "BedrockOperationsAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "DenyExternalAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    }
  ]
}
```

**Policy explanation:**

**KMSAdminAccess** – Provides administrative access to the AWS KMS key for the designated admin role, enabling key management operations while maintaining separation from operational access.

**BedrockOperationsAccess** – Grants Amazon Bedrock comprehensive key operations needed for transient data processing during ingestion and retrieval. Includes `CreateGrant` permission for delegating temporary access to other services.

**DenyExternalAccess** – Enforces organizational boundary by denying all operations from principals outside your AWS organization, regardless of other permissions.

### Knowledge Base vector store encryption key
<a name="knowledge-base-vector-store-encryption-key"></a>

Apply the following AWS KMS key policy to keys used for OpenSearch Serverless collections or S3 Vectors:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "KMSAdminAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/KMSAdminRole"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "OpenSearchServerlessAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "aoss.amazonaws.com"
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
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "S3VectorsAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
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
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "DenyExternalAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    }
  ]
}
```

#### Policy explanation
<a name="policy-explanation.90fd0ce6-05a9-50b4-aa6a-0eca03dac3f2"></a>
+ **KMSAdminAccess** – Provides full key management capabilities to the designated administrative role, ensuring centralized key governance while avoiding account root access.
+ **OpenSearchServerlessAccess** – Grants OpenSearch Serverless the encryption operations needed for vector storage. Scoped to your account to prevent cross-account access through the service.
+ **S3VectorsAccess** – Allows Amazon S3 service to perform encryption operations when using Amazon S3 as vector storage backend. Account-scoped to prevent unauthorized cross-account vector access.
+ **DenyExternalAccess** – Creates an organizational perimeter by explicitly denying all access from outside your AWS organization, providing defense-in-depth security.

### Model customization encryption
<a name="model-customization-encryption"></a>

Amazon Bedrock supports model customization through fine-tuning, continued pre-training, and distillation. These operations require access to training datasets stored in Amazon S3 buckets. Unlike Knowledge Base operations that only read documents, model customization jobs require additional AWS KMS permissions including `CreateGrant` to enable Amazon Bedrock to perform long-running training operations.

**Training data encryption key**

Apply the following AWS KMS key policy to keys used for Amazon S3 buckets containing model training datasets and fine-tuning data:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "KMSAdminAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/KMSAdminRole"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "BedrockTrainingAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012",
          "kms:ViaService": "s3.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "TrainingRoleAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789012:role/BedrockTrainingRole",
          "arn:aws:iam::123456789012:role/DataScientistRole"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyExternalAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    }
  ]
}
```

#### Policy explanation
<a name="policy-explanation.91d46be3-0ca5-5fdd-af66-2002ebefe151"></a>
+ **BedrockTrainingAccess** – Allows Amazon Bedrock to decrypt training data and create grants for long-running training jobs (via Amazon S3).
+ **TrainingRoleAccess** – Allows training and data science roles to encrypt/decrypt training datasets.
+ **DenyExternalAccess** – Blocks all access from principals outside the organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
