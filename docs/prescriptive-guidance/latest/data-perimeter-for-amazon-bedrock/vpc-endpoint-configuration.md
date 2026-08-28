---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/vpc-endpoint-configuration.html
---

# VPC endpoint configuration
<a name="vpc-endpoint-configuration"></a>

## Control objective
<a name="control-objective.59a3dd9e-c058-565e-a62f-3b1068cc044c"></a>

***Network perimeter**** – My identities can access resources only from expected networks*

Enforce that all Amazon Bedrock operations must originate from Amazon VPC endpoints by applying this service control policy (SCP) at the organization or OU level:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyBedrockPublicAccess",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:SourceVpce": "true"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **DenyBedrockPublicAccess** – Blocks Amazon Bedrock API calls that don't originate from an Amazon VPC endpoint, ensuring all AI workload traffic flows through private network paths.

**Note**
SCPs do not apply to the management account. Test enforcement using member accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
