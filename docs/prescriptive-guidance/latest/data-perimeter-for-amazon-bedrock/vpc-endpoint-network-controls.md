---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/vpc-endpoint-network-controls.html
---

# VPC endpoint network controls
<a name="vpc-endpoint-network-controls"></a>

## Control objective
<a name="control-objective.c09d1a37-9cb2-5222-9bdf-a51ad817058e"></a>

***Network perimeter**** – My resources can only be accessed from expected networks*

Enforce network-based access controls at Amazon VPC endpoints to ensure Amazon Bedrock resources are accessed only through specific network paths.

**VPC endpoint network policy**

Apply this policy to Amazon Bedrock VPC endpoints to enforce specific endpoint access:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSpecificVPCEndpoints",
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
        "ForAnyValue:StringEquals": {
          "aws:SourceVpce": [
            "vpce-1234567890abcdef0",
            "vpce-0987654321fedcba0"
          ]
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **VPC endpoint restriction** – Allows access only through specified Amazon VPC endpoints.
+ **Network boundary** – Blocks access from unauthorized network paths.
+ **Multi-endpoint support** – Supports multiple Amazon VPC endpoints for high availability.

**Important**
Replace `vpce-1234567890abcdef0` with your actual Amazon VPC IDs. To find your Amazon VPC endpoint IDs, use: `aws ec2 describe-vpc-endpoints --filters "Name=service-name,Values=com.amazonaws.*.bedrock"`

### Combined identity and network controls
<a name="combined-identity-and-network-controls"></a>

For comprehensive protection, combine this network policy with identity controls:

1. **Identity control** – Use `aws:PrincipalOrgID` to restrict identities (Identity perimeter).

1. **Network control** – Use `aws:SourceVpce `to restrict network paths (Network perimeter).

1. **Defense in depth** – Both conditions must be satisfied for access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
