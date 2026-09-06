---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::SiteToSiteVpnAttachment ProposedNetworkFunctionGroupChange
<a name="aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange"></a>

Describes proposed changes to a network function group.

## Syntax
<a name="aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[NetworkFunctionGroupName](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname)" : {{String}},
  "[Tags](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber): {{Integer}}
  [NetworkFunctionGroupName](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname): {{String}}
  [Tags](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber"></a>
The proposed new attachment policy rule number for the network function group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFunctionGroupName`  <a name="cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname"></a>
The proposed name change for the network function group name.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange-tags"></a>
The list of proposed changes to the key-value tags associated with the network function group.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-sitetositevpnattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
