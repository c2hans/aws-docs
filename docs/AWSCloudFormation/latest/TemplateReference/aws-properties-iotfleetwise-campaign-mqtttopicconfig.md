---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-mqtttopicconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign MqttTopicConfig
<a name="aws-properties-iotfleetwise-campaign-mqtttopicconfig"></a>

The MQTT topic to which the AWS IoT FleetWise campaign routes data. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) in the *AWS IoT Core Developer Guide*.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-mqtttopicconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-mqtttopicconfig-syntax.json"></a>

```
{
  "[ExecutionRoleArn](#cfn-iotfleetwise-campaign-mqtttopicconfig-executionrolearn)" : {{String}},
  "[MqttTopicArn](#cfn-iotfleetwise-campaign-mqtttopicconfig-mqtttopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-mqtttopicconfig-syntax.yaml"></a>

```
  [ExecutionRoleArn](#cfn-iotfleetwise-campaign-mqtttopicconfig-executionrolearn): {{String}}
  [MqttTopicArn](#cfn-iotfleetwise-campaign-mqtttopicconfig-mqtttopicarn): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-mqtttopicconfig-properties"></a>

`ExecutionRoleArn`  <a name="cfn-iotfleetwise-campaign-mqtttopicconfig-executionrolearn"></a>
The ARN of the role that grants AWS IoT FleetWise permission to access and act on messages sent to the MQTT topic.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MqttTopicArn`  <a name="cfn-iotfleetwise-campaign-mqtttopicconfig-mqtttopicarn"></a>
The ARN of the MQTT topic.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
