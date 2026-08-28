---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_VmInstanceAggregation.html
---

# VmInstanceAggregation
<a name="API_VmInstanceAggregation"></a>

An aggregation of information about VM instances.

## Contents
<a name="API_VmInstanceAggregation_Contents"></a>

 ** cloudAccountIds **   <a name="inspector2-Type-VmInstanceAggregation-cloudAccountIds"></a>
The cloud account IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudOrgIds **   <a name="inspector2-Type-VmInstanceAggregation-cloudOrgIds"></a>
The cloud organization IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudPartitions **   <a name="inspector2-Type-VmInstanceAggregation-cloudPartitions"></a>
The cloud partitions to aggregate findings for. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviders **   <a name="inspector2-Type-VmInstanceAggregation-cloudProviders"></a>
The cloud providers to aggregate findings for. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudRegions **   <a name="inspector2-Type-VmInstanceAggregation-cloudRegions"></a>
The cloud regions to aggregate findings for. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** instanceTags **   <a name="inspector2-Type-VmInstanceAggregation-instanceTags"></a>
The instance tags to aggregate findings for.
Type: Array of [MapFilter](API_MapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** operatingSystems **   <a name="inspector2-Type-VmInstanceAggregation-operatingSystems"></a>
The operating systems to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-VmInstanceAggregation-resourceIds"></a>
The resource IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-VmInstanceAggregation-sortBy"></a>
The value to sort results by. Specify a field name from the aggregation response, such as `CRITICAL`, `HIGH`, `ALL`, or `NETWORK_FINDINGS`.
Type: String
Valid Values: `CRITICAL | HIGH | ALL | NETWORK_FINDINGS`
Required: No

 ** sortOrder **   <a name="inspector2-Type-VmInstanceAggregation-sortOrder"></a>
The order to sort results by. Valid values are `ASC` and `DESC`.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** vmImageReferences **   <a name="inspector2-Type-VmInstanceAggregation-vmImageReferences"></a>
The VM image references to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_VmInstanceAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/VmInstanceAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/VmInstanceAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/VmInstanceAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
