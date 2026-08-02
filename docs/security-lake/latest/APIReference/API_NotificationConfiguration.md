---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_NotificationConfiguration"></a>

Specify the configurations you want to use for subscriber notification to notify the subscriber when new data is written to the data lake for sources that the subscriber consumes in Security Lake.

## Contents
<a name="API_NotificationConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** httpsNotificationConfiguration **   <a name="securitylake-Type-NotificationConfiguration-httpsNotificationConfiguration"></a>
The configurations used for HTTPS subscriber notification.
Type: [HttpsNotificationConfiguration](API_HttpsNotificationConfiguration.md) object
Required: No

 ** sqsNotificationConfiguration **   <a name="securitylake-Type-NotificationConfiguration-sqsNotificationConfiguration"></a>
The configurations for SQS subscriber notification.
Type: [SqsNotificationConfiguration](API_SqsNotificationConfiguration.md) object
Required: No

## See Also
<a name="API_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/NotificationConfiguration)
