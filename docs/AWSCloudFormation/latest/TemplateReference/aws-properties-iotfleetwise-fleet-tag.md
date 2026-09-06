---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-fleet-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Fleet Tag
<a name="aws-properties-iotfleetwise-fleet-tag"></a>

A set of key/value pairs that are used to manage the resource.

## Syntax
<a name="aws-properties-iotfleetwise-fleet-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-fleet-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotfleetwise-fleet-tag-key)" : {{String}},
  "[Value](#cfn-iotfleetwise-fleet-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-fleet-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotfleetwise-fleet-tag-key): {{String}}
  [Value](#cfn-iotfleetwise-fleet-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-fleet-tag-properties"></a>

`Key`  <a name="cfn-iotfleetwise-fleet-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotfleetwise-fleet-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
