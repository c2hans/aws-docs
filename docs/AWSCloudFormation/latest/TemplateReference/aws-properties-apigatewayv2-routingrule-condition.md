---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule Condition
<a name="aws-properties-apigatewayv2-routingrule-condition"></a>

Represents a condition. Conditions can contain up to two `matchHeaders` conditions and one `matchBasePaths` conditions. API Gateway evaluates header conditions and base path conditions together. You can only use AND between header and base path conditions.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-condition-syntax.json"></a>

```
{
  "[MatchBasePaths](#cfn-apigatewayv2-routingrule-condition-matchbasepaths)" : {{MatchBasePaths}},
  "[MatchHeaders](#cfn-apigatewayv2-routingrule-condition-matchheaders)" : {{MatchHeaders}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-condition-syntax.yaml"></a>

```
  [MatchBasePaths](#cfn-apigatewayv2-routingrule-condition-matchbasepaths): {{
    MatchBasePaths}}
  [MatchHeaders](#cfn-apigatewayv2-routingrule-condition-matchheaders): {{
    MatchHeaders}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-condition-properties"></a>

`MatchBasePaths`  <a name="cfn-apigatewayv2-routingrule-condition-matchbasepaths"></a>
The base path to be matched.
*Required*: No
*Type*: [MatchBasePaths](aws-properties-apigatewayv2-routingrule-matchbasepaths.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchHeaders`  <a name="cfn-apigatewayv2-routingrule-condition-matchheaders"></a>
The headers to be matched.
*Required*: No
*Type*: [MatchHeaders](aws-properties-apigatewayv2-routingrule-matchheaders.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
