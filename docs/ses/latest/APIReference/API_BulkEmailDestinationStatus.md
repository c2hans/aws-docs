---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_BulkEmailDestinationStatus.html
---

# BulkEmailDestinationStatus
<a name="API_BulkEmailDestinationStatus"></a>

An object that contains the response from the `SendBulkTemplatedEmail` operation.

## Contents
<a name="API_BulkEmailDestinationStatus_Contents"></a>

 ** Error **
A description of an error that prevented a message being sent using the `SendBulkTemplatedEmail` operation.
Type: String
Required: No

 ** MessageId **
The unique message identifier returned from the `SendBulkTemplatedEmail` operation.
Type: String
Required: No

 ** Status **
The status of a message sent using the `SendBulkTemplatedEmail` operation.
Possible values for this parameter include:
+  `Success`: Amazon SES accepted the message, and attempts to deliver it to the recipients.
+  `MessageRejected`: The message was rejected because it contained a virus.
+  `MailFromDomainNotVerified`: The sender's email address or domain was not verified.
+  `ConfigurationSetDoesNotExist`: The configuration set you specified does not exist.
+  `TemplateDoesNotExist`: The template you specified does not exist.
+  `AccountSuspended`: Your account has been shut down because of issues related to your email sending practices.
+  `AccountThrottled`: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.
+  `AccountDailyQuotaExceeded`: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.
+  `InvalidSendingPoolName`: The configuration set you specified refers to an IP pool that does not exist.
+  `AccountSendingPaused`: Email sending for the Amazon SES account was disabled using the [UpdateAccountSendingEnabled](API_UpdateAccountSendingEnabled.md) operation.
+  `ConfigurationSetSendingPaused`: Email sending for this configuration set was disabled using the [UpdateConfigurationSetSendingEnabled](API_UpdateConfigurationSetSendingEnabled.md) operation.
+  `InvalidParameterValue`: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.
+  `TransientFailure`: Amazon SES was unable to process your request because of a temporary issue.
+  `Failed`: Amazon SES was unable to process your request. See the error message for additional information.
Type: String
Valid Values: `Success | MessageRejected | MailFromDomainNotVerified | ConfigurationSetDoesNotExist | TemplateDoesNotExist | AccountSuspended | AccountThrottled | AccountDailyQuotaExceeded | InvalidSendingPoolName | AccountSendingPaused | ConfigurationSetSendingPaused | InvalidParameterValue | TransientFailure | Failed`
Required: No

## See Also
<a name="API_BulkEmailDestinationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/BulkEmailDestinationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/BulkEmailDestinationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/BulkEmailDestinationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
