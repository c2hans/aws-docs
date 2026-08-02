---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectAttachment ProposedSegmentChange
<a name="aws-properties-networkmanager-connectattachment-proposedsegmentchange"></a>

Describes a proposed segment change. In some cases, the segment change must first be evaluated and accepted.

## Syntax
<a name="aws-properties-networkmanager-connectattachment-proposedsegmentchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectattachment-proposedsegmentchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-connectattachment-proposedsegmentchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[SegmentName](#cfn-networkmanager-connectattachment-proposedsegmentchange-segmentname)" : {{String}},
  "[Tags](#cfn-networkmanager-connectattachment-proposedsegmentchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectattachment-proposedsegmentchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-connectattachment-proposedsegmentchange-attachmentpolicyrulenumber): {{Integer}}
  [SegmentName](#cfn-networkmanager-connectattachment-proposedsegmentchange-segmentname): {{String}}
  [Tags](#cfn-networkmanager-connectattachment-proposedsegmentchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-connectattachment-proposedsegmentchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-connectattachment-proposedsegmentchange-attachmentpolicyrulenumber"></a>
The rule number in the policy document that applies to this change.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentName`  <a name="cfn-networkmanager-connectattachment-proposedsegmentchange-segmentname"></a>
The name of the segment to change.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-connectattachment-proposedsegmentchange-tags"></a>
The list of key-value tags that changed for the segment.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-connectattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
