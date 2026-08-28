---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-autoscaling.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector AutoScaling
<a name="aws-properties-kafkaconnect-connector-autoscaling"></a>

Specifies how the connector scales.

## Syntax
<a name="aws-properties-kafkaconnect-connector-autoscaling-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-autoscaling-syntax.json"></a>

```
{
  "[MaxAutoscalingTaskCount](#cfn-kafkaconnect-connector-autoscaling-maxautoscalingtaskcount)" : {{Integer}},
  "[MaxWorkerCount](#cfn-kafkaconnect-connector-autoscaling-maxworkercount)" : {{Integer}},
  "[McuCount](#cfn-kafkaconnect-connector-autoscaling-mcucount)" : {{Integer}},
  "[MinWorkerCount](#cfn-kafkaconnect-connector-autoscaling-minworkercount)" : {{Integer}},
  "[ScaleInPolicy](#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy)" : {{ScaleInPolicy}},
  "[ScaleOutPolicy](#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy)" : {{ScaleOutPolicy}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-autoscaling-syntax.yaml"></a>

```
  [MaxAutoscalingTaskCount](#cfn-kafkaconnect-connector-autoscaling-maxautoscalingtaskcount): {{Integer}}
  [MaxWorkerCount](#cfn-kafkaconnect-connector-autoscaling-maxworkercount): {{Integer}}
  [McuCount](#cfn-kafkaconnect-connector-autoscaling-mcucount): {{Integer}}
  [MinWorkerCount](#cfn-kafkaconnect-connector-autoscaling-minworkercount): {{Integer}}
  [ScaleInPolicy](#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy): {{
    ScaleInPolicy}}
  [ScaleOutPolicy](#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy): {{
    ScaleOutPolicy}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-autoscaling-properties"></a>

`MaxAutoscalingTaskCount`  <a name="cfn-kafkaconnect-connector-autoscaling-maxautoscalingtaskcount"></a>
The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxWorkerCount`  <a name="cfn-kafkaconnect-connector-autoscaling-maxworkercount"></a>
The maximum number of workers allocated to the connector.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McuCount`  <a name="cfn-kafkaconnect-connector-autoscaling-mcucount"></a>
The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.
*Required*: Yes
*Type*: Integer
*Allowed values*: `1 | 2 | 4 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinWorkerCount`  <a name="cfn-kafkaconnect-connector-autoscaling-minworkercount"></a>
The minimum number of workers allocated to the connector.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleInPolicy`  <a name="cfn-kafkaconnect-connector-autoscaling-scaleinpolicy"></a>
The scale-in policy for the connector.
*Required*: Yes
*Type*: [ScaleInPolicy](aws-properties-kafkaconnect-connector-scaleinpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleOutPolicy`  <a name="cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy"></a>
The scale-out policy for the connector.
*Required*: Yes
*Type*: [ScaleOutPolicy](aws-properties-kafkaconnect-connector-scaleoutpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
