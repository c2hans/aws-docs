---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroupDetail.html
---

# UpdateCollectionGroupDetail
<a name="API_UpdateCollectionGroupDetail"></a>

Details about the updated collection group.

## Contents
<a name="API_UpdateCollectionGroupDetail_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-arn"></a>
The Amazon Resource Name (ARN) of the collection group.
Type: String
Required: No

 ** capacityLimits **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-capacityLimits"></a>
The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-createdDate"></a>
The Epoch time when the collection group was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-description"></a>
The description of the collection group.
Type: String
Required: No

 ** generation **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group.
Type: String
Valid Values: `CLASSIC | NEXTGEN`
Required: No

 ** id **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-id"></a>
The unique identifier of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-lastModifiedDate"></a>
The date and time when the collection group was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-UpdateCollectionGroupDetail-name"></a>
The name of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

## See Also
<a name="API_UpdateCollectionGroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateCollectionGroupDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateCollectionGroupDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateCollectionGroupDetail)
