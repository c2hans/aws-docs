---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ImageLayerAggregation.html
---

# ImageLayerAggregation
<a name="API_ImageLayerAggregation"></a>

The details that define an aggregation based on container image layers.

## Contents
<a name="API_ImageLayerAggregation_Contents"></a>

 ** cloudAccountIds **   <a name="inspector2-Type-ImageLayerAggregation-cloudAccountIds"></a>
The cloud account IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudOrgIds **   <a name="inspector2-Type-ImageLayerAggregation-cloudOrgIds"></a>
The cloud organization IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudPartitions **   <a name="inspector2-Type-ImageLayerAggregation-cloudPartitions"></a>
The cloud partitions to aggregate findings for. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviders **   <a name="inspector2-Type-ImageLayerAggregation-cloudProviders"></a>
The cloud providers to aggregate findings for. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudRegions **   <a name="inspector2-Type-ImageLayerAggregation-cloudRegions"></a>
The cloud regions to aggregate findings for. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** layerHashes **   <a name="inspector2-Type-ImageLayerAggregation-layerHashes"></a>
The hashes associated with the layers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** repositories **   <a name="inspector2-Type-ImageLayerAggregation-repositories"></a>
The repository associated with the container image hosting the layers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-ImageLayerAggregation-resourceIds"></a>
The ID of the container image layer.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-ImageLayerAggregation-sortBy"></a>
The value to sort results by.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-ImageLayerAggregation-sortOrder"></a>
The order to sort results by.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_ImageLayerAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ImageLayerAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ImageLayerAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ImageLayerAggregation)
