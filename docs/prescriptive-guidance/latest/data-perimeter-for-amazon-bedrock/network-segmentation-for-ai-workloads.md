---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/network-segmentation-for-ai-workloads.html
---

# Network segmentation for AI workloads
<a name="network-segmentation-for-ai-workloads"></a>

## Control objective
<a name="control-objective.08f3003d-09c5-5d40-9a64-34ebfb31b7a7"></a>

***Network perimeter**** – My identities can access resources only from expected networks*

Implement network segmentation that isolates AI processing from other workloads. Create dedicated subnets for Amazon Bedrock-related compute resources and configure AWS security groups that only allow necessary traffic flows.

**Dedicated AI subnet configuration:**

This Amazon VPC configuration defines isolated subnets for AI workloads. Applied during Amazon VPC setup or subnet creation.

```
{
  "VPCConfiguration": {
    "VpcId": "vpc-12345678",
    "Subnets": [
      {
        "SubnetId": "subnet-ai-workloads-1a",
        "AvailabilityZone": "us-east-1a",
        "CidrBlock": "10.0.10.0/24",
        "Tags": [
          {
            "Key": "Purpose",
            "Value": "BedrockAIWorkloads"
          }
        ]
      },
      {
        "SubnetId": "subnet-ai-workloads-1b",
        "AvailabilityZone": "us-east-1b",
        "CidrBlock": "10.0.11.0/24",
        "Tags": [
          {
            "Key": "Purpose",
            "Value": "BedrockAIWorkloads"
          }
        ]
      }
    ]
  }
}
```

**Policy explanation:**
+ **VPC Configuration** – Creates dedicated subnets for AI workloads with specific CIDR blocks and purpose tags, enabling network isolation and targeted security controls for Amazon Bedrock-related resources

### Security group rules for AI workloads
<a name="security-group-rules-for-ai-workloads"></a>

These security group rules control inbound/outbound traffic for AI workload resources. Applied to Amazon EC2 instances, AWS Lambda functions, or other compute resources accessing Amazon Bedrock.

**Note**
Replace `sg-bedrock-vpc-endpoints` with the actual security group ID attached to your Amazon Bedrock VPC endpoints.

```
{
  "SecurityGroupRules": [
    {
      "GroupId": "sg-bedrock-ai-workloads",
      "IpPermissions": [],
      "IpPermissionsEgress": [
        {
          "IpProtocol": "tcp",
          "FromPort": 443,
          "ToPort": 443,
          "UserIdGroupPairs": [
            {
              "GroupId": "sg-bedrock-vpc-endpoints",
              "Description": "HTTPS to Bedrock VPC endpoints"
            }
          ]
        }
      ]
    }
  ]
}
```

**Policy explanation:**
+ **SecurityGroupRules** – Restricts AI workload resources to communicate only with Amazon Bedrock VPC endpoints over HTTPS, preventing unauthorized network access and ensuring all Amazon Bedrock traffic flows through private endpoints

### VPC endpoint security group configuration
<a name="vpc-endpoint-security-group-configuration"></a>

The VPC endpoints for Amazon Bedrock must allow inbound traffic from the AI workload security group. Add this rule to the security group attached to your Amazon BedrockVPC endpoints:

```
{
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 443,
      "ToPort": 443,
      "UserIdGroupPairs": [
        {
          "GroupId": "sg-bedrock-ai-workloads",
          "Description": "HTTPS from AI workload security group"
        }
      ]
    }
  ]
}
```

**Policy explanation:**
+ **VPC Endpoint Security Group** – Allows inbound HTTPS traffic only from the AI workload security group, creating a secure communication channel between AI resources and Amazon Bedrock VPC endpoints

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
