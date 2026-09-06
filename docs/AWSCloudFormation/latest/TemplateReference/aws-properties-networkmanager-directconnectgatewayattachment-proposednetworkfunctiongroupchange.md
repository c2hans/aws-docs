---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::DirectConnectGatewayAttachment ProposedNetworkFunctionGroupChange
<a name="aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange"></a>

Describes proposed changes to a network function group.

## Syntax
<a name="aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[NetworkFunctionGroupName](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname)" : {{String}},
  "[Tags](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber): {{Integer}}
  [NetworkFunctionGroupName](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname): {{String}}
  [Tags](#cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber"></a>
The proposed new attachment policy rule number for the network function group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFunctionGroupName`  <a name="cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname"></a>
The proposed name change for the network function group name.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-directconnectgatewayattachment-proposednetworkfunctiongroupchange-tags"></a>
The list of proposed changes to the key-value tags associated with the network function group.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-directconnectgatewayattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
