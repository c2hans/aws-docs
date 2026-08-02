---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentLogConfiguration.html
---

# ExperimentLogConfiguration
<a name="API_ExperimentLogConfiguration"></a>

Describes the configuration for experiment logging.

## Contents
<a name="API_ExperimentLogConfiguration_Contents"></a>

 ** cloudWatchLogsConfiguration **   <a name="fis-Type-ExperimentLogConfiguration-cloudWatchLogsConfiguration"></a>
The configuration for experiment logging to Amazon CloudWatch Logs.
Type: [ExperimentCloudWatchLogsLogConfiguration](API_ExperimentCloudWatchLogsLogConfiguration.md) object
Required: No

 ** logSchemaVersion **   <a name="fis-Type-ExperimentLogConfiguration-logSchemaVersion"></a>
The schema version.
Type: Integer
Required: No

 ** s3Configuration **   <a name="fis-Type-ExperimentLogConfiguration-s3Configuration"></a>
The configuration for experiment logging to Amazon S3.
Type: [ExperimentS3LogConfiguration](API_ExperimentS3LogConfiguration.md) object
Required: No

## See Also
<a name="API_ExperimentLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentLogConfiguration)
