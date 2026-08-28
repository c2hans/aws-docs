---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::VpcAttachment ProposedSegmentChange
<a name="aws-properties-networkmanager-vpcattachment-proposedsegmentchange"></a>

Describes a proposed segment change. In some cases, the segment change must first be evaluated and accepted.

## Syntax
<a name="aws-properties-networkmanager-vpcattachment-proposedsegmentchange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-vpcattachment-proposedsegmentchange-syntax.json"></a>

```
{
  "[AttachmentPolicyRuleNumber](#cfn-networkmanager-vpcattachment-proposedsegmentchange-attachmentpolicyrulenumber)" : {{Integer}},
  "[SegmentName](#cfn-networkmanager-vpcattachment-proposedsegmentchange-segmentname)" : {{String}},
  "[Tags](#cfn-networkmanager-vpcattachment-proposedsegmentchange-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-vpcattachment-proposedsegmentchange-syntax.yaml"></a>

```
  [AttachmentPolicyRuleNumber](#cfn-networkmanager-vpcattachment-proposedsegmentchange-attachmentpolicyrulenumber): {{Integer}}
  [SegmentName](#cfn-networkmanager-vpcattachment-proposedsegmentchange-segmentname): {{String}}
  [Tags](#cfn-networkmanager-vpcattachment-proposedsegmentchange-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-networkmanager-vpcattachment-proposedsegmentchange-properties"></a>

`AttachmentPolicyRuleNumber`  <a name="cfn-networkmanager-vpcattachment-proposedsegmentchange-attachmentpolicyrulenumber"></a>
The rule number in the policy document that applies to this change.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentName`  <a name="cfn-networkmanager-vpcattachment-proposedsegmentchange-segmentname"></a>
The name of the segment to change.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-vpcattachment-proposedsegmentchange-tags"></a>
The list of key-value tags that changed for the segment.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-vpcattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
