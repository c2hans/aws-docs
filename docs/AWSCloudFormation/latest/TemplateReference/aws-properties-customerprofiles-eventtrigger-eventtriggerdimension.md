---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-eventtriggerdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger EventTriggerDimension
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerdimension"></a>

A specific event dimension to be assessed.

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerdimension-syntax.json"></a>

```
{
  "[ObjectAttributes](#cfn-customerprofiles-eventtrigger-eventtriggerdimension-objectattributes)" : {{[ ObjectAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerdimension-syntax.yaml"></a>

```
  [ObjectAttributes](#cfn-customerprofiles-eventtrigger-eventtriggerdimension-objectattributes): {{
    - ObjectAttribute}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-eventtriggerdimension-properties"></a>

`ObjectAttributes`  <a name="cfn-customerprofiles-eventtrigger-eventtriggerdimension-objectattributes"></a>
A list of object attributes to be evaluated.
*Required*: Yes
*Type*: Array of [ObjectAttribute](aws-properties-customerprofiles-eventtrigger-objectattribute.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
