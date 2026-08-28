---
source_url: https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/resource-statement.html
---

# Network Access Analyzer resource statements
<a name="resource-statement"></a>

A resource statement in Network Access Analyzer defines the network components for a match or exclude condition. Each resource statement includes resource IDs, resource ARNs, or resource types. A single resource statement can include either resource IDs or resource types, but not both.

You can specify the following components by resource ID or resource ARN:
+ EC2 instances (source and destination only)
+ Internet gateways (source and destination only)
+ NAT gateways (through only)
+ Network firewalls (through only)
+ Network interfaces (source and destination only)
+ Resource groups
+ Security groups (source and destination only)
+ Subnets (source and destination only)
+ Transit gateway attachments
+ Virtual private clouds (VPC) (source and destination only)
+ Virtual private gateways (source and destination only)
+ VPC endpoint services
+ VPC endpoints
+ VPC peering connections

You must specify the following components by ARN:
+ Classic, Application, Network, and Gateway Load Balancers (through only)

You can specify the following components by resource type:
+ `AWS::EC2::InternetGateway` (source and destination only)
+ `AWS::EC2::NatGateway` (through only)
+ `AWS::EC2::TransitGatewayAttachment`
+ `AWS::EC2::VPCEndpoint` (destination and through only)
+ `AWS::EC2::VPCEndpointService`
+ `AWS::EC2::VPCPeeringConnection`
+ `AWS::EC2::VPNGateway` (source and destination only)
+ `AWS::ElasticLoadBalancing::LoadBalancer` (through only)
+ `AWS::ElasticLoadBalancingV2::LoadBalancer` (through only)
+ `AWS::NetworkFirewall::NetworkFirewall` (through only)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
