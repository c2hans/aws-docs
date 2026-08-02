---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ContainerImageAggregation.html
---

# ContainerImageAggregation
<a name="API_ContainerImageAggregation"></a>

An aggregation of information about container images.

## Contents
<a name="API_ContainerImageAggregation_Contents"></a>

 ** architectures **   <a name="inspector2-Type-ContainerImageAggregation-architectures"></a>
The image architectures to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudAccountIds **   <a name="inspector2-Type-ContainerImageAggregation-cloudAccountIds"></a>
The cloud account IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudOrgIds **   <a name="inspector2-Type-ContainerImageAggregation-cloudOrgIds"></a>
The cloud organization IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudPartitions **   <a name="inspector2-Type-ContainerImageAggregation-cloudPartitions"></a>
The cloud partitions to aggregate findings for. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviders **   <a name="inspector2-Type-ContainerImageAggregation-cloudProviders"></a>
The cloud providers to aggregate findings for. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudRegions **   <a name="inspector2-Type-ContainerImageAggregation-cloudRegions"></a>
The cloud regions to aggregate findings for. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** imageDigests **   <a name="inspector2-Type-ContainerImageAggregation-imageDigests"></a>
The image digests to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** imageTags **   <a name="inspector2-Type-ContainerImageAggregation-imageTags"></a>
The image tags to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** inUseCount **   <a name="inspector2-Type-ContainerImageAggregation-inUseCount"></a>
The in-use counts to aggregate findings for.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-ContainerImageAggregation-lastInUseAt"></a>
The last in-use timestamps to aggregate findings for.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** registries **   <a name="inspector2-Type-ContainerImageAggregation-registries"></a>
The image registries to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** repositories **   <a name="inspector2-Type-ContainerImageAggregation-repositories"></a>
The image repositories to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-ContainerImageAggregation-resourceIds"></a>
The resource IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-ContainerImageAggregation-sortBy"></a>
The value to sort results by. Specify a field name from the aggregation response, such as `CRITICAL`, `HIGH`, or `ALL`.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-ContainerImageAggregation-sortOrder"></a>
The order to sort results by. Valid values are `ASC` and `DESC`.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_ContainerImageAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ContainerImageAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ContainerImageAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ContainerImageAggregation)
