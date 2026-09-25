---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-invokeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber InvokeConfiguration
<a name="aws-properties-eventsv2-subscriber-invokeconfiguration"></a>

Configuration for how the subscriber invokes its target. Specify the target ARN, the IAM role, and, optionally, the target-specific parameters object that matches the target type.

## Syntax
<a name="aws-properties-eventsv2-subscriber-invokeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-invokeconfiguration-syntax.json"></a>

```
{
  "[EventBusV2Parameters](#cfn-eventsv2-subscriber-invokeconfiguration-eventbusv2parameters)" : {{EventBusV2Parameters}},
  "[HttpParameters](#cfn-eventsv2-subscriber-invokeconfiguration-httpparameters)" : {{HttpParameters}},
  "[KinesisParameters](#cfn-eventsv2-subscriber-invokeconfiguration-kinesisparameters)" : {{KinesisParameters}},
  "[LambdaParameters](#cfn-eventsv2-subscriber-invokeconfiguration-lambdaparameters)" : {{LambdaParameters}},
  "[RoleArn](#cfn-eventsv2-subscriber-invokeconfiguration-rolearn)" : {{String}},
  "[SnsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-snsparameters)" : {{SnsParameters}},
  "[SqsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-sqsparameters)" : {{SqsParameters}},
  "[StepFunctionsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-stepfunctionsparameters)" : {{StepFunctionsParameters}},
  "[TargetArn](#cfn-eventsv2-subscriber-invokeconfiguration-targetarn)" : {{String}},
  "[UniversalTargetParameters](#cfn-eventsv2-subscriber-invokeconfiguration-universaltargetparameters)" : {{UniversalTargetParameters}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-invokeconfiguration-syntax.yaml"></a>

```
  [EventBusV2Parameters](#cfn-eventsv2-subscriber-invokeconfiguration-eventbusv2parameters): {{
    EventBusV2Parameters}}
  [HttpParameters](#cfn-eventsv2-subscriber-invokeconfiguration-httpparameters): {{
    HttpParameters}}
  [KinesisParameters](#cfn-eventsv2-subscriber-invokeconfiguration-kinesisparameters): {{
    KinesisParameters}}
  [LambdaParameters](#cfn-eventsv2-subscriber-invokeconfiguration-lambdaparameters): {{
    LambdaParameters}}
  [RoleArn](#cfn-eventsv2-subscriber-invokeconfiguration-rolearn): {{String}}
  [SnsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-snsparameters): {{
    SnsParameters}}
  [SqsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-sqsparameters): {{
    SqsParameters}}
  [StepFunctionsParameters](#cfn-eventsv2-subscriber-invokeconfiguration-stepfunctionsparameters): {{
    StepFunctionsParameters}}
  [TargetArn](#cfn-eventsv2-subscriber-invokeconfiguration-targetarn): {{String}}
  [UniversalTargetParameters](#cfn-eventsv2-subscriber-invokeconfiguration-universaltargetparameters): {{
    UniversalTargetParameters}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-invokeconfiguration-properties"></a>

`EventBusV2Parameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-eventbusv2parameters"></a>
Parameters for forwarding events to another EventBridge event bus, used when TargetArn is an event bus ARN of the form arn:{partition}:events:{region}:{account}:event-busv2/{name}/{id}.
*Required*: No
*Type*: [EventBusV2Parameters](aws-properties-eventsv2-subscriber-eventbusv2parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-httpparameters"></a>
Parameters for invoking an HTTP endpoint target, such as an Amazon API Gateway endpoint or an EventBridge API destination.
*Required*: No
*Type*: [HttpParameters](aws-properties-eventsv2-subscriber-httpparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-kinesisparameters"></a>
Parameters for writing events to an Amazon Kinesis Data Streams target.
*Required*: No
*Type*: [KinesisParameters](aws-properties-eventsv2-subscriber-kinesisparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-lambdaparameters"></a>
Parameters for invoking an AWS Lambda function target.
*Required*: No
*Type*: [LambdaParameters](aws-properties-eventsv2-subscriber-lambdaparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-rolearn"></a>
The ARN of the IAM role the service assumes to invoke the target. The role must belong to the same account as the subscriber.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:iam::\d{12}:role\/[\w+=,.@/-]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-snsparameters"></a>
Parameters for publishing events to an Amazon SNS topic target.
*Required*: No
*Type*: [SnsParameters](aws-properties-eventsv2-subscriber-snsparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqsParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-sqsparameters"></a>
Parameters for sending events to an Amazon SQS queue target.
*Required*: No
*Type*: [SqsParameters](aws-properties-eventsv2-subscriber-sqsparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepFunctionsParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-stepfunctionsparameters"></a>
Parameters for starting an AWS Step Functions state machine execution target.
*Required*: No
*Type*: [StepFunctionsParameters](aws-properties-eventsv2-subscriber-stepfunctionsparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-targetarn"></a>
The Amazon Resource Name (ARN) of the target that the subscriber invokes. For universal service integration targets, use the form arn:{partition}:events:::aws-sdk:{service}:{apiAction}.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UniversalTargetParameters`  <a name="cfn-eventsv2-subscriber-invokeconfiguration-universaltargetparameters"></a>
Parameters for invoking an AWS service API as a universal service integration target, used when TargetArn has the form arn:{partition}:events:::aws-sdk:{service}:{apiAction}.
*Required*: No
*Type*: [UniversalTargetParameters](aws-properties-eventsv2-subscriber-universaltargetparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
