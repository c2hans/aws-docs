---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-channelnamespace-handlerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace HandlerConfig
<a name="aws-properties-appsync-channelnamespace-handlerconfig"></a>

The `HandlerConfig` property type specifies the configuration for the handler.

## Syntax
<a name="aws-properties-appsync-channelnamespace-handlerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-channelnamespace-handlerconfig-syntax.json"></a>

```
{
  "[Behavior](#cfn-appsync-channelnamespace-handlerconfig-behavior)" : {{String}},
  "[Integration](#cfn-appsync-channelnamespace-handlerconfig-integration)" : {{Integration}}
}
```

### YAML
<a name="aws-properties-appsync-channelnamespace-handlerconfig-syntax.yaml"></a>

```
  [Behavior](#cfn-appsync-channelnamespace-handlerconfig-behavior): {{String}}
  [Integration](#cfn-appsync-channelnamespace-handlerconfig-integration): {{
    Integration}}
```

## Properties
<a name="aws-properties-appsync-channelnamespace-handlerconfig-properties"></a>

`Behavior`  <a name="cfn-appsync-channelnamespace-handlerconfig-behavior"></a>
The behavior for the handler.
*Required*: Yes
*Type*: String
*Allowed values*: `CODE | DIRECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Integration`  <a name="cfn-appsync-channelnamespace-handlerconfig-integration"></a>
The integration data source configuration for the handler.
*Required*: Yes
*Type*: [Integration](aws-properties-appsync-channelnamespace-integration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
