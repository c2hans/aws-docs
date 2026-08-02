---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CloudWatchLogDestination.html
---

# CloudWatchLogDestination
<a name="API_osis_CloudWatchLogDestination"></a>

The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch.

## Contents
<a name="API_osis_CloudWatchLogDestination_Contents"></a>

 ** LogGroup **   <a name="opensearchservice-Type-osis_CloudWatchLogDestination-LogGroup"></a>
The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, `/aws/vendedlogs/OpenSearchService/pipelines`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\/aws\/vendedlogs\/[\.\-_/#A-Za-z0-9]+`
Required: Yes

## See Also
<a name="API_osis_CloudWatchLogDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/CloudWatchLogDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/CloudWatchLogDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/CloudWatchLogDestination)
