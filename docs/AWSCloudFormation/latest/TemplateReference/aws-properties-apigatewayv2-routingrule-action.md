---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule Action
<a name="aws-properties-apigatewayv2-routingrule-action"></a>

Represents a routing rule action. The only supported action is `invokeApi`.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-action-syntax.json"></a>

```
{
  "[InvokeApi](#cfn-apigatewayv2-routingrule-action-invokeapi)" : {{ActionInvokeApi}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-action-syntax.yaml"></a>

```
  [InvokeApi](#cfn-apigatewayv2-routingrule-action-invokeapi): {{
    ActionInvokeApi}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-action-properties"></a>

`InvokeApi`  <a name="cfn-apigatewayv2-routingrule-action-invokeapi"></a>
Represents an InvokeApi action.
*Required*: Yes
*Type*: [ActionInvokeApi](aws-properties-apigatewayv2-routingrule-actioninvokeapi.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
