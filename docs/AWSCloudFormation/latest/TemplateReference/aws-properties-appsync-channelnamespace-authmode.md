---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-channelnamespace-authmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace AuthMode
<a name="aws-properties-appsync-channelnamespace-authmode"></a>

Describes an authorization configuration. Use `AuthMode` to specify the publishing and subscription authorization configuration for an Event API.

## Syntax
<a name="aws-properties-appsync-channelnamespace-authmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-channelnamespace-authmode-syntax.json"></a>

```
{
  "[AuthType](#cfn-appsync-channelnamespace-authmode-authtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-channelnamespace-authmode-syntax.yaml"></a>

```
  [AuthType](#cfn-appsync-channelnamespace-authmode-authtype): {{String}}
```

## Properties
<a name="aws-properties-appsync-channelnamespace-authmode-properties"></a>

`AuthType`  <a name="cfn-appsync-channelnamespace-authmode-authtype"></a>
The authorization type.
*Required*: No
*Type*: String
*Allowed values*: `AMAZON_COGNITO_USER_POOLS | AWS_IAM | API_KEY | OPENID_CONNECT | AWS_LAMBDA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
