---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_LogConfigurationType.html
---

# LogConfigurationType
<a name="API_LogConfigurationType"></a>

The configuration of user event logs to an external AWS service like Amazon Data Firehose, Amazon S3, or Amazon CloudWatch Logs.

This data type is a request parameter of [SetLogDeliveryConfiguration](API_SetLogDeliveryConfiguration.md) and a response parameter of [GetLogDeliveryConfiguration](API_GetLogDeliveryConfiguration.md).

## Contents
<a name="API_LogConfigurationType_Contents"></a>

 ** EventSource **   <a name="CognitoUserPools-Type-LogConfigurationType-EventSource"></a>
The source of events that your user pool sends for logging. To send error-level logs about user notification activity, set to `userNotification`. To send info-level logs about threat-protection user activity in user pools with the Plus feature plan, set to `userAuthEvents`.
Type: String
Valid Values: `userNotification | userAuthEvents`
Required: Yes

 ** LogLevel **   <a name="CognitoUserPools-Type-LogConfigurationType-LogLevel"></a>
The `errorlevel` selection of logs that a user pool sends for detailed activity logging. To send `userNotification` activity with [information about message delivery](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html), choose `ERROR` with `CloudWatchLogsConfiguration`. To send `userAuthEvents` activity with user logs from threat protection with the Plus feature plan, choose `INFO` with one of `CloudWatchLogsConfiguration`, `FirehoseConfiguration`, or `S3Configuration`.
Type: String
Valid Values: `ERROR | INFO`
Required: Yes

 ** CloudWatchLogsConfiguration **   <a name="CognitoUserPools-Type-LogConfigurationType-CloudWatchLogsConfiguration"></a>
The CloudWatch log group destination of user pool detailed activity logs, or of user activity log export with threat protection.
Type: [CloudWatchLogsConfigurationType](API_CloudWatchLogsConfigurationType.md) object
Required: No

 ** FirehoseConfiguration **   <a name="CognitoUserPools-Type-LogConfigurationType-FirehoseConfiguration"></a>
The Amazon Data Firehose stream destination of user activity log export with threat protection. To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).
Type: [FirehoseConfigurationType](API_FirehoseConfigurationType.md) object
Required: No

 ** S3Configuration **   <a name="CognitoUserPools-Type-LogConfigurationType-S3Configuration"></a>
The Amazon S3 bucket destination of user activity log export with threat protection. To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).
Type: [S3ConfigurationType](API_S3ConfigurationType.md) object
Required: No

## See Also
<a name="API_LogConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/LogConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/LogConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/LogConfigurationType)
