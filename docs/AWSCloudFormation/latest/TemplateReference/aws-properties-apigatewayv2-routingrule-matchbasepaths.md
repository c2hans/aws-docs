---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-matchbasepaths.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule MatchBasePaths
<a name="aws-properties-apigatewayv2-routingrule-matchbasepaths"></a>

Represents a `MatchBasePaths` condition.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-matchbasepaths-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-matchbasepaths-syntax.json"></a>

```
{
  "[AnyOf](#cfn-apigatewayv2-routingrule-matchbasepaths-anyof)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-matchbasepaths-syntax.yaml"></a>

```
  [AnyOf](#cfn-apigatewayv2-routingrule-matchbasepaths-anyof): {{
    - String}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-matchbasepaths-properties"></a>

`AnyOf`  <a name="cfn-apigatewayv2-routingrule-matchbasepaths-anyof"></a>
The string of the case sensitive base path to be matched.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
