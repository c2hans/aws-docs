---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-accessgrant-scopedactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant ScopedActions
<a name="aws-properties-cloudwatch-accessgrant-scopedactions"></a>

A group of actions within an access grant, together with the resource scopes and context conditions that apply to exactly those actions.

## Syntax
<a name="aws-properties-cloudwatch-accessgrant-scopedactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-accessgrant-scopedactions-syntax.json"></a>

```
{
  "[Actions](#cfn-cloudwatch-accessgrant-scopedactions-actions)" : {{[ String, ... ]}},
  "[ContextConditions](#cfn-cloudwatch-accessgrant-scopedactions-contextconditions)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Resources](#cfn-cloudwatch-accessgrant-scopedactions-resources)" : {{[ ResourceScope, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-accessgrant-scopedactions-syntax.yaml"></a>

```
  [Actions](#cfn-cloudwatch-accessgrant-scopedactions-actions): {{
    - String}}
  [ContextConditions](#cfn-cloudwatch-accessgrant-scopedactions-contextconditions): {{
    {{Key}}: {{Value}}}}
  [Resources](#cfn-cloudwatch-accessgrant-scopedactions-resources): {{
    - ResourceScope}}
```

## Properties
<a name="aws-properties-cloudwatch-accessgrant-scopedactions-properties"></a>

`Actions`  <a name="cfn-cloudwatch-accessgrant-scopedactions-actions"></a>
The actions this group applies to, each in vendor-code:Action form.
*Required*: Yes
*Type*: Array of String
*Minimum*: `3 | 1`
*Maximum*: `256 | 50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContextConditions`  <a name="cfn-cloudwatch-accessgrant-scopedactions-contextconditions"></a>
Context conditions for fine-grained access control on these actions, as a map of condition keys to lists of allowed values.
*Required*: No
*Type*: Object of Array
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-cloudwatch-accessgrant-scopedactions-resources"></a>
Resource scopes constraining these actions to specific resources.
*Required*: No
*Type*: Array of [ResourceScope](aws-properties-cloudwatch-accessgrant-resourcescope.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
