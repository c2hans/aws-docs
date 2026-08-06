---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DestinationConfiguration.html
---

# DestinationConfiguration
<a name="API_DestinationConfiguration"></a>

Configuration for where to deliver scheduled query results. Specifies the destination type and associated settings for result delivery.

## Contents
<a name="API_DestinationConfiguration_Contents"></a>

 ** lookupTableConfiguration **   <a name="CWL-Type-DestinationConfiguration-lookupTableConfiguration"></a>
Configuration for delivering query results to a lookup table. The query results automatically populate or refresh the specified lookup table on each scheduled execution.
Type: [LookupTableConfiguration](API_LookupTableConfiguration.md) object
Required: No

 ** s3Configuration **   <a name="CWL-Type-DestinationConfiguration-s3Configuration"></a>
Configuration for delivering query results to Amazon S3.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

## See Also
<a name="API_DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DestinationConfiguration)
