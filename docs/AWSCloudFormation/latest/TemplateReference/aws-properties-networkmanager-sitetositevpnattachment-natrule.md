---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-sitetositevpnattachment-natrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::SiteToSiteVpnAttachment NatRule
<a name="aws-properties-networkmanager-sitetositevpnattachment-natrule"></a>

Describes a NAT rule of an attachment.

## Syntax
<a name="aws-properties-networkmanager-sitetositevpnattachment-natrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-sitetositevpnattachment-natrule-syntax.json"></a>

```
{
  "[MatchSourceCidr](#cfn-networkmanager-sitetositevpnattachment-natrule-matchsourcecidr)" : {{String}},
  "[NatCidr](#cfn-networkmanager-sitetositevpnattachment-natrule-natcidr)" : {{String}},
  "[RuleNumber](#cfn-networkmanager-sitetositevpnattachment-natrule-rulenumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-networkmanager-sitetositevpnattachment-natrule-syntax.yaml"></a>

```
  [MatchSourceCidr](#cfn-networkmanager-sitetositevpnattachment-natrule-matchsourcecidr): {{String}}
  [NatCidr](#cfn-networkmanager-sitetositevpnattachment-natrule-natcidr): {{String}}
  [RuleNumber](#cfn-networkmanager-sitetositevpnattachment-natrule-rulenumber): {{Integer}}
```

## Properties
<a name="aws-properties-networkmanager-sitetositevpnattachment-natrule-properties"></a>

`MatchSourceCidr`  <a name="cfn-networkmanager-sitetositevpnattachment-natrule-matchsourcecidr"></a>
The source CIDR block that the rule matches for traffic from the attachment.
*Required*: Yes
*Type*: String
*Pattern*: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([0-9]|[1-2][0-9]|3[0-2])$`
*Minimum*: `9`
*Maximum*: `18`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatCidr`  <a name="cfn-networkmanager-sitetositevpnattachment-natrule-natcidr"></a>
The CIDR block that matching source addresses are translated to.
*Required*: Yes
*Type*: String
*Pattern*: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([0-9]|[1-2][0-9]|3[0-2])$`
*Minimum*: `9`
*Maximum*: `18`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleNumber`  <a name="cfn-networkmanager-sitetositevpnattachment-natrule-rulenumber"></a>
The rule number. Rule numbers identify the rules of an attachment and don't set the order in which rules are evaluated.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `32766`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
