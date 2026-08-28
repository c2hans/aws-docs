---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-channelnamespace-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace Integration
<a name="aws-properties-appsync-channelnamespace-integration"></a>

The `Integration` property type specifies the integration data source configuration for the handler.

## Syntax
<a name="aws-properties-appsync-channelnamespace-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-channelnamespace-integration-syntax.json"></a>

```
{
  "[DataSourceName](#cfn-appsync-channelnamespace-integration-datasourcename)" : {{String}},
  "[LambdaConfig](#cfn-appsync-channelnamespace-integration-lambdaconfig)" : {{LambdaConfig}}
}
```

### YAML
<a name="aws-properties-appsync-channelnamespace-integration-syntax.yaml"></a>

```
  [DataSourceName](#cfn-appsync-channelnamespace-integration-datasourcename): {{String}}
  [LambdaConfig](#cfn-appsync-channelnamespace-integration-lambdaconfig): {{
    LambdaConfig}}
```

## Properties
<a name="aws-properties-appsync-channelnamespace-integration-properties"></a>

`DataSourceName`  <a name="cfn-appsync-channelnamespace-integration-datasourcename"></a>
The unique name of the data source that has been configured on the API.
*Required*: Yes
*Type*: String
*Pattern*: `([_A-Za-z][_0-9A-Za-z]{0,511})?`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaConfig`  <a name="cfn-appsync-channelnamespace-integration-lambdaconfig"></a>
The configuration for a Lambda data source.
*Required*: No
*Type*: [LambdaConfig](aws-properties-appsync-channelnamespace-lambdaconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
