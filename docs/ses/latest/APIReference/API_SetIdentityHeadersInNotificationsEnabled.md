---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityHeadersInNotificationsEnabled.html
---

# SetIdentityHeadersInNotificationsEnabled
<a name="API_SetIdentityHeadersInNotificationsEnabled"></a>

Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.

You can execute this operation no more than once per second.

For more information about using notifications with Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html).

## Request Parameters
<a name="API_SetIdentityHeadersInNotificationsEnabled_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Enabled **
Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of `true` specifies that Amazon SES includes headers in notifications, and a value of `false` specifies that Amazon SES does not include headers in notifications.
This value can only be set when `NotificationType` is already set to use a particular Amazon SNS topic.
Type: Boolean
Required: Yes

 ** Identity **
The identity for which to enable or disable headers in notifications. Examples: `user@example.com`, `example.com`.
Type: String
Required: Yes

 ** NotificationType **
The notification type for which to enable or disable headers in notifications.
Type: String
Valid Values: `Bounce | Complaint | Delivery`
Required: Yes

## Errors
<a name="API_SetIdentityHeadersInNotificationsEnabled_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_SetIdentityHeadersInNotificationsEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled)
