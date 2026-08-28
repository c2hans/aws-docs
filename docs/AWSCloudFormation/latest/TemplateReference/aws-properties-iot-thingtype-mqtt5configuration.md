---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-thingtype-mqtt5configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::ThingType Mqtt5Configuration
<a name="aws-properties-iot-thingtype-mqtt5configuration"></a>

The configuration to add user-defined properties to enrich MQTT 5 messages.

## Syntax
<a name="aws-properties-iot-thingtype-mqtt5configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-thingtype-mqtt5configuration-syntax.json"></a>

```
{
  "[PropagatingAttributes](#cfn-iot-thingtype-mqtt5configuration-propagatingattributes)" : {{[ PropagatingAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-thingtype-mqtt5configuration-syntax.yaml"></a>

```
  [PropagatingAttributes](#cfn-iot-thingtype-mqtt5configuration-propagatingattributes): {{
    - PropagatingAttribute}}
```

## Properties
<a name="aws-properties-iot-thingtype-mqtt5configuration-properties"></a>

`PropagatingAttributes`  <a name="cfn-iot-thingtype-mqtt5configuration-propagatingattributes"></a>
An object that represents the connection attribute, the thing attribute, and the MQTT 5 user property key.
*Required*: No
*Type*: Array of [PropagatingAttribute](aws-properties-iot-thingtype-propagatingattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
