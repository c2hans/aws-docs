---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-stage-accesslogsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::Stage AccessLogSettings
<a name="aws-properties-apigatewayv2-stage-accesslogsettings"></a>

Settings for logging access in a stage.

## Syntax
<a name="aws-properties-apigatewayv2-stage-accesslogsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-stage-accesslogsettings-syntax.json"></a>

```
{
  "[DestinationArn](#cfn-apigatewayv2-stage-accesslogsettings-destinationarn)" : {{String}},
  "[Format](#cfn-apigatewayv2-stage-accesslogsettings-format)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-stage-accesslogsettings-syntax.yaml"></a>

```
  [DestinationArn](#cfn-apigatewayv2-stage-accesslogsettings-destinationarn): {{String}}
  [Format](#cfn-apigatewayv2-stage-accesslogsettings-format): {{String}}
```

## Properties
<a name="aws-properties-apigatewayv2-stage-accesslogsettings-properties"></a>

`DestinationArn`  <a name="cfn-apigatewayv2-stage-accesslogsettings-destinationarn"></a>
The ARN of the CloudWatch Logs log group to receive access logs. This parameter is required to enable access logging.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-apigatewayv2-stage-accesslogsettings-format"></a>
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId. This parameter is required to enable access logging.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigatewayv2-stage-accesslogsettings--seealso"></a>
+ [Stages](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-stages.html) in the *Amazon API Gateway Version 2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
