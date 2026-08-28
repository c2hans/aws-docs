---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-input-inputdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::Input InputDefinition
<a name="aws-properties-iotevents-input-inputdefinition"></a>

The definition of the input.

## Syntax
<a name="aws-properties-iotevents-input-inputdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-input-inputdefinition-syntax.json"></a>

```
{
  "[Attributes](#cfn-iotevents-input-inputdefinition-attributes)" : {{[ Attribute, ... ]}}
}
```

### YAML
<a name="aws-properties-iotevents-input-inputdefinition-syntax.yaml"></a>

```
  [Attributes](#cfn-iotevents-input-inputdefinition-attributes): {{
    - Attribute}}
```

## Properties
<a name="aws-properties-iotevents-input-inputdefinition-properties"></a>

`Attributes`  <a name="cfn-iotevents-input-inputdefinition-attributes"></a>
The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using `BatchPutMessage`. Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the `condition` expressions used by detectors that monitor this input.
*Required*: Yes
*Type*: Array of [Attribute](aws-properties-iotevents-input-attribute.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
