---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargethttpparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetHttpParameters
<a name="aws-properties-pipes-pipe-pipetargethttpparameters"></a>

These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargethttpparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargethttpparameters-syntax.json"></a>

```
{
  "[HeaderParameters](#cfn-pipes-pipe-pipetargethttpparameters-headerparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PathParameterValues](#cfn-pipes-pipe-pipetargethttpparameters-pathparametervalues)" : {{[ String, ... ]}},
  "[QueryStringParameters](#cfn-pipes-pipe-pipetargethttpparameters-querystringparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargethttpparameters-syntax.yaml"></a>

```
  [HeaderParameters](#cfn-pipes-pipe-pipetargethttpparameters-headerparameters): {{
    {{Key}}: {{Value}}}}
  [PathParameterValues](#cfn-pipes-pipe-pipetargethttpparameters-pathparametervalues): {{
    - String}}
  [QueryStringParameters](#cfn-pipes-pipe-pipetargethttpparameters-querystringparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargethttpparameters-properties"></a>

`HeaderParameters`  <a name="cfn-pipes-pipe-pipetargethttpparameters-headerparameters"></a>
The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `^[!#$%&'*+-.^_`|~0-9a-zA-Z]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathParameterValues`  <a name="cfn-pipes-pipe-pipetargethttpparameters-pathparametervalues"></a>
The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("\*").
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringParameters`  <a name="cfn-pipes-pipe-pipetargethttpparameters-querystringparameters"></a>
The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `^[^\x00-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
