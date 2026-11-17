---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall VpcEndpoint
<a name="aws-properties-networkfirewall-firewall-vpcendpoint"></a>

The VPC and subnets for the endpoints of a proxy mode firewall. You use this in `CreateFirewall`. Network Firewall creates the firewall endpoints and the firewall's NAT gateways in this VPC.

This differs from `VpcEndpointAssociation`, which defines additional endpoints for a firewall in other VPCs.

## Syntax
<a name="aws-properties-networkfirewall-firewall-vpcendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-vpcendpoint-syntax.json"></a>

```
{
  "[SubnetMappings](#cfn-networkfirewall-firewall-vpcendpoint-subnetmappings)" : {{[ SubnetMapping, ... ]}},
  "[VpcId](#cfn-networkfirewall-firewall-vpcendpoint-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-vpcendpoint-syntax.yaml"></a>

```
  [SubnetMappings](#cfn-networkfirewall-firewall-vpcendpoint-subnetmappings): {{
    - SubnetMapping}}
  [VpcId](#cfn-networkfirewall-firewall-vpcendpoint-vpcid): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-vpcendpoint-properties"></a>

`SubnetMappings`  <a name="cfn-networkfirewall-firewall-vpcendpoint-subnetmappings"></a>
The subnets where Network Firewall creates the firewall endpoints of a proxy mode firewall. Specify one subnet for each Availability Zone, and a NAT gateway mapping in each of those Availability Zones.
*Required*: No
*Type*: Array of [SubnetMapping](aws-properties-networkfirewall-firewall-subnetmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-networkfirewall-firewall-vpcendpoint-vpcid"></a>
The ID of the VPC where Network Firewall creates the endpoints and NAT gateways of a proxy mode firewall.
*Required*: No
*Type*: String
*Pattern*: `^vpc-[0-9a-f]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
