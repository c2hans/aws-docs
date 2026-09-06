---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataQualityAppSpecification.html
---

# DataQualityAppSpecification
<a name="API_DataQualityAppSpecification"></a>

Information about the container that a data quality monitoring job runs.

## Contents
<a name="API_DataQualityAppSpecification_Contents"></a>

 ** ImageUri **   <a name="sagemaker-Type-DataQualityAppSpecification-ImageUri"></a>
The container image that the data quality monitoring job runs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** ContainerArguments **   <a name="sagemaker-Type-DataQualityAppSpecification-ContainerArguments"></a>
The arguments to send to the container that the monitoring job runs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** ContainerEntrypoint **   <a name="sagemaker-Type-DataQualityAppSpecification-ContainerEntrypoint"></a>
The entrypoint for a container used to run a monitoring job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** Environment **   <a name="sagemaker-Type-DataQualityAppSpecification-Environment"></a>
Sets the environment variables in the container that the monitoring job runs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

 ** PostAnalyticsProcessorSourceUri **   <a name="sagemaker-Type-DataQualityAppSpecification-PostAnalyticsProcessorSourceUri"></a>
An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** RecordPreprocessorSourceUri **   <a name="sagemaker-Type-DataQualityAppSpecification-RecordPreprocessorSourceUri"></a>
An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_DataQualityAppSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DataQualityAppSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DataQualityAppSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DataQualityAppSpecification)
