---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CatalogItem.html
---

# CatalogItem
<a name="API_CatalogItem"></a>

 Information about a catalog item.

## Contents
<a name="API_CatalogItem_Contents"></a>

 ** CatalogItemId **   <a name="outposts-Type-CatalogItem-CatalogItemId"></a>
 The ID of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `OR-[A-Z0-9]{7}`
Required: No

 ** EC2Capacities **   <a name="outposts-Type-CatalogItem-EC2Capacities"></a>
 Information about the EC2 capacity of an item.
Type: Array of [EC2Capacity](API_EC2Capacity.md) objects
Required: No

 ** ItemStatus **   <a name="outposts-Type-CatalogItem-ItemStatus"></a>
 The status of a catalog item.
Type: String
Valid Values: `AVAILABLE | DISCONTINUED`
Required: No

 ** PowerKva **   <a name="outposts-Type-CatalogItem-PowerKva"></a>
 Information about the power draw of an item.
Type: Float
Required: No

 ** RackScalingType **   <a name="outposts-Type-CatalogItem-RackScalingType"></a>
The rack scaling type supported by the catalog item. Valid values are `SINGLE_RACK` and `MULTI_RACK`.
Type: String
Valid Values: `SINGLE_RACK | MULTI_RACK`
Required: No

 ** SupportedStorage **   <a name="outposts-Type-CatalogItem-SupportedStorage"></a>
 The supported storage options for the catalog item.
Type: Array of strings
Valid Values: `EBS | S3`
Required: No

 ** SupportedUplinkGbps **   <a name="outposts-Type-CatalogItem-SupportedUplinkGbps"></a>
 The uplink speed this catalog item requires for the connection to the Region.
Type: Array of integers
Required: No

 ** WeightLbs **   <a name="outposts-Type-CatalogItem-WeightLbs"></a>
 The weight of the item in pounds.
Type: Integer
Required: No

## See Also
<a name="API_CatalogItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CatalogItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CatalogItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CatalogItem)
