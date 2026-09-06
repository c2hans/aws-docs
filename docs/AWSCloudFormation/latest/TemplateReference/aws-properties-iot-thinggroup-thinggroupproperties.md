---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-thinggroup-thinggroupproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ThingGroup ThingGroupProperties
<a name="aws-properties-iot-thinggroup-thinggroupproperties"></a>

Thing group properties.

## Syntax
<a name="aws-properties-iot-thinggroup-thinggroupproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-thinggroup-thinggroupproperties-syntax.json"></a>

```
{
  "[AttributePayload](#cfn-iot-thinggroup-thinggroupproperties-attributepayload)" : {{AttributePayload}},
  "[ThingGroupDescription](#cfn-iot-thinggroup-thinggroupproperties-thinggroupdescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-thinggroup-thinggroupproperties-syntax.yaml"></a>

```
  [AttributePayload](#cfn-iot-thinggroup-thinggroupproperties-attributepayload): {{
    AttributePayload}}
  [ThingGroupDescription](#cfn-iot-thinggroup-thinggroupproperties-thinggroupdescription): {{String}}
```

## Properties
<a name="aws-properties-iot-thinggroup-thinggroupproperties-properties"></a>

`AttributePayload`  <a name="cfn-iot-thinggroup-thinggroupproperties-attributepayload"></a>
The thing group attributes in JSON format.
*Required*: No
*Type*: [AttributePayload](aws-properties-iot-thinggroup-attributepayload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingGroupDescription`  <a name="cfn-iot-thinggroup-thinggroupproperties-thinggroupdescription"></a>
The thing group description.
*Required*: No
*Type*: String
*Pattern*: `[\p{Graph}\x20]*`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
