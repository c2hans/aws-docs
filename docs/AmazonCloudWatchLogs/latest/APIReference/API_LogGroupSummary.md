---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogGroupSummary.html
---

# LogGroupSummary
<a name="API_LogGroupSummary"></a>

This structure contains information about one log group in your account.

## Contents
<a name="API_LogGroupSummary_Contents"></a>

 ** logGroupArn **   <a name="CWL-Type-LogGroupSummary-logGroupArn"></a>
The Amazon Resource Name (ARN) of the log group.
Type: String
Required: No

 ** logGroupClass **   <a name="CWL-Type-LogGroupSummary-logGroupClass"></a>
The log group class for this log group. For details about the features supported by each log group class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
Type: String
Valid Values: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
Required: No

 ** logGroupName **   <a name="CWL-Type-LogGroupSummary-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

## See Also
<a name="API_LogGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogGroupSummary)
