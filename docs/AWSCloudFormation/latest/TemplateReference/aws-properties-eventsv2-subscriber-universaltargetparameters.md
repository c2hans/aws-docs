---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-universaltargetparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber UniversalTargetParameters
<a name="aws-properties-eventsv2-subscriber-universaltargetparameters"></a>

Parameters for invoking an AWS service API as a universal service integration target, used when TargetArn has the form arn:{partition}:events:::aws-sdk:{service}:{apiAction}.

## Syntax
<a name="aws-properties-eventsv2-subscriber-universaltargetparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-universaltargetparameters-syntax.json"></a>

```
{
  "[Input](#cfn-eventsv2-subscriber-universaltargetparameters-input)" : {{String}},
  "[InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-universaltargetparameters-invocationtimeoutseconds)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-universaltargetparameters-syntax.yaml"></a>

```
  [Input](#cfn-eventsv2-subscriber-universaltargetparameters-input): {{String}}
  [InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-universaltargetparameters-invocationtimeoutseconds): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-universaltargetparameters-properties"></a>

`Input`  <a name="cfn-eventsv2-subscriber-universaltargetparameters-input"></a>
JSON string or JSONata expression that produces the API request. Supports {% ... %} JSONata expressions for dynamic values from the event.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `262144`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationTimeoutSeconds`  <a name="cfn-eventsv2-subscriber-universaltargetparameters-invocationtimeoutseconds"></a>
Timeout in seconds for each invocation of the target (1-30, default 30). Must be a literal integer written as a string; JSONata expressions are not supported for this field.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
