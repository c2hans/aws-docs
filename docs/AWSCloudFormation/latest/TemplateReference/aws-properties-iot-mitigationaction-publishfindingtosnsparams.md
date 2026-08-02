---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction PublishFindingToSnsParams
<a name="aws-properties-iot-mitigationaction-publishfindingtosnsparams"></a>

Parameters to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.

## Syntax
<a name="aws-properties-iot-mitigationaction-publishfindingtosnsparams-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-mitigationaction-publishfindingtosnsparams-syntax.json"></a>

```
{
  "[TopicArn](#cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-mitigationaction-publishfindingtosnsparams-syntax.yaml"></a>

```
  [TopicArn](#cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn): {{String}}
```

## Properties
<a name="aws-properties-iot-mitigationaction-publishfindingtosnsparams-properties"></a>

`TopicArn`  <a name="cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn"></a>
The ARN of the topic to which you want to publish the findings.
*Required*: Yes
*Type*: String
*Minimum*: `11`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
