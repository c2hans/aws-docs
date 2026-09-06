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
