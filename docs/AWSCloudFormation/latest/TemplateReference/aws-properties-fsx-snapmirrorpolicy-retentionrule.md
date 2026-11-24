---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-snapmirrorpolicy-retentionrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapmirrorPolicy RetentionRule

<a name="aws-properties-fsx-snapmirrorpolicy-retentionrule-description"></a>The `RetentionRule` property type specifies Property description not available. for an [AWS::FSx::SnapmirrorPolicy](aws-resource-fsx-snapmirrorpolicy.md).

## Syntax
<a name="aws-properties-fsx-snapmirrorpolicy-retentionrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-snapmirrorpolicy-retentionrule-syntax.json"></a>

```json
{
  "[Count](#cfn-fsx-snapmirrorpolicy-retentionrule-count)" : {{Integer}},
  "[CreationSchedule](#cfn-fsx-snapmirrorpolicy-retentionrule-creationschedule)" : {{String}},
  "[Label](#cfn-fsx-snapmirrorpolicy-retentionrule-label)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-snapmirrorpolicy-retentionrule-syntax.yaml"></a>

```yaml
  [Count](#cfn-fsx-snapmirrorpolicy-retentionrule-count): {{Integer}}
  [CreationSchedule](#cfn-fsx-snapmirrorpolicy-retentionrule-creationschedule): {{String}}
  [Label](#cfn-fsx-snapmirrorpolicy-retentionrule-label): {{String}}
```

## Properties
<a name="aws-properties-fsx-snapmirrorpolicy-retentionrule-properties"></a>

`Count`  <a name="cfn-fsx-snapmirrorpolicy-retentionrule-count"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1019`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreationSchedule`  <a name="cfn-fsx-snapmirrorpolicy-retentionrule-creationschedule"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_:.-]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-fsx-snapmirrorpolicy-retentionrule-label"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `31`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
