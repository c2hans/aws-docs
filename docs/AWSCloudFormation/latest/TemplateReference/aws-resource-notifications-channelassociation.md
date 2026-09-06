---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-channelassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::ChannelAssociation
<a name="aws-resource-notifications-channelassociation"></a>

The `AWS::Notifications::ChannelAssociation` resource associates a `Channel` with a `NotificationConfiguration` for AWS User Notifications. For more information about AWS User Notifications, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).

## Syntax
<a name="aws-resource-notifications-channelassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-channelassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::ChannelAssociation",
  "Properties" : {
      "[Arn](#cfn-notifications-channelassociation-arn)" : {{String}},
      "[NotificationConfigurationArn](#cfn-notifications-channelassociation-notificationconfigurationarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-channelassociation-syntax.yaml"></a>

```
Type: AWS::Notifications::ChannelAssociation
Properties:
  [Arn](#cfn-notifications-channelassociation-arn): {{String}}
  [NotificationConfigurationArn](#cfn-notifications-channelassociation-notificationconfigurationarn): {{String}}
```

## Properties
<a name="aws-resource-notifications-channelassociation-properties"></a>

`Arn`  <a name="cfn-notifications-channelassociation-arn"></a>
The Amazon Resource Name (ARN) of the `Channel`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotificationConfigurationArn`  <a name="cfn-notifications-channelassociation-notificationconfigurationarn"></a>
The ARN of the `NotificationConfiguration` associated with the `Channel`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-channelassociation-return-values"></a>

### Ref
<a name="aws-resource-notifications-channelassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.
