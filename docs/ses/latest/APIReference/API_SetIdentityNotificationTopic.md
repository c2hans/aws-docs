---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityNotificationTopic.html
---

# SetIdentityNotificationTopic
<a name="API_SetIdentityNotificationTopic"></a>

Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify.

You can execute this operation no more than once per second.

For more information about feedback notification, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html).

## Request Parameters
<a name="API_SetIdentityNotificationTopic_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Identity **
The identity (email address or domain) for the Amazon SNS topic.
You can only specify a verified identity for this parameter.
You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: `sender@example.com`, `example.com`, `arn:aws:ses:us-east-1:123456789012:identity/example.com`.
Type: String
Required: Yes

 ** NotificationType **
The type of notifications that are published to the specified Amazon SNS topic.
Type: String
Valid Values: `Bounce | Complaint | Delivery`
Required: Yes

 ** SnsTopic **
The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, `SnsTopic` is cleared and publishing is disabled.
Type: String
Required: No

## Errors
<a name="API_SetIdentityNotificationTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_SetIdentityNotificationTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SetIdentityNotificationTopic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SetIdentityNotificationTopic)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
