---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-thingtype-thingtypeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ThingType ThingTypeProperties
<a name="aws-properties-iot-thingtype-thingtypeproperties"></a>

The ThingTypeProperties contains information about the thing type including: a thing type description, and a list of searchable thing attribute names.

## Syntax
<a name="aws-properties-iot-thingtype-thingtypeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-thingtype-thingtypeproperties-syntax.json"></a>

```
{
  "[Mqtt5Configuration](#cfn-iot-thingtype-thingtypeproperties-mqtt5configuration)" : {{Mqtt5Configuration}},
  "[SearchableAttributes](#cfn-iot-thingtype-thingtypeproperties-searchableattributes)" : {{[ String, ... ]}},
  "[ThingTypeDescription](#cfn-iot-thingtype-thingtypeproperties-thingtypedescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-thingtype-thingtypeproperties-syntax.yaml"></a>

```
  [Mqtt5Configuration](#cfn-iot-thingtype-thingtypeproperties-mqtt5configuration): {{
    Mqtt5Configuration}}
  [SearchableAttributes](#cfn-iot-thingtype-thingtypeproperties-searchableattributes): {{
    - String}}
  [ThingTypeDescription](#cfn-iot-thingtype-thingtypeproperties-thingtypedescription): {{String}}
```

## Properties
<a name="aws-properties-iot-thingtype-thingtypeproperties-properties"></a>

`Mqtt5Configuration`  <a name="cfn-iot-thingtype-thingtypeproperties-mqtt5configuration"></a>
The configuration to add user-defined properties to enrich MQTT 5 messages.
*Required*: No
*Type*: [Mqtt5Configuration](aws-properties-iot-thingtype-mqtt5configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SearchableAttributes`  <a name="cfn-iot-thingtype-thingtypeproperties-searchableattributes"></a>
A list of searchable thing attribute names.
*Required*: No
*Type*: Array of String
*Maximum*: `128 | 3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingTypeDescription`  <a name="cfn-iot-thingtype-thingtypeproperties-thingtypedescription"></a>
The description of the thing type.
*Required*: No
*Type*: String
*Pattern*: `[\p{Graph}\x20]*`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
