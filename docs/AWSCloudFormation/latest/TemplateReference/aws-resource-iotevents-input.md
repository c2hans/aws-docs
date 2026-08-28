---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotevents-input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::Input
<a name="aws-resource-iotevents-input"></a>

The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [ How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.

## Syntax
<a name="aws-resource-iotevents-input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotevents-input-syntax.json"></a>

```
{
  "Type" : "AWS::IoTEvents::Input",
  "Properties" : {
      "[InputDefinition](#cfn-iotevents-input-inputdefinition)" : {{InputDefinition}},
      "[InputDescription](#cfn-iotevents-input-inputdescription)" : {{String}},
      "[InputName](#cfn-iotevents-input-inputname)" : {{String}},
      "[Tags](#cfn-iotevents-input-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotevents-input-syntax.yaml"></a>

```
Type: AWS::IoTEvents::Input
Properties:
  [InputDefinition](#cfn-iotevents-input-inputdefinition): {{
    InputDefinition}}
  [InputDescription](#cfn-iotevents-input-inputdescription): {{String}}
  [InputName](#cfn-iotevents-input-inputname): {{String}}
  [Tags](#cfn-iotevents-input-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotevents-input-properties"></a>

`InputDefinition`  <a name="cfn-iotevents-input-inputdefinition"></a>
The definition of the input.
*Required*: Yes
*Type*: [InputDefinition](aws-properties-iotevents-input-inputdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputDescription`  <a name="cfn-iotevents-input-inputdescription"></a>
A brief description of the input.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputName`  <a name="cfn-iotevents-input-inputname"></a>
The name of the input.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotevents-input-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-iotevents-input-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotevents-input-return-values"></a>

### Ref
<a name="aws-resource-iotevents-input-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the input. For example:

 `{"Ref": "myInput"}`

For the AWS IoT Events input `myInput`, `Ref` returns the name of the input.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-iotevents-input--examples"></a>

### Input
<a name="aws-resource-iotevents-input--examples--Input"></a>

The following example creates an input.

#### JSON
<a name="aws-resource-iotevents-input--examples--Input--json"></a>

```
{
  "Description": "Input Template for CloudFormation",
  "Resources": {
    "myInput": {
      "Type": "AWS::IoTEvents::Input",
      "Properties": {
        "InputName": "myInput",
        "InputDescription": "My Input created by CloudFormation",
        "InputDefinition": {
          "Attributes": [
            {
              "JsonPath": "foo"
            },
            {
              "JsonPath": "bar"
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-iotevents-input--examples--Input--yaml"></a>

```
---
Description: "Input Template for CloudFormation"
Resources:
  myInput:
    Type: "AWS::IoTEvents::Input"
    Properties:
      InputName: "myInput"
      InputDescription: "My Input created by CloudFormation"
      InputDefinition:
        Attributes:
          -
            JsonPath: "foo"
          -
            JsonPath: "bar"
```

## See also
<a name="aws-resource-iotevents-input--seealso"></a>
+ [ How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*
+ [CreateInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateInput.html) in the *AWS IoT Events API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
