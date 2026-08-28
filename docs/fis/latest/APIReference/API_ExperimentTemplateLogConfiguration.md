---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateLogConfiguration.html
---

# ExperimentTemplateLogConfiguration
<a name="API_ExperimentTemplateLogConfiguration"></a>

Describes the configuration for experiment logging.

## Contents
<a name="API_ExperimentTemplateLogConfiguration_Contents"></a>

 ** cloudWatchLogsConfiguration **   <a name="fis-Type-ExperimentTemplateLogConfiguration-cloudWatchLogsConfiguration"></a>
The configuration for experiment logging to Amazon CloudWatch Logs.
Type: [ExperimentTemplateCloudWatchLogsLogConfiguration](API_ExperimentTemplateCloudWatchLogsLogConfiguration.md) object
Required: No

 ** logSchemaVersion **   <a name="fis-Type-ExperimentTemplateLogConfiguration-logSchemaVersion"></a>
The schema version.
Type: Integer
Required: No

 ** s3Configuration **   <a name="fis-Type-ExperimentTemplateLogConfiguration-s3Configuration"></a>
The configuration for experiment logging to Amazon S3.
Type: [ExperimentTemplateS3LogConfiguration](API_ExperimentTemplateS3LogConfiguration.md) object
Required: No

## See Also
<a name="API_ExperimentTemplateLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateLogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
