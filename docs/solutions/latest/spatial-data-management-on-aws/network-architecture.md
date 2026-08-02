---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/network-architecture.html
---

# Network Architecture
<a name="network-architecture"></a>

## VPC Configuration
<a name="vpc-configuration"></a>

| Component | Configuration |
| --- | --- |
| Subnets | Public, private (with NAT gateway), and isolated (no internet) |
| Availability Zones | Two Availability Zones for high availability |
| NAT Gateways | One NAT gateway per Availability Zone for redundancy |
| VPC Endpoints | Eight VPC endpoints for private AWS service access |

## Lambda Placement
<a name="lambda-placement"></a>

| Function | Subnet Type | Purpose |
| --- | --- | --- |
| Resource Operation Function | Private subnets | Requires internet access for external APIs |
| Asset Watcher Function | Isolated subnets | No internet access required |
| Other Functions | Private subnets | Based on individual requirements |

## Security Groups
<a name="security-groups"></a>

| Security Group | Rules |
| --- | --- |
| Lambda Security Group | Outbound HTTPS to VPC endpoints and internet |
| VPC Endpoint Security Group | Inbound HTTPS from Lambda |
| OpenSearch Security Group | Inbound HTTPS from Lambda |
