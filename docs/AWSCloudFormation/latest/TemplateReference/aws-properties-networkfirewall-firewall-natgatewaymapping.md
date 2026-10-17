---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-natgatewaymapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall NatGatewayMapping
<a name="aws-properties-networkfirewall-firewall-natgatewaymapping"></a>

A NAT gateway that a proxy mode firewall uses to proxy traffic. This is used in CreateFirewall when `NoSourcePreservation` is `TRUE`.

## Syntax
<a name="aws-properties-networkfirewall-firewall-natgatewaymapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-natgatewaymapping-syntax.json"></a>

```
{
  "[NatGatewayId](#cfn-networkfirewall-firewall-natgatewaymapping-natgatewayid)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-natgatewaymapping-syntax.yaml"></a>

```
  [NatGatewayId](#cfn-networkfirewall-firewall-natgatewaymapping-natgatewayid): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-natgatewaymapping-properties"></a>

`NatGatewayId`  <a name="cfn-networkfirewall-firewall-natgatewaymapping-natgatewayid"></a>
A unique identifier for the NAT gateway to use with proxy resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
