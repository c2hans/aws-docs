---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_LogPublishingOptions.html
---

# LogPublishingOptions
<a name="API_osis_LogPublishingOptions"></a>

Container for the values required to configure logging for the pipeline. If you don't specify these values, OpenSearch Ingestion will not publish logs from your application to CloudWatch Logs.

## Contents
<a name="API_osis_LogPublishingOptions_Contents"></a>

 ** CloudWatchLogDestination **   <a name="opensearchservice-Type-osis_LogPublishingOptions-CloudWatchLogDestination"></a>
The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if `IsLoggingEnabled` is set to `true`.
Type: [CloudWatchLogDestination](API_osis_CloudWatchLogDestination.md) object
Required: No

 ** IsLoggingEnabled **   <a name="opensearchservice-Type-osis_LogPublishingOptions-IsLoggingEnabled"></a>
Whether logs should be published.
Type: Boolean
Required: No

## See Also
<a name="API_osis_LogPublishingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/LogPublishingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/LogPublishingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/LogPublishingOptions)
