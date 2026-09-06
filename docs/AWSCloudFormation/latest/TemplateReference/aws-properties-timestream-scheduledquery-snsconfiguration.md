---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-snsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery SnsConfiguration
<a name="aws-properties-timestream-scheduledquery-snsconfiguration"></a>

Details on SNS that are required to send the notification.

## Syntax
<a name="aws-properties-timestream-scheduledquery-snsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-snsconfiguration-syntax.json"></a>

```
{
  "[TopicArn](#cfn-timestream-scheduledquery-snsconfiguration-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-snsconfiguration-syntax.yaml"></a>

```
  [TopicArn](#cfn-timestream-scheduledquery-snsconfiguration-topicarn): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-snsconfiguration-properties"></a>

`TopicArn`  <a name="cfn-timestream-scheduledquery-snsconfiguration-topicarn"></a>
SNS topic ARN that the scheduled query status notifications will be sent to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
