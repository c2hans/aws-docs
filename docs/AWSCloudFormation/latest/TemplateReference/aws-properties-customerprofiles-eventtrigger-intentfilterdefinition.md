---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-intentfilterdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger IntentFilterDefinition
<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition"></a>

<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition-description"></a>The `IntentFilterDefinition` property type specifies Property description not available. for an [AWS::CustomerProfiles::EventTrigger](aws-resource-customerprofiles-eventtrigger.md).

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition-syntax.json"></a>

```
{
  "[Groups](#cfn-customerprofiles-eventtrigger-intentfilterdefinition-groups)" : {{[ IntentFilterGroup, ... ]}},
  "[LogicalOperator](#cfn-customerprofiles-eventtrigger-intentfilterdefinition-logicaloperator)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition-syntax.yaml"></a>

```
  [Groups](#cfn-customerprofiles-eventtrigger-intentfilterdefinition-groups): {{
    - IntentFilterGroup}}
  [LogicalOperator](#cfn-customerprofiles-eventtrigger-intentfilterdefinition-logicaloperator): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-intentfilterdefinition-properties"></a>

`Groups`  <a name="cfn-customerprofiles-eventtrigger-intentfilterdefinition-groups"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [IntentFilterGroup](aws-properties-customerprofiles-eventtrigger-intentfiltergroup.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalOperator`  <a name="cfn-customerprofiles-eventtrigger-intentfilterdefinition-logicaloperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ANY | ALL | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
