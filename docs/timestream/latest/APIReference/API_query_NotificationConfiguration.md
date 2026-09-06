---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_query_NotificationConfiguration"></a>

Notification configuration for a scheduled query. A notification is sent by Timestream when a scheduled query is created, its state is updated or when it is deleted.

## Contents
<a name="API_query_NotificationConfiguration_Contents"></a>

 ** SnsConfiguration **   <a name="timestream-Type-query_NotificationConfiguration-SnsConfiguration"></a>
Details about the Amazon Simple Notification Service (SNS) configuration. This field is visible only when SNS Topic is provided when updating the account settings.
Type: [SnsConfiguration](API_query_SnsConfiguration.md) object
Required: Yes

## See Also
<a name="API_query_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/NotificationConfiguration)
