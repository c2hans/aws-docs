---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-sqs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel Sqs
<a name="aws-properties-iotevents-detectormodel-sqs"></a>

Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

## Syntax
<a name="aws-properties-iotevents-detectormodel-sqs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-sqs-syntax.json"></a>

```
{
  "[Payload](#cfn-iotevents-detectormodel-sqs-payload)" : {{Payload}},
  "[QueueUrl](#cfn-iotevents-detectormodel-sqs-queueurl)" : {{String}},
  "[UseBase64](#cfn-iotevents-detectormodel-sqs-usebase64)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-sqs-syntax.yaml"></a>

```
  [Payload](#cfn-iotevents-detectormodel-sqs-payload): {{
    Payload}}
  [QueueUrl](#cfn-iotevents-detectormodel-sqs-queueurl): {{String}}
  [UseBase64](#cfn-iotevents-detectormodel-sqs-usebase64): {{Boolean}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-sqs-properties"></a>

`Payload`  <a name="cfn-iotevents-detectormodel-sqs-payload"></a>
You can configure the action payload when you send a message to an Amazon SQS queue.
*Required*: No
*Type*: [Payload](aws-properties-iotevents-detectormodel-payload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueUrl`  <a name="cfn-iotevents-detectormodel-sqs-queueurl"></a>
The URL of the SQS queue where the data is written.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBase64`  <a name="cfn-iotevents-detectormodel-sqs-usebase64"></a>
Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
