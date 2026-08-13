---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-channelnamespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ChannelNamespace
<a name="aws-resource-appsync-channelnamespace"></a>

The `AWS::AppSync::ChannelNamespace` resource creates a channel namespace associated with an `Api`. The `ChannelNamespace` contains the definitions for code handlers for the `Api`.

## Syntax
<a name="aws-resource-appsync-channelnamespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appsync-channelnamespace-syntax.json"></a>

```
{
  "Type" : "AWS::AppSync::ChannelNamespace",
  "Properties" : {
      "[ApiId](#cfn-appsync-channelnamespace-apiid)" : {{String}},
      "[CodeHandlers](#cfn-appsync-channelnamespace-codehandlers)" : {{String}},
      "[CodeS3Location](#cfn-appsync-channelnamespace-codes3location)" : {{String}},
      "[HandlerConfigs](#cfn-appsync-channelnamespace-handlerconfigs)" : {{HandlerConfigs}},
      "[Name](#cfn-appsync-channelnamespace-name)" : {{String}},
      "[PublishAuthModes](#cfn-appsync-channelnamespace-publishauthmodes)" : {{[ AuthMode, ... ]}},
      "[SubscribeAuthModes](#cfn-appsync-channelnamespace-subscribeauthmodes)" : {{[ AuthMode, ... ]}},
      "[Tags](#cfn-appsync-channelnamespace-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appsync-channelnamespace-syntax.yaml"></a>

```
Type: AWS::AppSync::ChannelNamespace
Properties:
  [ApiId](#cfn-appsync-channelnamespace-apiid): {{String}}
  [CodeHandlers](#cfn-appsync-channelnamespace-codehandlers): {{String}}
  [CodeS3Location](#cfn-appsync-channelnamespace-codes3location): {{String}}
  [HandlerConfigs](#cfn-appsync-channelnamespace-handlerconfigs): {{
    HandlerConfigs}}
  [Name](#cfn-appsync-channelnamespace-name): {{String}}
  [PublishAuthModes](#cfn-appsync-channelnamespace-publishauthmodes): {{
    - AuthMode}}
  [SubscribeAuthModes](#cfn-appsync-channelnamespace-subscribeauthmodes): {{
    - AuthMode}}
  [Tags](#cfn-appsync-channelnamespace-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appsync-channelnamespace-properties"></a>

`ApiId`  <a name="cfn-appsync-channelnamespace-apiid"></a>
The `Api` ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeHandlers`  <a name="cfn-appsync-channelnamespace-codehandlers"></a>
The event handler functions that run custom business logic to process published events and subscribe requests.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeS3Location`  <a name="cfn-appsync-channelnamespace-codes3location"></a>
The Amazon S3 endpoint where the code is located.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HandlerConfigs`  <a name="cfn-appsync-channelnamespace-handlerconfigs"></a>
The configuration for the `OnPublish` and `OnSubscribe` handlers.
*Required*: No
*Type*: [HandlerConfigs](aws-properties-appsync-channelnamespace-handlerconfigs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appsync-channelnamespace-name"></a>
The name of the channel namespace. This name must be unique within the `Api`.
*Required*: Yes
*Type*: String
*Pattern*: `([A-Za-z0-9](?:[A-Za-z0-9\-]{0,48}[A-Za-z0-9])?)`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublishAuthModes`  <a name="cfn-appsync-channelnamespace-publishauthmodes"></a>
The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default `Api`authorization configuration.
*Required*: No
*Type*: Array of [AuthMode](aws-properties-appsync-channelnamespace-authmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscribeAuthModes`  <a name="cfn-appsync-channelnamespace-subscribeauthmodes"></a>
The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default `Api`authorization configuration.
*Required*: No
*Type*: Array of [AuthMode](aws-properties-appsync-channelnamespace-authmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appsync-channelnamespace-tags"></a>
A set of tags (key-value pairs) for this channel namespace.
*Required*: No
*Type*: Array of [Tag](aws-properties-appsync-channelnamespace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appsync-channelnamespace-return-values"></a>

### Ref
<a name="aws-resource-appsync-channelnamespace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns The Amazon Resource Name (ARN) of the channel namespace.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-appsync-channelnamespace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-appsync-channelnamespace-return-values-fn--getatt-fn--getatt"></a>

`ChannelNamespaceArn`  <a name="ChannelNamespaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the channel namespace.
