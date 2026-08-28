---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-iotevents.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel IotEvents
<a name="aws-properties-iotevents-detectormodel-iotevents"></a>

Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.

## Syntax
<a name="aws-properties-iotevents-detectormodel-iotevents-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-iotevents-syntax.json"></a>

```
{
  "[InputName](#cfn-iotevents-detectormodel-iotevents-inputname)" : {{String}},
  "[Payload](#cfn-iotevents-detectormodel-iotevents-payload)" : {{Payload}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-iotevents-syntax.yaml"></a>

```
  [InputName](#cfn-iotevents-detectormodel-iotevents-inputname): {{String}}
  [Payload](#cfn-iotevents-detectormodel-iotevents-payload): {{
    Payload}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-iotevents-properties"></a>

`InputName`  <a name="cfn-iotevents-detectormodel-iotevents-inputname"></a>
The name of the AWS IoT Events input where the data is sent.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-iotevents-detectormodel-iotevents-payload"></a>
You can configure the action payload when you send a message to an AWS IoT Events input.
*Required*: No
*Type*: [Payload](aws-properties-iotevents-detectormodel-payload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
