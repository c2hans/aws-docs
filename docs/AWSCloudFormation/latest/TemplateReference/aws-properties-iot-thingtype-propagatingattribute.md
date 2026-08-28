---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-thingtype-propagatingattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ThingType PropagatingAttribute
<a name="aws-properties-iot-thingtype-propagatingattribute"></a>

An object that represents the connection attribute, the thing attribute, and the MQTT 5 user property key.

## Syntax
<a name="aws-properties-iot-thingtype-propagatingattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-thingtype-propagatingattribute-syntax.json"></a>

```
{
  "[ConnectionAttribute](#cfn-iot-thingtype-propagatingattribute-connectionattribute)" : {{String}},
  "[ThingAttribute](#cfn-iot-thingtype-propagatingattribute-thingattribute)" : {{String}},
  "[UserPropertyKey](#cfn-iot-thingtype-propagatingattribute-userpropertykey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-thingtype-propagatingattribute-syntax.yaml"></a>

```
  [ConnectionAttribute](#cfn-iot-thingtype-propagatingattribute-connectionattribute): {{String}}
  [ThingAttribute](#cfn-iot-thingtype-propagatingattribute-thingattribute): {{String}}
  [UserPropertyKey](#cfn-iot-thingtype-propagatingattribute-userpropertykey): {{String}}
```

## Properties
<a name="aws-properties-iot-thingtype-propagatingattribute-properties"></a>

`ConnectionAttribute`  <a name="cfn-iot-thingtype-propagatingattribute-connectionattribute"></a>
The attribute associated with the connection details.
*Required*: No
*Type*: String
*Allowed values*: `iot:ClientId | iot:Thing.ThingName`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingAttribute`  <a name="cfn-iot-thingtype-propagatingattribute-thingattribute"></a>
The thing attribute that is propagating for MQTT 5 message enrichment.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.,@/:#-]+`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPropertyKey`  <a name="cfn-iot-thingtype-propagatingattribute-userpropertykey"></a>
The key of the MQTT 5 user property, which is a key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9:$.]+`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
