---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-eventrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::EventRule
<a name="aws-resource-notifications-eventrule"></a>

Creates an [https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html](https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html) that is associated with a specified `NotificationConfiguration`.

## Syntax
<a name="aws-resource-notifications-eventrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-eventrule-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::EventRule",
  "Properties" : {
      "[EventPattern](#cfn-notifications-eventrule-eventpattern)" : {{String}},
      "[EventType](#cfn-notifications-eventrule-eventtype)" : {{String}},
      "[NotificationConfigurationArn](#cfn-notifications-eventrule-notificationconfigurationarn)" : {{String}},
      "[Regions](#cfn-notifications-eventrule-regions)" : {{[ String, ... ]}},
      "[Source](#cfn-notifications-eventrule-source)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-eventrule-syntax.yaml"></a>

```
Type: AWS::Notifications::EventRule
Properties:
  [EventPattern](#cfn-notifications-eventrule-eventpattern): {{String}}
  [EventType](#cfn-notifications-eventrule-eventtype): {{String}}
  [NotificationConfigurationArn](#cfn-notifications-eventrule-notificationconfigurationarn): {{String}}
  [Regions](#cfn-notifications-eventrule-regions): {{
    - String}}
  [Source](#cfn-notifications-eventrule-source): {{String}}
```

## Properties
<a name="aws-resource-notifications-eventrule-properties"></a>

`EventPattern`  <a name="cfn-notifications-eventrule-eventpattern"></a>
An additional event pattern used to further filter the events this `EventRule` receives.
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide.*
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventType`  <a name="cfn-notifications-eventrule-eventtype"></a>
The event type this rule should match with the EventBridge events. It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the * Amazon EventBridge User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9 \-\(\)])+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NotificationConfigurationArn`  <a name="cfn-notifications-eventrule-notificationconfigurationarn"></a>
The ARN for the `NotificationConfiguration` associated with this `EventRule`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regions`  <a name="cfn-notifications-eventrule-regions"></a>
A list of AWS Regions that send events to this `EventRule`.
*Required*: Yes
*Type*: Array of String
*Maximum*: `25`
*Minimum*: `2 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-notifications-eventrule-source"></a>
The event source this rule should match with the EventBridge event sources. It must match with atleast one of the valid EventBridge event sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the * Amazon EventBridge User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^aws.([a-z0-9\-])+$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-eventrule-return-values"></a>

### Ref
<a name="aws-resource-notifications-eventrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.

### Fn::GetAtt
<a name="aws-resource-notifications-eventrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-notifications-eventrule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the `EventRule`. CloudFormation stack generates this ARN and then uses this ARN associated with the `NotificationConfiguration`.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of the `EventRule`.

`ManagedRules`  <a name="ManagedRules-fn::getatt"></a>
A list of Amazon EventBridge Managed Rule ARNs associated with this `EventRule`.
These are created by AWS User Notifications within your account so your `EventRules` can function.
