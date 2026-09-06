---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_NotificationChannelConfig.html
---

# NotificationChannelConfig
<a name="API_NotificationChannelConfig"></a>

 Information about notification channels you have configured with DevOps Guru. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS).

## Contents
<a name="API_NotificationChannelConfig_Contents"></a>

 ** Sns **   <a name="DevOpsGuru-Type-NotificationChannelConfig-Sns"></a>
 Information about a notification channel configured in DevOps Guru to send notifications when insights are created.
If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see [Permissions for Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html).
If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see [Permissions for AWS KMS–encrypted Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html).
Type: [SnsChannelConfig](API_SnsChannelConfig.md) object
Required: Yes

 ** Filters **   <a name="DevOpsGuru-Type-NotificationChannelConfig-Filters"></a>
 The filter configurations for the Amazon SNS notification topic you use with DevOps Guru. If you do not provide filter configurations, the default configurations are to receive notifications for all message types of `High` or `Medium` severity.
Type: [NotificationFilterConfig](API_NotificationFilterConfig.md) object
Required: No

## See Also
<a name="API_NotificationChannelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/NotificationChannelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/NotificationChannelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/NotificationChannelConfig)
