---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/model-access-controls.html
---

# Model access controls
<a name="model-access-controls"></a>

## Control objective
<a name="control-objective.8c129199-0120-5002-b70e-65efae39bb41"></a>

***Resource perimeter**** – My identities can access only trusted resources*

Different foundation models and custom models require different access patterns. My identities can access only trusted resources by implementing granular policies that restrict access to specific models based on the principal's role and intended use case:

**Model-specific access policy (IAM policy):**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowApprovedModelsInApprovedRegions",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": ["us-east-1", "us-west-2"],
          "bedrock:ModelId": [
            "anthropic.claude-3-sonnet-20240229-v1:0",
            "customer-service-model"
          ]
        }
      }
    },
    {
      "Sid": "ExplicitDenyOtherRegions",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": ["us-east-1", "us-west-2"]
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowApprovedModelsInApprovedRegions** – Grants access to specific Amazon Bedrock models while restricting operations to approved regions
+ **ExplicitDenyOtherRegions** – Explicitly denies model invocations in regions outside the approved list

### Path-based access patterns (IAM policy)
<a name="path-based-access-patterns-iam-policy"></a>

Implement environment separation through role paths by attaching the following IAM policy to roles that need path-based model access:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ProductionBedrockAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
      ],
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:role/production/*"
        }
      }
    },
    {
      "Sid": "DevelopmentBedrockAccess",
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-haiku-20240307-v1:0"
      ],
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:role/development/*"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **ProductionBedrockAccess** – Grants production roles access to the Claude Sonnet model with streaming capabilities for high-performance production workloads
+ **DevelopmentBedrockAccess** – Restricts development roles to the Claude Haiku model without streaming, providing cost-effective access for testing and development

Create roles with paths like `/production/AppName` or `/development/AppName`. Paths are immutable and visible in CloudTrail, making them ideal for environment separation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
