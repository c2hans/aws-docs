---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectAttachment ProposedNetworkFunctionGroupChange
<a name="aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange"></a>

Describes proposed changes to a network function group.

## Syntax
<a name="aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[NetworkFunctionGroupName](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname)" : {{String}},
  "[Tags](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber): {{Integer}}
  [NetworkFunctionGroupName](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname): {{String}}
  [Tags](#cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-connectattachment-proposednetworkfunctiongroupchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber"></a>
The proposed new attachment policy rule number for the network function group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFunctionGroupName`  <a name="cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname"></a>
The proposed name change for the network function group name.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-connectattachment-proposednetworkfunctiongroupchange-tags"></a>
The list of proposed changes to the key-value tags associated with the network function group.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-connectattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
