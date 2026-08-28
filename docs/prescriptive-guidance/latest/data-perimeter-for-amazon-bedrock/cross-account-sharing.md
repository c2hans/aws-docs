---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/cross-account-sharing.html
---

# Cross account sharing
<a name="cross-account-sharing"></a>

## Control objective
<a name="control-objective.c3787cd3-0c9c-5dc8-85cc-fcef8fbf14f6"></a>

***Identity perimeter**** – Only trusted identities can access my resources*

When sharing custom models across accounts, implement explicit trust relationships with time-bound access and specific use case restrictions by applying the following resource-based policy to the custom model. For example, a parent company might share a specialized legal document analysis model with subsidiaries, but only for specific document types and with audit logging enabled.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SubsidiaryModelAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::555666777888:role/LegalDocumentProcessor"
      },
      "Action": "bedrock:InvokeModel",
      "Resource": "arn:aws:bedrock:*:123456789012:custom-model/legal-analysis-model",
      "Condition": {
        "StringEquals": {
          "bedrock:ModelId": "legal-analysis-model"
        },
        "StringLike": {
          "aws:userid": "*:LegalTeam*"
        },
        "DateLessThan": {
          "aws:CurrentTime": "2026-06-30T23:59:59Z"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **SubsidiaryModelAccess** – Grants time-bound access to a custom legal analysis model for a specific subsidiary role, with additional validation that the user session belongs to the legal team.

### Multi-subsidiary sharing pattern
<a name="multi-subsidiary-sharing-pattern"></a>

For organizations with multiple subsidiaries requiring access to shared models, apply the following resource-based policy to the shared custom model:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MultiSubsidiaryAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::555666777888:role/SubsidiaryAIRole",
          "arn:aws:iam::999888777666:role/SubsidiaryAIRole",
          "arn:aws:iam::111222333444:role/SubsidiaryAIRole"
        ]
      },
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:GetCustomModel"
      ],
      "Resource": "arn:aws:bedrock:*:123456789012:custom-model/shared-analytics-model",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": ["us-east-1", "eu-west-1"]
        },
        "StringLike": {
          "aws:PrincipalTag/BusinessUnit": ["Finance", "Operations", "Legal"]
        },
        "Bool": {
          "aws:SecureTransport": "true"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **MultiSubsidiaryAccess** – Allows multiple subsidiary accounts to access a shared analytics model with regional restrictions, business unit validation, and mandatory HTTPS transport for secure cross-account model sharing

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
