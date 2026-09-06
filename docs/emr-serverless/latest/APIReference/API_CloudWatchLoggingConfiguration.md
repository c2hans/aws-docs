---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CloudWatchLoggingConfiguration.html
---

# CloudWatchLoggingConfiguration
<a name="API_CloudWatchLoggingConfiguration"></a>

The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.

## Contents
<a name="API_CloudWatchLoggingConfiguration_Contents"></a>

 ** enabled **   <a name="emrserverless-Type-CloudWatchLoggingConfiguration-enabled"></a>
Enables CloudWatch logging.
Type: Boolean
Required: Yes

 ** encryptionKeyArn **   <a name="emrserverless-Type-CloudWatchLoggingConfiguration-encryptionKeyArn"></a>
The AWS Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:([0-9]{12}):key\/[a-zA-Z0-9-]+`
Required: No

 ** logGroupName **   <a name="emrserverless-Type-CloudWatchLoggingConfiguration-logGroupName"></a>
The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** logStreamNamePrefix **   <a name="emrserverless-Type-CloudWatchLoggingConfiguration-logStreamNamePrefix"></a>
Prefix for the CloudWatch log stream name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** logTypes **   <a name="emrserverless-Type-CloudWatchLoggingConfiguration-logTypes"></a>
The types of logs that you want to publish to CloudWatch. If you don't specify any log types, driver STDOUT and STDERR logs will be published to CloudWatch Logs by default. For more information including the supported worker types for Hive and Spark, see [Logging for EMR Serverless with CloudWatch](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html#jobs-log-storage-cw).
+  **Key Valid Values**: `SPARK_DRIVER`, `SPARK_EXECUTOR`, `HIVE_DRIVER`, `TEZ_TASK`
+  **Array Members Valid Values**: `STDOUT`, `STDERR`, `HIVE_LOG`, `TEZ_AM`, `SYSTEM_LOGS`
Type: String to array of strings map
Map Entries: Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z]+[-_]*[a-zA-Z]+`
Required: No

## See Also
<a name="API_CloudWatchLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/CloudWatchLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/CloudWatchLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/CloudWatchLoggingConfiguration)
