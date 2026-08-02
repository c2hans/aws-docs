---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchCollection.html
---

# OpenSearchCollection
<a name="API_OpenSearchCollection"></a>

This structure contains information about the OpenSearch Service collection used for this integration. An OpenSearch Service collection is a logical grouping of one or more indexes that represent an analytics workload. For more information, see [Creating and managing OpenSearch Service Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html).

## Contents
<a name="API_OpenSearchCollection_Contents"></a>

 ** collectionArn **   <a name="CWL-Type-OpenSearchCollection-collectionArn"></a>
The ARN of the collection.
Type: String
Required: No

 ** collectionEndpoint **   <a name="CWL-Type-OpenSearchCollection-collectionEndpoint"></a>
The endpoint of the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^https://[\.\-_/#:A-Za-z0-9]+\.com$`
Required: No

 ** status **   <a name="CWL-Type-OpenSearchCollection-status"></a>
This structure contains information about the status of this OpenSearch Service resource.
Type: [OpenSearchResourceStatus](API_OpenSearchResourceStatus.md) object
Required: No

## See Also
<a name="API_OpenSearchCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchCollection)
