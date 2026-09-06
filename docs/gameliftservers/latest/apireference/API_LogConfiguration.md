---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LogConfiguration.html
---

# LogConfiguration
<a name="API_LogConfiguration"></a>

A method for collecting container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods:

## Contents
<a name="API_LogConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LogDestination **   <a name="gameliftservers-Type-LogConfiguration-LogDestination"></a>
The type of log collection to use for a fleet.
+  `CLOUDWATCH` -- (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
+  `S3` -- Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleet's home AWS Region.
+  `NONE` -- Don't collect container logs.
Type: String
Valid Values: `NONE | CLOUDWATCH | S3`
Required: No

 ** LogGroupArn **   <a name="gameliftservers-Type-LogConfiguration-LogGroupArn"></a>
If log destination is `CLOUDWATCH`, logs are sent to the specified log group in Amazon CloudWatch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/\-\*]+`
Required: No

 ** S3BucketName **   <a name="gameliftservers-Type-LogConfiguration-S3BucketName"></a>
If log destination is `S3`, logs are sent to the specified Amazon S3 bucket name.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_LogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LogConfiguration)
