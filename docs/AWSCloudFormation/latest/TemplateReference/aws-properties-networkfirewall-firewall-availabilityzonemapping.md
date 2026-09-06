---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-availabilityzonemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall AvailabilityZoneMapping
<a name="aws-properties-networkfirewall-firewall-availabilityzonemapping"></a>

Defines the mapping between an Availability Zone and a firewall endpoint for a transit gateway-attached firewall. Each mapping represents where the firewall can process traffic. You use these mappings when calling `CreateFirewall`, `AssociateAvailabilityZones`, and `DisassociateAvailabilityZones`.

To retrieve the current Availability Zone mappings for a firewall, use `DescribeFirewall`.

## Syntax
<a name="aws-properties-networkfirewall-firewall-availabilityzonemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-availabilityzonemapping-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-networkfirewall-firewall-availabilityzonemapping-availabilityzone)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-availabilityzonemapping-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-networkfirewall-firewall-availabilityzonemapping-availabilityzone): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-availabilityzonemapping-properties"></a>

`AvailabilityZone`  <a name="cfn-networkfirewall-firewall-availabilityzonemapping-availabilityzone"></a>
The ID of the Availability Zone where the firewall endpoint is located. For example, `us-east-2a`. The Availability Zone must be in the same Region as the transit gateway.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
