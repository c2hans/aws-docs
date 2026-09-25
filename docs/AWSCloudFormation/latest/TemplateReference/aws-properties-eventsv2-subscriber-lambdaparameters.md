---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-lambdaparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber LambdaParameters
<a name="aws-properties-eventsv2-subscriber-lambdaparameters"></a>

Parameters for invoking an AWS Lambda function target.

## Syntax
<a name="aws-properties-eventsv2-subscriber-lambdaparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-lambdaparameters-syntax.json"></a>

```
{
  "[DurableExecutionName](#cfn-eventsv2-subscriber-lambdaparameters-durableexecutionname)" : {{String}},
  "[InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-lambdaparameters-invocationtimeoutseconds)" : {{String}},
  "[InvocationType](#cfn-eventsv2-subscriber-lambdaparameters-invocationtype)" : {{String}},
  "[Qualifier](#cfn-eventsv2-subscriber-lambdaparameters-qualifier)" : {{String}},
  "[TenantId](#cfn-eventsv2-subscriber-lambdaparameters-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-lambdaparameters-syntax.yaml"></a>

```
  [DurableExecutionName](#cfn-eventsv2-subscriber-lambdaparameters-durableexecutionname): {{String}}
  [InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-lambdaparameters-invocationtimeoutseconds): {{String}}
  [InvocationType](#cfn-eventsv2-subscriber-lambdaparameters-invocationtype): {{String}}
  [Qualifier](#cfn-eventsv2-subscriber-lambdaparameters-qualifier): {{String}}
  [TenantId](#cfn-eventsv2-subscriber-lambdaparameters-tenantid): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-lambdaparameters-properties"></a>

`DurableExecutionName`  <a name="cfn-eventsv2-subscriber-lambdaparameters-durableexecutionname"></a>
A unique name for a durable function execution. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationTimeoutSeconds`  <a name="cfn-eventsv2-subscriber-lambdaparameters-invocationtimeoutseconds"></a>
The timeout in seconds for each invocation of the target, written as a string. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationType`  <a name="cfn-eventsv2-subscriber-lambdaparameters-invocationtype"></a>
How the function is invoked: EVENT (asynchronous) or REQUEST\_RESPONSE (synchronous).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Qualifier`  <a name="cfn-eventsv2-subscriber-lambdaparameters-qualifier"></a>
The version or alias of the Lambda function to invoke. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantId`  <a name="cfn-eventsv2-subscriber-lambdaparameters-tenantid"></a>
The tenant identifier for multi-tenant Lambda functions. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
