---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CloudWatchLogsConfig.html
---

# CloudWatchLogsConfig
<a name="API_CloudWatchLogsConfig"></a>

 Information about CloudWatch Logs for a build project.

## Contents
<a name="API_CloudWatchLogsConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** status **   <a name="CodeBuild-Type-CloudWatchLogsConfig-status"></a>
The current status of the logs in CloudWatch Logs for a build project. Valid values are:
+  `ENABLED`: CloudWatch Logs are enabled for this build project.
+  `DISABLED`: CloudWatch Logs are not enabled for this build project.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** groupName **   <a name="CodeBuild-Type-CloudWatchLogsConfig-groupName"></a>
 The group name of the logs in CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).
Type: String
Required: No

 ** streamName **   <a name="CodeBuild-Type-CloudWatchLogsConfig-streamName"></a>
 The prefix of the stream name of the CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).
Type: String
Required: No

## See Also
<a name="API_CloudWatchLogsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/CloudWatchLogsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/CloudWatchLogsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/CloudWatchLogsConfig)
