---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-eventtriggercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger EventTriggerCondition
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggercondition"></a>

Specifies the circumstances under which the event should trigger the destination.

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggercondition-syntax.json"></a>

```
{
  "[EventTriggerDimensions](#cfn-customerprofiles-eventtrigger-eventtriggercondition-eventtriggerdimensions)" : {{[ EventTriggerDimension, ... ]}},
  "[LogicalOperator](#cfn-customerprofiles-eventtrigger-eventtriggercondition-logicaloperator)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggercondition-syntax.yaml"></a>

```
  [EventTriggerDimensions](#cfn-customerprofiles-eventtrigger-eventtriggercondition-eventtriggerdimensions): {{
    - EventTriggerDimension}}
  [LogicalOperator](#cfn-customerprofiles-eventtrigger-eventtriggercondition-logicaloperator): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggercondition-properties"></a>

`EventTriggerDimensions`  <a name="cfn-customerprofiles-eventtrigger-eventtriggercondition-eventtriggerdimensions"></a>
A list of dimensions to be evaluated for the event.
*Required*: Yes
*Type*: Array of [EventTriggerDimension](aws-properties-customerprofiles-eventtrigger-eventtriggerdimension.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalOperator`  <a name="cfn-customerprofiles-eventtrigger-eventtriggercondition-logicaloperator"></a>
The operator used to combine multiple dimensions.
*Required*: Yes
*Type*: String
*Allowed values*: `ANY | ALL | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
