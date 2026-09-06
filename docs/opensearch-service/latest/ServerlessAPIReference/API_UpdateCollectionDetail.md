---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionDetail.html
---

# UpdateCollectionDetail
<a name="API_UpdateCollectionDetail"></a>

Details about an updated OpenSearch Serverless collection.

## Contents
<a name="API_UpdateCollectionDetail_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-UpdateCollectionDetail-arn"></a>
The Amazon Resource Name (ARN) of the collection.
Type: String
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-UpdateCollectionDetail-createdDate"></a>
The date and time when the collection was created.
Type: Long
Required: No

 ** deletionProtection **   <a name="opensearchserverless-Type-UpdateCollectionDetail-deletionProtection"></a>
Indicates whether deletion protection is `ENABLED` or `DISABLED` for the collection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** description **   <a name="opensearchserverless-Type-UpdateCollectionDetail-description"></a>
The description of the collection.
Type: String
Required: No

 ** id **   <a name="opensearchserverless-Type-UpdateCollectionDetail-id"></a>
The unique identifier of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-UpdateCollectionDetail-lastModifiedDate"></a>
The date and time when the collection was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-UpdateCollectionDetail-name"></a>
The name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-UpdateCollectionDetail-status"></a>
The current status of the collection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED | UPDATE_FAILED`
Required: No

 ** type **   <a name="opensearchserverless-Type-UpdateCollectionDetail-type"></a>
The collection type.
Type: String
Valid Values: `SEARCH | TIMESERIES | VECTORSEARCH`
Required: No

 ** vectorOptions **   <a name="opensearchserverless-Type-UpdateCollectionDetail-vectorOptions"></a>
Configuration options for vector search capabilities in the collection.
Type: [VectorOptions](API_VectorOptions.md) object
Required: No

## See Also
<a name="API_UpdateCollectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateCollectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateCollectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateCollectionDetail)
