---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-nobidaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link NoBidAction
<a name="aws-properties-rtbfabric-link-nobidaction"></a>

Describes a no bid action.

## Syntax
<a name="aws-properties-rtbfabric-link-nobidaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-nobidaction-syntax.json"></a>

```
{
  "[NoBidReasonCode](#cfn-rtbfabric-link-nobidaction-nobidreasoncode)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-nobidaction-syntax.yaml"></a>

```
  [NoBidReasonCode](#cfn-rtbfabric-link-nobidaction-nobidreasoncode): {{Integer}}
```

## Properties
<a name="aws-properties-rtbfabric-link-nobidaction-properties"></a>

`NoBidReasonCode`  <a name="cfn-rtbfabric-link-nobidaction-nobidreasoncode"></a>
The reason code for the no bid action.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
