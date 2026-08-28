---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-datadestinationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign DataDestinationConfig
<a name="aws-properties-iotfleetwise-campaign-datadestinationconfig"></a>

The destination where the AWS IoT FleetWise campaign sends data. You can send data to be stored in Amazon S3 or Amazon Timestream.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-datadestinationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-datadestinationconfig-syntax.json"></a>

```
{
  "[MqttTopicConfig](#cfn-iotfleetwise-campaign-datadestinationconfig-mqtttopicconfig)" : {{MqttTopicConfig}},
  "[S3Config](#cfn-iotfleetwise-campaign-datadestinationconfig-s3config)" : {{S3Config}},
  "[TimestreamConfig](#cfn-iotfleetwise-campaign-datadestinationconfig-timestreamconfig)" : {{TimestreamConfig}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-datadestinationconfig-syntax.yaml"></a>

```
  [MqttTopicConfig](#cfn-iotfleetwise-campaign-datadestinationconfig-mqtttopicconfig): {{
    MqttTopicConfig}}
  [S3Config](#cfn-iotfleetwise-campaign-datadestinationconfig-s3config): {{
    S3Config}}
  [TimestreamConfig](#cfn-iotfleetwise-campaign-datadestinationconfig-timestreamconfig): {{
    TimestreamConfig}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-datadestinationconfig-properties"></a>

`MqttTopicConfig`  <a name="cfn-iotfleetwise-campaign-datadestinationconfig-mqtttopicconfig"></a>
The MQTT topic to which the AWS IoT FleetWise campaign routes data.
*Required*: No
*Type*: [MqttTopicConfig](aws-properties-iotfleetwise-campaign-mqtttopicconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Config`  <a name="cfn-iotfleetwise-campaign-datadestinationconfig-s3config"></a>
 The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data.
*Required*: No
*Type*: [S3Config](aws-properties-iotfleetwise-campaign-s3config.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimestreamConfig`  <a name="cfn-iotfleetwise-campaign-datadestinationconfig-timestreamconfig"></a>
 The Amazon Timestream table where the campaign sends data.
*Required*: No
*Type*: [TimestreamConfig](aws-properties-iotfleetwise-campaign-timestreamconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
