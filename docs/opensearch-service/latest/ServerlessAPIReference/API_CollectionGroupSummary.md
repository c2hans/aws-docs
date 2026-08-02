---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupSummary.html
---

# CollectionGroupSummary
<a name="API_CollectionGroupSummary"></a>

Summary information about a collection group.

## Contents
<a name="API_CollectionGroupSummary_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-CollectionGroupSummary-arn"></a>
The Amazon Resource Name (ARN) of the collection group.
Type: String
Required: No

 ** capacityLimits **   <a name="opensearchserverless-Type-CollectionGroupSummary-capacityLimits"></a>
Capacity limits for a collection group. These limits define the minimum and maximum OpenSearch Compute Units (OCUs) for indexing and search operations that can be used by collections in the group.
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-CollectionGroupSummary-createdDate"></a>
The Epoch time when the collection group was created.
Type: Long
Required: No

 ** generation **   <a name="opensearchserverless-Type-CollectionGroupSummary-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group.
Type: String
Valid Values: `CLASSIC | NEXTGEN`
Required: No

 ** id **   <a name="opensearchserverless-Type-CollectionGroupSummary-id"></a>
The unique identifier of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionGroupSummary-name"></a>
The name of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** numberOfCollections **   <a name="opensearchserverless-Type-CollectionGroupSummary-numberOfCollections"></a>
The number of collections within the collection group.
Type: Integer
Required: No

## See Also
<a name="API_CollectionGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionGroupSummary)
