---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall VpcEndpoint
<a name="aws-properties-networkfirewall-firewall-vpcendpoint"></a>

The VPC and subnets for a proxy mode firewall endpoint. This is used in CreateFirewall when `NoSourcePreservation` is `TRUE`, to specify where Network Firewall creates the firewall endpoint.

This differs from [AWS::NetworkFirewall::VpcEndpointAssociation](aws-resource-networkfirewall-vpcendpointassociation.md), which defines additional secondary endpoints for a firewall in other VPCs.

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
The subnets in which Network Firewall creates the firewall endpoint for a proxy mode firewall. Each subnet must belong to a different Availability Zone in the VPC.
*Required*: No
*Type*: Array of [SubnetMapping](aws-properties-networkfirewall-firewall-subnetmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-networkfirewall-firewall-vpcendpoint-vpcid"></a>
The unique identifier of the VPC where Network Firewall creates the proxy mode firewall endpoint.
*Required*: No
*Type*: String
*Pattern*: `^vpc-[0-9a-f]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
