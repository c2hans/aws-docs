---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-stepfunctionsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber StepFunctionsParameters
<a name="aws-properties-eventsv2-subscriber-stepfunctionsparameters"></a>

Parameters for starting an AWS Step Functions state machine execution target.

## Syntax
<a name="aws-properties-eventsv2-subscriber-stepfunctionsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-stepfunctionsparameters-syntax.json"></a>

```
{
  "[InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtimeoutseconds)" : {{String}},
  "[InvocationType](#cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtype)" : {{String}},
  "[Name](#cfn-eventsv2-subscriber-stepfunctionsparameters-name)" : {{String}},
  "[TraceHeader](#cfn-eventsv2-subscriber-stepfunctionsparameters-traceheader)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-stepfunctionsparameters-syntax.yaml"></a>

```
  [InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtimeoutseconds): {{String}}
  [InvocationType](#cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtype): {{String}}
  [Name](#cfn-eventsv2-subscriber-stepfunctionsparameters-name): {{String}}
  [TraceHeader](#cfn-eventsv2-subscriber-stepfunctionsparameters-traceheader): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-stepfunctionsparameters-properties"></a>

`InvocationTimeoutSeconds`  <a name="cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtimeoutseconds"></a>
The timeout in seconds for each invocation of the target, written as a string. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationType`  <a name="cfn-eventsv2-subscriber-stepfunctionsparameters-invocationtype"></a>
How the execution is started: EVENT (StartExecution, asynchronous) or REQUEST\_RESPONSE (StartSyncExecution, synchronous).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-eventsv2-subscriber-stepfunctionsparameters-name"></a>
A name for the execution. Must be unique for the account, Region, and state machine. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TraceHeader`  <a name="cfn-eventsv2-subscriber-stepfunctionsparameters-traceheader"></a>
The AWS X-Ray trace header for distributed tracing. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
