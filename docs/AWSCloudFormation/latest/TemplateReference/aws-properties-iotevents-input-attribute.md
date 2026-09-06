---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-input-attribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::Input Attribute
<a name="aws-properties-iotevents-input-attribute"></a>

The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using `BatchPutMessage`. Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the `condition` expressions used by detectors.

## Syntax
<a name="aws-properties-iotevents-input-attribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-input-attribute-syntax.json"></a>

```
{
  "[JsonPath](#cfn-iotevents-input-attribute-jsonpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-input-attribute-syntax.yaml"></a>

```
  [JsonPath](#cfn-iotevents-input-attribute-jsonpath): {{String}}
```

## Properties
<a name="aws-properties-iotevents-input-attribute-properties"></a>

`JsonPath`  <a name="cfn-iotevents-input-attribute-jsonpath"></a>
An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events (`BatchPutMessage`). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the `condition` expressions used by detectors.
Syntax: `<field-name>.<field-name>...`
*Required*: Yes
*Type*: String
*Pattern*: `^((`[a-zA-Z0-9_\- ]+`)|([a-zA-Z0-9_\-]+))(\.((`[a-zA-Z0-9_\- ]+`)|([a-zA-Z0-9_\-]+)))*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
