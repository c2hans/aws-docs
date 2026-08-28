---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-eventconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api EventConfig
<a name="aws-properties-appsync-api-eventconfig"></a>

Describes the authorization configuration for connections, message publishing, message subscriptions, and logging for an Event API.

## Syntax
<a name="aws-properties-appsync-api-eventconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-eventconfig-syntax.json"></a>

```
{
  "[AuthProviders](#cfn-appsync-api-eventconfig-authproviders)" : {{[ AuthProvider, ... ]}},
  "[ConnectionAuthModes](#cfn-appsync-api-eventconfig-connectionauthmodes)" : {{[ AuthMode, ... ]}},
  "[DefaultPublishAuthModes](#cfn-appsync-api-eventconfig-defaultpublishauthmodes)" : {{[ AuthMode, ... ]}},
  "[DefaultSubscribeAuthModes](#cfn-appsync-api-eventconfig-defaultsubscribeauthmodes)" : {{[ AuthMode, ... ]}},
  "[LogConfig](#cfn-appsync-api-eventconfig-logconfig)" : {{EventLogConfig}}
}
```

### YAML
<a name="aws-properties-appsync-api-eventconfig-syntax.yaml"></a>

```
  [AuthProviders](#cfn-appsync-api-eventconfig-authproviders): {{
    - AuthProvider}}
  [ConnectionAuthModes](#cfn-appsync-api-eventconfig-connectionauthmodes): {{
    - AuthMode}}
  [DefaultPublishAuthModes](#cfn-appsync-api-eventconfig-defaultpublishauthmodes): {{
    - AuthMode}}
  [DefaultSubscribeAuthModes](#cfn-appsync-api-eventconfig-defaultsubscribeauthmodes): {{
    - AuthMode}}
  [LogConfig](#cfn-appsync-api-eventconfig-logconfig): {{
    EventLogConfig}}
```

## Properties
<a name="aws-properties-appsync-api-eventconfig-properties"></a>

`AuthProviders`  <a name="cfn-appsync-api-eventconfig-authproviders"></a>
A list of authorization providers.
*Required*: Yes
*Type*: Array of [AuthProvider](aws-properties-appsync-api-authprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionAuthModes`  <a name="cfn-appsync-api-eventconfig-connectionauthmodes"></a>
A list of valid authorization modes for the Event API connections.
*Required*: Yes
*Type*: Array of [AuthMode](aws-properties-appsync-api-authmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultPublishAuthModes`  <a name="cfn-appsync-api-eventconfig-defaultpublishauthmodes"></a>
A list of valid authorization modes for the Event API publishing.
*Required*: Yes
*Type*: Array of [AuthMode](aws-properties-appsync-api-authmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultSubscribeAuthModes`  <a name="cfn-appsync-api-eventconfig-defaultsubscribeauthmodes"></a>
A list of valid authorization modes for the Event API subscriptions.
*Required*: Yes
*Type*: Array of [AuthMode](aws-properties-appsync-api-authmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfig`  <a name="cfn-appsync-api-eventconfig-logconfig"></a>
The CloudWatch Logs configuration for the Event API.
*Required*: No
*Type*: [EventLogConfig](aws-properties-appsync-api-eventlogconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
