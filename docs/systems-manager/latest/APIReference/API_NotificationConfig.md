---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_NotificationConfig.html
---

# NotificationConfig
<a name="API_NotificationConfig"></a>

Configurations for sending notifications.

## Contents
<a name="API_NotificationConfig_Contents"></a>

 ** NotificationArn **   <a name="systemsmanager-Type-NotificationConfig-NotificationArn"></a>
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.
Type: String
Required: No

 ** NotificationEvents **   <a name="systemsmanager-Type-NotificationConfig-NotificationEvents"></a>
The different events for which you can receive notifications. To learn more about these events, see [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Valid Values: `All | InProgress | Success | TimedOut | Cancelled | Failed`
Required: No

 ** NotificationType **   <a name="systemsmanager-Type-NotificationConfig-NotificationType"></a>
The type of notification.
+  `Command`: Receive notification when the status of a command changes.
+  `Invocation`: For commands sent to multiple managed nodes, receive notification on a per-node basis when the status of a command changes.
Type: String
Valid Values: `Command | Invocation`
Required: No

## See Also
<a name="API_NotificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/NotificationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/NotificationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/NotificationConfig)
