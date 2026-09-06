---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateLogConfigurationInput.html
---

# UpdateExperimentTemplateLogConfigurationInput
<a name="API_UpdateExperimentTemplateLogConfigurationInput"></a>

Specifies the configuration for experiment logging.

## Contents
<a name="API_UpdateExperimentTemplateLogConfigurationInput_Contents"></a>

 ** cloudWatchLogsConfiguration **   <a name="fis-Type-UpdateExperimentTemplateLogConfigurationInput-cloudWatchLogsConfiguration"></a>
The configuration for experiment logging to Amazon CloudWatch Logs.
Type: [ExperimentTemplateCloudWatchLogsLogConfigurationInput](API_ExperimentTemplateCloudWatchLogsLogConfigurationInput.md) object
Required: No

 ** logSchemaVersion **   <a name="fis-Type-UpdateExperimentTemplateLogConfigurationInput-logSchemaVersion"></a>
The schema version.
Type: Integer
Required: No

 ** s3Configuration **   <a name="fis-Type-UpdateExperimentTemplateLogConfigurationInput-s3Configuration"></a>
The configuration for experiment logging to Amazon S3.
Type: [ExperimentTemplateS3LogConfigurationInput](API_ExperimentTemplateS3LogConfigurationInput.md) object
Required: No

## See Also
<a name="API_UpdateExperimentTemplateLogConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/UpdateExperimentTemplateLogConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/UpdateExperimentTemplateLogConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/UpdateExperimentTemplateLogConfigurationInput)
