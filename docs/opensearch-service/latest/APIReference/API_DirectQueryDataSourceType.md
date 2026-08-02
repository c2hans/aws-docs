---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DirectQueryDataSourceType.html
---

# DirectQueryDataSourceType
<a name="API_DirectQueryDataSourceType"></a>

 The type of data source that is used for direct queries. This is a supported AWS service, such as CloudWatch Logs or Security Lake.

## Contents
<a name="API_DirectQueryDataSourceType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CloudWatchLog **   <a name="opensearchservice-Type-DirectQueryDataSourceType-CloudWatchLog"></a>
 Specifies CloudWatch Logs as a type of data source for direct queries.
Type: [CloudWatchDirectQueryDataSource](API_CloudWatchDirectQueryDataSource.md) object
Required: No

 ** Prometheus **   <a name="opensearchservice-Type-DirectQueryDataSourceType-Prometheus"></a>
 Specifies Prometheus as a type of data source for direct queries.
Type: [PrometheusDirectQueryDataSource](API_PrometheusDirectQueryDataSource.md) object
Required: No

 ** SecurityLake **   <a name="opensearchservice-Type-DirectQueryDataSourceType-SecurityLake"></a>
 Specifies Security Lake as a type of data source for direct queries.
Type: [SecurityLakeDirectQueryDataSource](API_SecurityLakeDirectQueryDataSource.md) object
Required: No

## See Also
<a name="API_DirectQueryDataSourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DirectQueryDataSourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DirectQueryDataSourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DirectQueryDataSourceType)
