---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-channelnamespace-handlerconfigs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace HandlerConfigs
<a name="aws-properties-appsync-channelnamespace-handlerconfigs"></a>

The `HandlerConfigs` property type specifies the configuration for the `OnPublish` and `OnSubscribe` handlers.

## Syntax
<a name="aws-properties-appsync-channelnamespace-handlerconfigs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-channelnamespace-handlerconfigs-syntax.json"></a>

```
{
  "[OnPublish](#cfn-appsync-channelnamespace-handlerconfigs-onpublish)" : {{HandlerConfig}},
  "[OnSubscribe](#cfn-appsync-channelnamespace-handlerconfigs-onsubscribe)" : {{HandlerConfig}}
}
```

### YAML
<a name="aws-properties-appsync-channelnamespace-handlerconfigs-syntax.yaml"></a>

```
  [OnPublish](#cfn-appsync-channelnamespace-handlerconfigs-onpublish): {{
    HandlerConfig}}
  [OnSubscribe](#cfn-appsync-channelnamespace-handlerconfigs-onsubscribe): {{
    HandlerConfig}}
```

## Properties
<a name="aws-properties-appsync-channelnamespace-handlerconfigs-properties"></a>

`OnPublish`  <a name="cfn-appsync-channelnamespace-handlerconfigs-onpublish"></a>
The configuration for the `OnPublish` handler.
*Required*: No
*Type*: [HandlerConfig](aws-properties-appsync-channelnamespace-handlerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnSubscribe`  <a name="cfn-appsync-channelnamespace-handlerconfigs-onsubscribe"></a>
The configuration for the `OnSubscribe` handler.
*Required*: No
*Type*: [HandlerConfig](aws-properties-appsync-channelnamespace-handlerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
