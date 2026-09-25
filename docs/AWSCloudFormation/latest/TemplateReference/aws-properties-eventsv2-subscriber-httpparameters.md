---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-httpparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber HttpParameters
<a name="aws-properties-eventsv2-subscriber-httpparameters"></a>

Parameters for invoking an HTTP endpoint target, such as an Amazon API Gateway endpoint or an EventBridge API destination.

## Syntax
<a name="aws-properties-eventsv2-subscriber-httpparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-httpparameters-syntax.json"></a>

```
{
  "[HeaderParameters](#cfn-eventsv2-subscriber-httpparameters-headerparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-httpparameters-invocationtimeoutseconds)" : {{String}},
  "[PathParameterValues](#cfn-eventsv2-subscriber-httpparameters-pathparametervalues)" : {{[ String, ... ]}},
  "[QueryStringParameters](#cfn-eventsv2-subscriber-httpparameters-querystringparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-httpparameters-syntax.yaml"></a>

```
  [HeaderParameters](#cfn-eventsv2-subscriber-httpparameters-headerparameters): {{
    {{Key}}: {{Value}}}}
  [InvocationTimeoutSeconds](#cfn-eventsv2-subscriber-httpparameters-invocationtimeoutseconds): {{String}}
  [PathParameterValues](#cfn-eventsv2-subscriber-httpparameters-pathparametervalues): {{
    - String}}
  [QueryStringParameters](#cfn-eventsv2-subscriber-httpparameters-querystringparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-httpparameters-properties"></a>

`HeaderParameters`  <a name="cfn-eventsv2-subscriber-httpparameters-headerparameters"></a>
A map of HTTP header names to values. A header name or value may also be a JSONata expression.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?=[\s\S]{1,512}$)([!#$%&'*+\-.^_`|~0-9a-zA-Z]+|\{%[\s\S]+?%\})$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationTimeoutSeconds`  <a name="cfn-eventsv2-subscriber-httpparameters-invocationtimeoutseconds"></a>
The timeout in seconds for each invocation of the target, written as a string. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathParameterValues`  <a name="cfn-eventsv2-subscriber-httpparameters-pathparametervalues"></a>
Values for the path parameters (wildcards) in the target URL, in order.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringParameters`  <a name="cfn-eventsv2-subscriber-httpparameters-querystringparameters"></a>
A map of query string parameter names to values.
*Required*: No
*Type*: Object of String
*Pattern*: `^[^\u0000-\u001F\u007F]{1,512}$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
