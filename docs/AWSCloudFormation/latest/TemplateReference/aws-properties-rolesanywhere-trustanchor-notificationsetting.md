---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-trustanchor-notificationsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::TrustAnchor NotificationSetting
<a name="aws-properties-rolesanywhere-trustanchor-notificationsetting"></a>

 Customizable notification settings that will be applied to notification events. IAM Roles Anywhere consumes these settings while notifying across multiple channels - CloudWatch metrics, EventBridge, and Health Dashboard.

## Syntax
<a name="aws-properties-rolesanywhere-trustanchor-notificationsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-trustanchor-notificationsetting-syntax.json"></a>

```
{
  "[Channel](#cfn-rolesanywhere-trustanchor-notificationsetting-channel)" : {{String}},
  "[Enabled](#cfn-rolesanywhere-trustanchor-notificationsetting-enabled)" : {{Boolean}},
  "[Event](#cfn-rolesanywhere-trustanchor-notificationsetting-event)" : {{String}},
  "[Threshold](#cfn-rolesanywhere-trustanchor-notificationsetting-threshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-trustanchor-notificationsetting-syntax.yaml"></a>

```
  [Channel](#cfn-rolesanywhere-trustanchor-notificationsetting-channel): {{String}}
  [Enabled](#cfn-rolesanywhere-trustanchor-notificationsetting-enabled): {{Boolean}}
  [Event](#cfn-rolesanywhere-trustanchor-notificationsetting-event): {{String}}
  [Threshold](#cfn-rolesanywhere-trustanchor-notificationsetting-threshold): {{Number}}
```

## Properties
<a name="aws-properties-rolesanywhere-trustanchor-notificationsetting-properties"></a>

`Channel`  <a name="cfn-rolesanywhere-trustanchor-notificationsetting-channel"></a>
The specified channel of notification. IAM Roles Anywhere uses CloudWatch metrics, EventBridge, and Health Dashboard to notify for an event.
In the absence of a specific channel, IAM Roles Anywhere applies this setting to 'ALL' channels.
*Required*: No
*Type*: String
*Allowed values*: `ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-rolesanywhere-trustanchor-notificationsetting-enabled"></a>
Indicates whether the notification setting is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Event`  <a name="cfn-rolesanywhere-trustanchor-notificationsetting-event"></a>
The event to which this notification setting is applied.
*Required*: Yes
*Type*: String
*Allowed values*: `CA_CERTIFICATE_EXPIRY | END_ENTITY_CERTIFICATE_EXPIRY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-rolesanywhere-trustanchor-notificationsetting-threshold"></a>
The number of days before a notification event. This value is required for a notification setting that is enabled.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `360`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
