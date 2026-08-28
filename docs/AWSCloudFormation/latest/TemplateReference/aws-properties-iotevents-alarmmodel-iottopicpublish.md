---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-iottopicpublish.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel IotTopicPublish
<a name="aws-properties-iotevents-alarmmodel-iottopicpublish"></a>

Information required to publish the MQTT message through the AWS IoT message broker.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-iottopicpublish-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-iottopicpublish-syntax.json"></a>

```
{
  "[MqttTopic](#cfn-iotevents-alarmmodel-iottopicpublish-mqtttopic)" : {{String}},
  "[Payload](#cfn-iotevents-alarmmodel-iottopicpublish-payload)" : {{Payload}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-iottopicpublish-syntax.yaml"></a>

```
  [MqttTopic](#cfn-iotevents-alarmmodel-iottopicpublish-mqtttopic): {{String}}
  [Payload](#cfn-iotevents-alarmmodel-iottopicpublish-payload): {{
    Payload}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-iottopicpublish-properties"></a>

`MqttTopic`  <a name="cfn-iotevents-alarmmodel-iottopicpublish-mqtttopic"></a>
The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>`) and input values (`$input.<input-name>.<path-to-datum>`) as the topic string.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-iotevents-alarmmodel-iottopicpublish-payload"></a>
You can configure the action payload when you publish a message to an AWS IoT Core topic.
*Required*: No
*Type*: [Payload](aws-properties-iotevents-alarmmodel-payload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
