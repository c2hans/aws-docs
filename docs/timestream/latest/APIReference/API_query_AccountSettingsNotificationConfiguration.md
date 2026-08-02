---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_AccountSettingsNotificationConfiguration.html
---

# AccountSettingsNotificationConfiguration
<a name="API_query_AccountSettingsNotificationConfiguration"></a>

Configuration settings for notifications related to account settings.

## Contents
<a name="API_query_AccountSettingsNotificationConfiguration_Contents"></a>

 ** RoleArn **   <a name="timestream-Type-query_AccountSettingsNotificationConfiguration-RoleArn"></a>
An Amazon Resource Name (ARN) that grants Timestream permission to publish notifications. This field is only visible if SNS Topic is provided when updating the account settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** SnsConfiguration **   <a name="timestream-Type-query_AccountSettingsNotificationConfiguration-SnsConfiguration"></a>
Details on SNS that are required to send the notification.
Type: [SnsConfiguration](API_query_SnsConfiguration.md) object
Required: No

## See Also
<a name="API_query_AccountSettingsNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration)
