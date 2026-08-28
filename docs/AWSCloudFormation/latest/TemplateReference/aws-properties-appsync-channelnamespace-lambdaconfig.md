---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-channelnamespace-lambdaconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace LambdaConfig
<a name="aws-properties-appsync-channelnamespace-lambdaconfig"></a>

The `LambdaConfig` property type specifies the integration configuration for a Lambda data source.

## Syntax
<a name="aws-properties-appsync-channelnamespace-lambdaconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-channelnamespace-lambdaconfig-syntax.json"></a>

```
{
  "[InvokeType](#cfn-appsync-channelnamespace-lambdaconfig-invoketype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-channelnamespace-lambdaconfig-syntax.yaml"></a>

```
  [InvokeType](#cfn-appsync-channelnamespace-lambdaconfig-invoketype): {{String}}
```

## Properties
<a name="aws-properties-appsync-channelnamespace-lambdaconfig-properties"></a>

`InvokeType`  <a name="cfn-appsync-channelnamespace-lambdaconfig-invoketype"></a>
The invocation type for a Lambda data source.
*Required*: Yes
*Type*: String
*Allowed values*: `REQUEST_RESPONSE | EVENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
