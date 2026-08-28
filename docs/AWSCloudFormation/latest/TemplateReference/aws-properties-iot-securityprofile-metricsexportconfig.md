---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-metricsexportconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile MetricsExportConfig
<a name="aws-properties-iot-securityprofile-metricsexportconfig"></a>

Specifies the MQTT topic and role ARN required for metric export.

## Syntax
<a name="aws-properties-iot-securityprofile-metricsexportconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-metricsexportconfig-syntax.json"></a>

```
{
  "[MqttTopic](#cfn-iot-securityprofile-metricsexportconfig-mqtttopic)" : {{String}},
  "[RoleArn](#cfn-iot-securityprofile-metricsexportconfig-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-metricsexportconfig-syntax.yaml"></a>

```
  [MqttTopic](#cfn-iot-securityprofile-metricsexportconfig-mqtttopic): {{String}}
  [RoleArn](#cfn-iot-securityprofile-metricsexportconfig-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-metricsexportconfig-properties"></a>

`MqttTopic`  <a name="cfn-iot-securityprofile-metricsexportconfig-mqtttopic"></a>
The MQTT topic that Device Defender Detect should publish messages to for metrics export.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-securityprofile-metricsexportconfig-rolearn"></a>
This role ARN has permission to publish MQTT messages, after which Device Defender Detect can assume the role and publish messages on your behalf.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
