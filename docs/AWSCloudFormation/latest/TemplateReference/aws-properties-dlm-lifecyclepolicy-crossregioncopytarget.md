---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-crossregioncopytarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy CrossRegionCopyTarget
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopytarget"></a>

**[Default policies only]** Specifies a destination Region for cross-Region copy actions.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopytarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopytarget-syntax.json"></a>

```
{
  "[TargetRegion](#cfn-dlm-lifecyclepolicy-crossregioncopytarget-targetregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopytarget-syntax.yaml"></a>

```
  [TargetRegion](#cfn-dlm-lifecyclepolicy-crossregioncopytarget-targetregion): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopytarget-properties"></a>

`TargetRegion`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopytarget-targetregion"></a>
The target Region, for example `us-east-1`.
*Required*: No
*Type*: String
*Pattern*: `([a-z]+-){2,3}\d`
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
