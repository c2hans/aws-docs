---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::TransitGatewayRouteTableAttachment ProposedNetworkFunctionGroupChange
<a name="aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange"></a>

Describes proposed changes to a network function group.

## Syntax
<a name="aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[NetworkFunctionGroupName](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname)" : {{String}},
  "[Tags](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber): {{Integer}}
  [NetworkFunctionGroupName](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname): {{String}}
  [Tags](#cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-attachmentpolicyrulenumber"></a>
The proposed new attachment policy rule number for the network function group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFunctionGroupName`  <a name="cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-networkfunctiongroupname"></a>
The proposed name change for the network function group name.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-transitgatewayroutetableattachment-proposednetworkfunctiongroupchange-tags"></a>
The list of proposed changes to the key-value tags associated with the network function group.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-transitgatewayroutetableattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
