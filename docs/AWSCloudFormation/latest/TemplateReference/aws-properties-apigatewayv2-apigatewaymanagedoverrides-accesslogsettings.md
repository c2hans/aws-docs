---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::ApiGatewayManagedOverrides AccessLogSettings
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings"></a>

The `AccessLogSettings` property overrides the access log settings for an API Gateway-managed stage.

## Syntax
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-syntax.json"></a>

```
{
  "[DestinationArn](#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn)" : {{String}},
  "[Format](#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-syntax.yaml"></a>

```
  [DestinationArn](#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn): {{String}}
  [Format](#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format): {{String}}
```

## Properties
<a name="aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-properties"></a>

`DestinationArn`  <a name="cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn"></a>
The ARN of the CloudWatch Logs log group to receive access logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format"></a>
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
