---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/identity-tagging-controls.html
---

# Identity tagging controls
<a name="identity-tagging-controls"></a>

## Control objective
<a name="control-objective.ac66a8f3-6169-5b15-8cae-3075dae64d47"></a>

***Resource perimeter**** – My identities can access only trusted resources*

Control which resources can be accessed by identities based on principal and resource tags using IAM policies that implement attribute-based access control (ABAC).

### Tag-based resource access control
<a name="tag-based-resource-access-control"></a>

Grant data clearance levels to specific roles by attaching this IAM policy to roles that need restricted data access:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRestrictedDataAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/DataClassification": "Restricted",
          "aws:PrincipalTag/DataClearance": "Restricted"
        }
      }
    },
    {
      "Sid": "DenyRestrictedDataWithoutClearance",
      "Effect": "Deny",
      "Action": "s3:GetObject",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/DataClassification": "Restricted"
        },
        "StringNotEquals": {
          "aws:PrincipalTag/DataClearance": "Restricted"
        }
      }
    }
  ]
}
```

### Amazon Bedrock model access by classification
<a name="br-model-access-by-classification"></a>

Control access to different Amazon Bedrock models based on data classification tags:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowModelAccessByClassification",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalTag/DataClearance": "Restricted"
        },
        "ForAnyValue:StringLike": {
          "bedrock:modelId": [
            "anthropic.claude-3-sonnet*",
            "amazon.titan-text-express*"
          ]
        }
      }
    },
    {
      "Sid": "DenyHighValueModelsWithoutClearance",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalTag/DataClearance": "Restricted"
        },
        "ForAnyValue:StringLike": {
          "bedrock:modelId": [
            "anthropic.claude-3-opus*"
          ]
        }
      }
    }
  ]
}
```

**Policy explanation:**

**IAM policy (identity-based) characteristics:**
+ **Attached to** – IAM roles/users (controls what the role can do)
+ **Scope** – Applies to all resources the role tries to access
+ **Principal** – No principal field - applies to whoever assumes the role
+ **Enforcement** – Role-level permissions - defines what tagged principals can access
+ **Use case** – Granting data clearance levels to specific roles
+ **Perimeter** – Resource perimeter (controls which resources identities can access)

**Tag-based access patterns:**

1. **Principal tags** – `aws:PrincipalTag/DataClearance` defines the identity's clearance level

1. **Resource tags** – `s3:ExistingObjectTag/DataClassification` defines the resource's sensitivity

1. **Model restrictions** – `bedrock:modelId` controls access to specific AI models

1. **ABAC enforcement** – Both principal and resource tags must match for access

**Combined effect with resource-based policies:**

1. IAM policy grants permissions based on principal tags (resource perimeter)

1. Amazon S3 bucket policy enforces resource-level restrictions (identity perimeter)

1. Both must allow access for the operation to succeed

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
