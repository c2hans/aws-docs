---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_LogsLocation.html
---

# LogsLocation
<a name="API_LogsLocation"></a>

Information about build logs in CloudWatch Logs.

## Contents
<a name="API_LogsLocation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cloudWatchLogs **   <a name="CodeBuild-Type-LogsLocation-cloudWatchLogs"></a>
 Information about CloudWatch Logs for a build project.
Type: [CloudWatchLogsConfig](API_CloudWatchLogsConfig.md) object
Required: No

 ** cloudWatchLogsArn **   <a name="CodeBuild-Type-LogsLocation-cloudWatchLogsArn"></a>
The ARN of the CloudWatch Logs stream for a build execution. Its format is `arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}`. The CloudWatch Logs stream is created during the PROVISIONING phase of a build and the ARN will not be valid until it is created. For more information, see [Resources Defined by CloudWatch Logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies).
Type: String
Required: No

 ** deepLink **   <a name="CodeBuild-Type-LogsLocation-deepLink"></a>
The URL to an individual build log in CloudWatch Logs. The log stream is created during the PROVISIONING phase of a build and the `deeplink` will not be valid until it is created.
Type: String
Required: No

 ** groupName **   <a name="CodeBuild-Type-LogsLocation-groupName"></a>
The name of the CloudWatch Logs group for the build logs.
Type: String
Required: No

 ** s3DeepLink **   <a name="CodeBuild-Type-LogsLocation-s3DeepLink"></a>
 The URL to a build log in an S3 bucket.
Type: String
Required: No

 ** s3Logs **   <a name="CodeBuild-Type-LogsLocation-s3Logs"></a>
 Information about S3 logs for a build project.
Type: [S3LogsConfig](API_S3LogsConfig.md) object
Required: No

 ** s3LogsArn **   <a name="CodeBuild-Type-LogsLocation-s3LogsArn"></a>
 The ARN of S3 logs for a build project. Its format is `arn:${Partition}:s3:::${BucketName}/${ObjectName}`. For more information, see [Resources Defined by Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies).
Type: String
Required: No

 ** streamName **   <a name="CodeBuild-Type-LogsLocation-streamName"></a>
The name of the CloudWatch Logs stream for the build logs.
Type: String
Required: No

## See Also
<a name="API_LogsLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/LogsLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/LogsLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/LogsLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
