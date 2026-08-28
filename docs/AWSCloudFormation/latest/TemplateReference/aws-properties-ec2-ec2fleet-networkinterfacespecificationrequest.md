---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet NetworkInterfaceSpecificationRequest
<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest"></a>

<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest-description"></a>The `NetworkInterfaceSpecificationRequest` property type specifies Property description not available. for an [AWS::EC2::EC2Fleet](aws-resource-ec2-ec2fleet.md).

## Syntax
<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest-syntax.json"></a>

```
{
  "[AssociatePublicIpAddress](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-associatepublicipaddress)" : {{Boolean}},
  "[DeleteOnTermination](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deleteontermination)" : {{Boolean}},
  "[Description](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-description)" : {{String}},
  "[DeviceIndex](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deviceindex)" : {{Integer}},
  "[Groups](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-groups)" : {{[ String, ... ]}},
  "[InterfaceType](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-interfacetype)" : {{String}},
  "[Ipv6AddressCount](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresscount)" : {{Integer}},
  "[Ipv6Addresses](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresses)" : {{[ Ipv6AddressRequest, ... ]}},
  "[NetworkCardIndex](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkcardindex)" : {{Integer}},
  "[NetworkInterfaceId](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkinterfaceid)" : {{String}},
  "[PrivateIpAddress](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddress)" : {{String}},
  "[PrivateIpAddresses](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddresses)" : {{[ PrivateIpAddressSpecificationRequest, ... ]}},
  "[SecondaryPrivateIpAddressCount](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-secondaryprivateipaddresscount)" : {{Integer}},
  "[SubnetId](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest-syntax.yaml"></a>

```
  [AssociatePublicIpAddress](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-associatepublicipaddress): {{Boolean}}
  [DeleteOnTermination](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deleteontermination): {{Boolean}}
  [Description](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-description): {{String}}
  [DeviceIndex](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deviceindex): {{Integer}}
  [Groups](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-groups): {{
    - String}}
  [InterfaceType](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-interfacetype): {{String}}
  [Ipv6AddressCount](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresscount): {{Integer}}
  [Ipv6Addresses](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresses): {{
    - Ipv6AddressRequest}}
  [NetworkCardIndex](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkcardindex): {{Integer}}
  [NetworkInterfaceId](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkinterfaceid): {{String}}
  [PrivateIpAddress](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddress): {{String}}
  [PrivateIpAddresses](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddresses): {{
    - PrivateIpAddressSpecificationRequest}}
  [SecondaryPrivateIpAddressCount](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-secondaryprivateipaddresscount): {{Integer}}
  [SubnetId](#cfn-ec2-ec2fleet-networkinterfacespecificationrequest-subnetid): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-networkinterfacespecificationrequest-properties"></a>

`AssociatePublicIpAddress`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-associatepublicipaddress"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeleteOnTermination`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deleteontermination"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeviceIndex`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-deviceindex"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Groups`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-groups"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InterfaceType`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-interfacetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6AddressCount`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresscount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Addresses`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-ipv6addresses"></a>
Property description not available.
*Required*: No
*Type*: Array of [Ipv6AddressRequest](aws-properties-ec2-ec2fleet-ipv6addressrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkCardIndex`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkcardindex"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInterfaceId`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-networkinterfaceid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddress`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddress"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateIpAddresses`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-privateipaddresses"></a>
Property description not available.
*Required*: No
*Type*: Array of [PrivateIpAddressSpecificationRequest](aws-properties-ec2-ec2fleet-privateipaddressspecificationrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecondaryPrivateIpAddressCount`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-secondaryprivateipaddresscount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-ec2fleet-networkinterfacespecificationrequest-subnetid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
