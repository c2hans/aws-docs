---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-routingrule-actioninvokeapi.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::RoutingRule ActionInvokeApi
<a name="aws-properties-apigatewayv2-routingrule-actioninvokeapi"></a>

Represents an InvokeApi action.

## Syntax
<a name="aws-properties-apigatewayv2-routingrule-actioninvokeapi-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-routingrule-actioninvokeapi-syntax.json"></a>

```
{
  "[ApiId](#cfn-apigatewayv2-routingrule-actioninvokeapi-apiid)" : {{String}},
  "[Stage](#cfn-apigatewayv2-routingrule-actioninvokeapi-stage)" : {{String}},
  "[StripBasePath](#cfn-apigatewayv2-routingrule-actioninvokeapi-stripbasepath)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-routingrule-actioninvokeapi-syntax.yaml"></a>

```
  [ApiId](#cfn-apigatewayv2-routingrule-actioninvokeapi-apiid): {{String}}
  [Stage](#cfn-apigatewayv2-routingrule-actioninvokeapi-stage): {{String}}
  [StripBasePath](#cfn-apigatewayv2-routingrule-actioninvokeapi-stripbasepath): {{Boolean}}
```

## Properties
<a name="aws-properties-apigatewayv2-routingrule-actioninvokeapi-properties"></a>

`ApiId`  <a name="cfn-apigatewayv2-routingrule-actioninvokeapi-apiid"></a>
The API identifier of the target API.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-apigatewayv2-routingrule-actioninvokeapi-stage"></a>
The name of the target stage.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripBasePath`  <a name="cfn-apigatewayv2-routingrule-actioninvokeapi-stripbasepath"></a>
The strip base path setting. When true, API Gateway strips the incoming matched base path when forwarding the request to the target API.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
