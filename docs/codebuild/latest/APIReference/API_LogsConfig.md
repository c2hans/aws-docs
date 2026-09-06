---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_LogsConfig.html
---

# LogsConfig
<a name="API_LogsConfig"></a>

 Information about logs for a build project. These can be logs in CloudWatch Logs, built in a specified S3 bucket, or both.

## Contents
<a name="API_LogsConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cloudWatchLogs **   <a name="CodeBuild-Type-LogsConfig-cloudWatchLogs"></a>
 Information about CloudWatch Logs for a build project. CloudWatch Logs are enabled by default.
Type: [CloudWatchLogsConfig](API_CloudWatchLogsConfig.md) object
Required: No

 ** s3Logs **   <a name="CodeBuild-Type-LogsConfig-s3Logs"></a>
 Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.
Type: [S3LogsConfig](API_S3LogsConfig.md) object
Required: No

## See Also
<a name="API_LogsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/LogsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/LogsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/LogsConfig)
