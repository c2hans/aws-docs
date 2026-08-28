---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringAppSpecification.html
---

# MonitoringAppSpecification
<a name="API_MonitoringAppSpecification"></a>

Container image configuration object for the monitoring job.

## Contents
<a name="API_MonitoringAppSpecification_Contents"></a>

 ** ImageUri **   <a name="sagemaker-Type-MonitoringAppSpecification-ImageUri"></a>
The container image to be run by the monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** ContainerArguments **   <a name="sagemaker-Type-MonitoringAppSpecification-ContainerArguments"></a>
An array of arguments for the container used to run the monitoring job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** ContainerEntrypoint **   <a name="sagemaker-Type-MonitoringAppSpecification-ContainerEntrypoint"></a>
Specifies the entrypoint for a container used to run the monitoring job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** PostAnalyticsProcessorSourceUri **   <a name="sagemaker-Type-MonitoringAppSpecification-PostAnalyticsProcessorSourceUri"></a>
An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** RecordPreprocessorSourceUri **   <a name="sagemaker-Type-MonitoringAppSpecification-RecordPreprocessorSourceUri"></a>
An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_MonitoringAppSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringAppSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringAppSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringAppSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
