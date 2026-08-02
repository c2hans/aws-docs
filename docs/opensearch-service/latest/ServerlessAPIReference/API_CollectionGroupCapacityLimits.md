---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupCapacityLimits.html
---

# CollectionGroupCapacityLimits
<a name="API_CollectionGroupCapacityLimits"></a>

Capacity limits for a collection group. These limits define the minimum and maximum OpenSearch Compute Units (OCUs) for indexing and search operations that can be used by collections in the group.

## Contents
<a name="API_CollectionGroupCapacityLimits_Contents"></a>

 ** maxIndexingCapacityInOCU **   <a name="opensearchserverless-Type-CollectionGroupCapacityLimits-maxIndexingCapacityInOCU"></a>
The maximum indexing capacity for collections in the group.
Type: Float
Valid Range: Minimum value of 1.
Required: No

 ** maxSearchCapacityInOCU **   <a name="opensearchserverless-Type-CollectionGroupCapacityLimits-maxSearchCapacityInOCU"></a>
The maximum search capacity for collections in the group.
Type: Float
Valid Range: Minimum value of 1.
Required: No

 ** minIndexingCapacityInOCU **   <a name="opensearchserverless-Type-CollectionGroupCapacityLimits-minIndexingCapacityInOCU"></a>
The minimum indexing capacity for collections in the group.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** minSearchCapacityInOCU **   <a name="opensearchserverless-Type-CollectionGroupCapacityLimits-minSearchCapacityInOCU"></a>
The minimum search capacity for collections in the group.
Type: Float
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CollectionGroupCapacityLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionGroupCapacityLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionGroupCapacityLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionGroupCapacityLimits)
