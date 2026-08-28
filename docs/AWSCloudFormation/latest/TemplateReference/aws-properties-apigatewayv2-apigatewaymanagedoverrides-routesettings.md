---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::ApiGatewayManagedOverrides RouteSettings
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings"></a>

The `RouteSettings` property overrides the route settings for an API Gateway-managed route.

## Syntax
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings-syntax.json"></a>

```
{
  "[DetailedMetricsEnabled](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled)" : {{Boolean}},
  "[ThrottlingBurstLimit](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit)" : {{Integer}},
  "[ThrottlingRateLimit](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit)" : {{Number}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings-syntax.yaml"></a>

```
  [DetailedMetricsEnabled](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled): {{Boolean}}
  [ThrottlingBurstLimit](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit): {{Integer}}
  [ThrottlingRateLimit](#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit): {{Number}}
```

## Properties
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings-properties"></a>

`DetailedMetricsEnabled`  <a name="cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled"></a>
Specifies whether detailed metrics are enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottlingBurstLimit`  <a name="cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit"></a>
Specifies the throttling burst limit.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottlingRateLimit`  <a name="cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit"></a>
Specifies the throttling rate limit.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
