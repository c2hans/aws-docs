---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::LogDeliveryConfiguration CloudWatchLogsConfiguration
<a name="aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration"></a>

Configuration for the CloudWatch log group destination of user pool detailed activity logging, or of user activity log export with advanced security features.

## Syntax
<a name="aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-properties"></a>

`LogGroupArn`  <a name="cfn-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration-loggrouparn"></a>
The Amazon Resource Name (arn) of a CloudWatch Logs log group where your user pool sends logs. The log group must not be encrypted with AWS Key Management Service and must be in the same AWS account as your user pool.
To send logs to log groups with a resource policy of a size greater than 5120 characters, configure a log group with a path that starts with `/aws/vendedlogs`. For more information, see [Enabling logging from certain AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
