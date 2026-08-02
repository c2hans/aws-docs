---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/vpc-endpoint-policies.html
---

# Amazon VPC endpoint policies
<a name="vpc-endpoint-policies"></a>

## Control objective
<a name="control-objective.c08425ef-4960-564f-94ba-4d53e69cba0c"></a>

***Identity perimeter**** – Only trusted identities are allowed from my network*

Control which identities can access Amazon Bedrock through VPC endpoints by attaching the following policy to the Amazon Bedrock VPC endpoint.

**Important**
Replace `o-1234567890` with your AWS organization ID.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOrganizationAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:CreateKnowledgeBase",
        "bedrock:GetKnowledgeBase"
      ],
      "Resource": "*",
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
+ **AllowOrganizationAccess** – Permits Amazon Bedrock API calls only from identities within your AWSorganization, creating an identity boundary at the VPC endpoint level.

**Note**
For network-based VPC endpoint controls, see the [Network Perimeter](network-perimeter.md) section.
