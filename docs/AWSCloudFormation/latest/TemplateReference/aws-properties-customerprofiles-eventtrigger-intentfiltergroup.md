---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-intentfiltergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger IntentFilterGroup
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup"></a>

<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup-description"></a>The `IntentFilterGroup` property type specifies Property description not available. for an [AWS::CustomerProfiles::EventTrigger](aws-resource-customerprofiles-eventtrigger.md).

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup-syntax.json"></a>

```
{
  "[Conditions](#cfn-customerprofiles-eventtrigger-intentfiltergroup-conditions)" : {{[ IntentFilterCondition, ... ]}},
  "[LogicalOperator](#cfn-customerprofiles-eventtrigger-intentfiltergroup-logicaloperator)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup-syntax.yaml"></a>

```
  [Conditions](#cfn-customerprofiles-eventtrigger-intentfiltergroup-conditions): {{
    - IntentFilterCondition}}
  [LogicalOperator](#cfn-customerprofiles-eventtrigger-intentfiltergroup-logicaloperator): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltergroup-properties"></a>

`Conditions`  <a name="cfn-customerprofiles-eventtrigger-intentfiltergroup-conditions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [IntentFilterCondition](aws-properties-customerprofiles-eventtrigger-intentfiltercondition.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalOperator`  <a name="cfn-customerprofiles-eventtrigger-intentfiltergroup-logicaloperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ANY | ALL | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
