---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-matchheaders.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule MatchHeaders
<a name="aws-properties-apigatewayv2-routingrule-matchheaders"></a>

Represents a `MatchHeaders` condition.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-matchheaders-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-matchheaders-syntax.json"></a>

```
{
  "[AnyOf](#cfn-apigatewayv2-routingrule-matchheaders-anyof)" : {{[ MatchHeaderValue, ... ]}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-matchheaders-syntax.yaml"></a>

```
  [AnyOf](#cfn-apigatewayv2-routingrule-matchheaders-anyof): {{
    - MatchHeaderValue}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-matchheaders-properties"></a>

`AnyOf`  <a name="cfn-apigatewayv2-routingrule-matchheaders-anyof"></a>
The header name and header value glob to be matched. The matchHeaders condition is matched if any of the header name and header value globs are matched.
*Required*: Yes
*Type*: Array of [MatchHeaderValue](aws-properties-apigatewayv2-routingrule-matchheadervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
