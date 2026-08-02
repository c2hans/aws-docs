---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CloudWatchLoggingOptionUpdate.html
---

# CloudWatchLoggingOptionUpdate
<a name="API_CloudWatchLoggingOptionUpdate"></a>

Describes the Amazon CloudWatch logging option updates.

## Contents
<a name="API_CloudWatchLoggingOptionUpdate_Contents"></a>

 ** CloudWatchLoggingOptionId **   <a name="APIReference-Type-CloudWatchLoggingOptionUpdate-CloudWatchLoggingOptionId"></a>
The ID of the CloudWatch logging option to update
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** LogStreamARNUpdate **   <a name="APIReference-Type-CloudWatchLoggingOptionUpdate-LogStreamARNUpdate"></a>
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_CloudWatchLoggingOptionUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionUpdate)
