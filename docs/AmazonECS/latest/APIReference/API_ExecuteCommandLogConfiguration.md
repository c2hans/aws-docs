---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExecuteCommandLogConfiguration.html
---

# ExecuteCommandLogConfiguration
<a name="API_ExecuteCommandLogConfiguration"></a>

The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket.

## Contents
<a name="API_ExecuteCommandLogConfiguration_Contents"></a>

 ** cloudWatchEncryptionEnabled **   <a name="ECS-Type-ExecuteCommandLogConfiguration-cloudWatchEncryptionEnabled"></a>
Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off.
Type: Boolean
Required: No

 ** cloudWatchLogGroupName **   <a name="ECS-Type-ExecuteCommandLogConfiguration-cloudWatchLogGroupName"></a>
The name of the CloudWatch log group to send logs to.
The CloudWatch log group must already be created.
Type: String
Required: No

 ** s3BucketName **   <a name="ECS-Type-ExecuteCommandLogConfiguration-s3BucketName"></a>
The name of the S3 bucket to send logs to.
The S3 bucket must already be created.
Type: String
Required: No

 ** s3EncryptionEnabled **   <a name="ECS-Type-ExecuteCommandLogConfiguration-s3EncryptionEnabled"></a>
Determines whether to use encryption on the S3 logs. If not specified, encryption is not used.
Type: Boolean
Required: No

 ** s3KeyPrefix **   <a name="ECS-Type-ExecuteCommandLogConfiguration-s3KeyPrefix"></a>
An optional folder in the S3 bucket to place logs in.
Type: String
Required: No

## See Also
<a name="API_ExecuteCommandLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExecuteCommandLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExecuteCommandLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExecuteCommandLogConfiguration)
