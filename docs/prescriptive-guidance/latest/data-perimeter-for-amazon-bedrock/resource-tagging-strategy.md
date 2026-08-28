---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/resource-tagging-strategy.html
---

# Resource tagging strategy
<a name="resource-tagging-strategy"></a>

## Control objective
<a name="control-objective.829f4f54-3f8d-5a43-916e-fce484660204"></a>

***Resource perimeter**** – My identities can access only trusted resources*

Implement a comprehensive tagging strategy to support resource perimeter controls. This example shows a recommended tag structure:

```
{
  "RequiredTags": {
    "DataClassification": ["Public", "Internal", "Confidential", "Restricted"],
    "Purpose": ["Training", "Inference", "KnowledgeBase", "Monitoring"],
    "Owner": ["TeamName"],
    "Environment": ["Development", "Staging", "Production"],
    "CostCenter": ["BusinessUnit"]
  }
}
```

**Tag-based access control example (S3 bucket policy):**

Control access to sensitive data based on resource and principal tags by applying this bucket policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictedDataAccess",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::bedrock-data-bucket/*",
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

This policy uses pure ABAC (attribute-based access control) - any principal tagged with `DataClearance=Restricted` can access objects tagged `DataClassification=Restricted`, without hardcoding specific role names.

**Note**
For identity-based tagging policies that control which resources identities can access, see [Identity tagging controls](identity-tagging-controls.md) in this section.

### Key characteristics of resource-based tagging policies
<a name="key-characteristics-of-resource-based-tagging-policies"></a>

**S3 Bucket Policy (Resource-based):**
+ **Attached to** – Amazon S3 bucket (controls who can access the bucket)
+ **Scope** – Only applies to that specific Amazon S3 bucket
+ **Principal** – Uses principal: "\*" to apply to all callers
+ **Enforcement** – Bucket-level protection - even if IAM allows access, bucket policy can deny
+ **Use case** – Protecting specific data repositories from unauthorized access
+ **Perimeter** – Identity perimeter (controls which identities can access resources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
