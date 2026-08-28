---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-usageplan-throttlesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::UsagePlan ThrottleSettings
<a name="aws-properties-apigateway-usageplan-throttlesettings"></a>

`ThrottleSettings` is a property of the [AWS::ApiGateway::UsagePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html) resource that specifies the overall request rate (average requests per second) and burst capacity when users call your REST APIs.

## Syntax
<a name="aws-properties-apigateway-usageplan-throttlesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-usageplan-throttlesettings-syntax.json"></a>

```
{
  "[BurstLimit](#cfn-apigateway-usageplan-throttlesettings-burstlimit)" : {{Integer}},
  "[RateLimit](#cfn-apigateway-usageplan-throttlesettings-ratelimit)" : {{Number}}
}
```

### YAML
<a name="aws-properties-apigateway-usageplan-throttlesettings-syntax.yaml"></a>

```
  [BurstLimit](#cfn-apigateway-usageplan-throttlesettings-burstlimit): {{Integer}}
  [RateLimit](#cfn-apigateway-usageplan-throttlesettings-ratelimit): {{Number}}
```

## Properties
<a name="aws-properties-apigateway-usageplan-throttlesettings-properties"></a>

`BurstLimit`  <a name="cfn-apigateway-usageplan-throttlesettings-burstlimit"></a>
The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateLimit`  <a name="cfn-apigateway-usageplan-throttlesettings-ratelimit"></a>
The API target request rate limit.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigateway-usageplan-throttlesettings--seealso"></a>
+ [UsagePlan](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
