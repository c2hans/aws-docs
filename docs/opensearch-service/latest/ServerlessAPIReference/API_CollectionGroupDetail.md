---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupDetail.html
---

# CollectionGroupDetail
<a name="API_CollectionGroupDetail"></a>

Details about a collection group.

## Contents
<a name="API_CollectionGroupDetail_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-CollectionGroupDetail-arn"></a>
The Amazon Resource Name (ARN) of the collection group.
Type: String
Required: No

 ** capacityLimits **   <a name="opensearchserverless-Type-CollectionGroupDetail-capacityLimits"></a>
The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-CollectionGroupDetail-createdDate"></a>
The Epoch time when the collection group was created.
Type: Long
Required: No

 ** currentCapacity **   <a name="opensearchserverless-Type-CollectionGroupDetail-currentCapacity"></a>
Current search and indexing capacity for the collection group.
Type: [CurrentCapacity](API_CurrentCapacity.md) object
Required: No

 ** description **   <a name="opensearchserverless-Type-CollectionGroupDetail-description"></a>
The description of the collection group.
Type: String
Required: No

 ** generation **   <a name="opensearchserverless-Type-CollectionGroupDetail-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group.
Type: String
Valid Values: `CLASSIC | NEXTGEN`
Required: No

 ** id **   <a name="opensearchserverless-Type-CollectionGroupDetail-id"></a>
The unique identifier of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionGroupDetail-name"></a>
The name of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** numberOfCollections **   <a name="opensearchserverless-Type-CollectionGroupDetail-numberOfCollections"></a>
The number of collections associated with the collection group.
Type: Integer
Required: No

 ** standbyReplicas **   <a name="opensearchserverless-Type-CollectionGroupDetail-standbyReplicas"></a>
Indicates whether standby replicas are used for the collection group.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** tags **   <a name="opensearchserverless-Type-CollectionGroupDetail-tags"></a>
A map of key-value pairs associated with the collection group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_CollectionGroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionGroupDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionGroupDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionGroupDetail)
