---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-vpcendpointassociation-subnetmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::VpcEndpointAssociation SubnetMapping
<a name="aws-properties-networkfirewall-vpcendpointassociation-subnetmapping"></a>

The ID for a subnet that's used in an association with a firewall. This is used in `CreateFirewall`, `AssociateSubnets`, and `CreateVpcEndpointAssociation`. AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.

## Syntax
<a name="aws-properties-networkfirewall-vpcendpointassociation-subnetmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-vpcendpointassociation-subnetmapping-syntax.json"></a>

```
{
  "[IPAddressType](#cfn-networkfirewall-vpcendpointassociation-subnetmapping-ipaddresstype)" : {{String}},
  "[SubnetId](#cfn-networkfirewall-vpcendpointassociation-subnetmapping-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-vpcendpointassociation-subnetmapping-syntax.yaml"></a>

```
  [IPAddressType](#cfn-networkfirewall-vpcendpointassociation-subnetmapping-ipaddresstype): {{String}}
  [SubnetId](#cfn-networkfirewall-vpcendpointassociation-subnetmapping-subnetid): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-vpcendpointassociation-subnetmapping-properties"></a>

`IPAddressType`  <a name="cfn-networkfirewall-vpcendpointassociation-subnetmapping-ipaddresstype"></a>
The subnet's IP address type. You can't change the IP address type after you create the subnet.
*Required*: No
*Type*: String
*Allowed values*: `DUALSTACK | IPV4 | IPV6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-networkfirewall-vpcendpointassociation-subnetmapping-subnetid"></a>
The unique identifier for the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
