---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachine CloudWatchLogsLogGroup
<a name="aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup"></a>

Defines a CloudWatch log group.

**Note**
For more information see [Standard Versus Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) in the AWS Step Functions Developer Guide.

## Syntax
<a name="aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup-properties"></a>

`LogGroupArn`  <a name="cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn"></a>
The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with `:*`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
