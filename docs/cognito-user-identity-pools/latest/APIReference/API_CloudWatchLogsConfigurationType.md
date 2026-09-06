---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CloudWatchLogsConfigurationType.html
---

# CloudWatchLogsConfigurationType
<a name="API_CloudWatchLogsConfigurationType"></a>

Configuration for the CloudWatch log group destination of user pool detailed activity logging, or of user activity log export with threat protection.

This data type is a request parameter of [SetLogDeliveryConfiguration](API_SetLogDeliveryConfiguration.md) and a response parameter of [GetLogDeliveryConfiguration](API_GetLogDeliveryConfiguration.md).

## Contents
<a name="API_CloudWatchLogsConfigurationType_Contents"></a>

 ** LogGroupArn **   <a name="CognitoUserPools-Type-CloudWatchLogsConfigurationType-LogGroupArn"></a>
The Amazon Resource Name (arn) of a CloudWatch Logs log group where your user pool sends logs. The log group must not be encrypted with AWS Key Management Service and must be in the same AWS account as your user pool.
To send logs to log groups with a resource policy of a size greater than 5120 characters, configure a log group with a path that starts with `/aws/vendedlogs`. For more information, see [Enabling logging from certain AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_CloudWatchLogsConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CloudWatchLogsConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CloudWatchLogsConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CloudWatchLogsConfigurationType)
