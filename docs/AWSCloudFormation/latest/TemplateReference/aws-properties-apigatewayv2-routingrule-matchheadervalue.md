---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-matchheadervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule MatchHeaderValue
<a name="aws-properties-apigatewayv2-routingrule-matchheadervalue"></a>

Represents a `MatchHeaderValue`.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-matchheadervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-matchheadervalue-syntax.json"></a>

```
{
  "[Header](#cfn-apigatewayv2-routingrule-matchheadervalue-header)" : {{String}},
  "[ValueGlob](#cfn-apigatewayv2-routingrule-matchheadervalue-valueglob)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-matchheadervalue-syntax.yaml"></a>

```
  [Header](#cfn-apigatewayv2-routingrule-matchheadervalue-header): {{String}}
  [ValueGlob](#cfn-apigatewayv2-routingrule-matchheadervalue-valueglob): {{String}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-matchheadervalue-properties"></a>

`Header`  <a name="cfn-apigatewayv2-routingrule-matchheadervalue-header"></a>
The case insensitive header name to be matched. The header name must be less than 40 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`|~.`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueGlob`  <a name="cfn-apigatewayv2-routingrule-matchheadervalue-valueglob"></a>
The case sensitive header glob value to be matched against entire header value. The header glob value must be less than 128 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`|~`. Wildcard matching is supported for header glob values but must be for `*prefix-match`, `suffix-match*`, or `*infix*-match`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
