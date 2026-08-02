---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeEnrichmentHttpParameters
<a name="aws-properties-pipes-pipe-pipeenrichmenthttpparameters"></a>

These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations. In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.

## Syntax
<a name="aws-properties-pipes-pipe-pipeenrichmenthttpparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipeenrichmenthttpparameters-syntax.json"></a>

```
{
  "[HeaderParameters](#cfn-pipes-pipe-pipeenrichmenthttpparameters-headerparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PathParameterValues](#cfn-pipes-pipe-pipeenrichmenthttpparameters-pathparametervalues)" : {{[ String, ... ]}},
  "[QueryStringParameters](#cfn-pipes-pipe-pipeenrichmenthttpparameters-querystringparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipeenrichmenthttpparameters-syntax.yaml"></a>

```
  [HeaderParameters](#cfn-pipes-pipe-pipeenrichmenthttpparameters-headerparameters): {{
    {{Key}}: {{Value}}}}
  [PathParameterValues](#cfn-pipes-pipe-pipeenrichmenthttpparameters-pathparametervalues): {{
    - String}}
  [QueryStringParameters](#cfn-pipes-pipe-pipeenrichmenthttpparameters-querystringparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipeenrichmenthttpparameters-properties"></a>

`HeaderParameters`  <a name="cfn-pipes-pipe-pipeenrichmenthttpparameters-headerparameters"></a>
The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `^[!#$%&'*+-.^_`|~0-9a-zA-Z]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathParameterValues`  <a name="cfn-pipes-pipe-pipeenrichmenthttpparameters-pathparametervalues"></a>
The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("\*").
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringParameters`  <a name="cfn-pipes-pipe-pipeenrichmenthttpparameters-querystringparameters"></a>
The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `^[^\x00-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
