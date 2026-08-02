---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/network-access-control-lists-nac-ls.html
---

# Network access control lists (NACLs)
<a name="network-access-control-lists-nac-ls"></a>

## Control objective
<a name="control-objective.fd700ef0-e194-5c21-8b6a-d741a6fbf25a"></a>

***Network perimeter**** – My identities can access resources only from expected networks*

Implement network ACLs as an additional layer of defense for AI workload subnets. NACLs provide subnet-level traffic filtering that complements AWS security group rules.

**NACL configuration for AI workload subnet:**

This NACL is applied to the AI workload subnet to restrict traffic at the subnet boundary. It allows only HTTPS traffic to Amazon VPC endpoints and blocks all external internet access.

```
{
  "NetworkAclEntries": [
    {
      "RuleNumber": 100,
      "Protocol": "6",
      "RuleAction": "allow",
      "Egress": true,
      "PortRange": {
        "From": 443,
        "To": 443
      },
      "CidrBlock": "10.0.0.0/16"
    },
    {
      "RuleNumber": 110,
      "Protocol": "6",
      "RuleAction": "allow",
      "Egress": true,
      "PortRange": {
        "From": 1024,
        "To": 65535
      },
      "CidrBlock": "10.0.0.0/16"
    }
  ]
}
```

**Policy explanation:**
+ **Rule 100** – Allows outbound HTTPS (port 443) to VPC CIDR for Amazon Bedrock API calls through VPC endpoints.
+ **Rule 110** – Allows outbound ephemeral ports (1024-65535) to VPC CIDR for return traffic from Amazon Bedrock responses.
+ **Implicit deny** – All other traffic is denied by default NACL rule (32767).
