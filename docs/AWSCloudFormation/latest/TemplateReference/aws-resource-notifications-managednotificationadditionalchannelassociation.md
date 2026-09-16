---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-managednotificationadditionalchannelassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::ManagedNotificationAdditionalChannelAssociation
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation"></a>

Associates a `Channel` with a `ManagedNotificationAdditionalChannelAssociation` for AWS User Notifications. For more information about AWS User Notifications, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).

## Syntax
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::ManagedNotificationAdditionalChannelAssociation",
  "Properties" : {
      "[ChannelArn](#cfn-notifications-managednotificationadditionalchannelassociation-channelarn)" : {{String}},
      "[IsSensitiveEventsSubscribed](#cfn-notifications-managednotificationadditionalchannelassociation-issensitiveeventssubscribed)" : {{Boolean}},
      "[ManagedNotificationConfigurationArn](#cfn-notifications-managednotificationadditionalchannelassociation-managednotificationconfigurationarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-syntax.yaml"></a>

```
Type: AWS::Notifications::ManagedNotificationAdditionalChannelAssociation
Properties:
  [ChannelArn](#cfn-notifications-managednotificationadditionalchannelassociation-channelarn): {{String}}
  [IsSensitiveEventsSubscribed](#cfn-notifications-managednotificationadditionalchannelassociation-issensitiveeventssubscribed): {{Boolean}}
  [ManagedNotificationConfigurationArn](#cfn-notifications-managednotificationadditionalchannelassociation-managednotificationconfigurationarn): {{String}}
```

## Properties
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-properties"></a>

`ChannelArn`  <a name="cfn-notifications-managednotificationadditionalchannelassociation-channelarn"></a>
 The ARN of the `Channel`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsSensitiveEventsSubscribed`  <a name="cfn-notifications-managednotificationadditionalchannelassociation-issensitiveeventssubscribed"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedNotificationConfigurationArn`  <a name="cfn-notifications-managednotificationadditionalchannelassociation-managednotificationconfigurationarn"></a>
 The ARN of the `ManagedNotificationAdditionalChannelAssociation` associated with the `Channel`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:notifications::([0-9]{12}|):managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-return-values"></a>

### Ref
<a name="aws-resource-notifications-managednotificationadditionalchannelassociation-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.
