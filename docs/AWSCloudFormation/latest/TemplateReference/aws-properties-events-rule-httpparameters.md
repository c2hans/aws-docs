---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-httpparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule HttpParameters
<a name="aws-properties-events-rule-httpparameters"></a>

These are custom parameter to be used when the target is an API Gateway APIs or EventBridge ApiDestinations. In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.

## Syntax
<a name="aws-properties-events-rule-httpparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-httpparameters-syntax.json"></a>

```
{
  "[HeaderParameters](#cfn-events-rule-httpparameters-headerparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PathParameterValues](#cfn-events-rule-httpparameters-pathparametervalues)" : {{[ String, ... ]}},
  "[QueryStringParameters](#cfn-events-rule-httpparameters-querystringparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-events-rule-httpparameters-syntax.yaml"></a>

```
  [HeaderParameters](#cfn-events-rule-httpparameters-headerparameters): {{
    {{Key}}: {{Value}}}}
  [PathParameterValues](#cfn-events-rule-httpparameters-pathparametervalues): {{
    - String}}
  [QueryStringParameters](#cfn-events-rule-httpparameters-querystringparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-events-rule-httpparameters-properties"></a>

`HeaderParameters`  <a name="cfn-events-rule-httpparameters-headerparameters"></a>
The headers that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathParameterValues`  <a name="cfn-events-rule-httpparameters-pathparametervalues"></a>
The path parameter values to be used to populate API Gateway API or EventBridge ApiDestination path wildcards ("\*").
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringParameters`  <a name="cfn-events-rule-httpparameters-querystringparameters"></a>
The query string keys/values that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
