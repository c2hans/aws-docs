---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ServerlessFunctionAggregation.html
---

# ServerlessFunctionAggregation
<a name="API_ServerlessFunctionAggregation"></a>

An aggregation of information about serverless functions.

## Contents
<a name="API_ServerlessFunctionAggregation_Contents"></a>

 ** cloudAccountIds **   <a name="inspector2-Type-ServerlessFunctionAggregation-cloudAccountIds"></a>
The cloud account IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudOrgIds **   <a name="inspector2-Type-ServerlessFunctionAggregation-cloudOrgIds"></a>
The cloud organization IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudPartitions **   <a name="inspector2-Type-ServerlessFunctionAggregation-cloudPartitions"></a>
The cloud partitions to aggregate findings for. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviders **   <a name="inspector2-Type-ServerlessFunctionAggregation-cloudProviders"></a>
The cloud providers to aggregate findings for. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudRegions **   <a name="inspector2-Type-ServerlessFunctionAggregation-cloudRegions"></a>
The cloud regions to aggregate findings for. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** functionNames **   <a name="inspector2-Type-ServerlessFunctionAggregation-functionNames"></a>
The function names to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** functionTags **   <a name="inspector2-Type-ServerlessFunctionAggregation-functionTags"></a>
The function tags to aggregate findings for.
Type: Array of [MapFilter](API_MapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-ServerlessFunctionAggregation-resourceIds"></a>
The resource IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** runtimes **   <a name="inspector2-Type-ServerlessFunctionAggregation-runtimes"></a>
The runtimes to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-ServerlessFunctionAggregation-sortBy"></a>
The value to sort results by. Specify a field name from the aggregation response, such as `CRITICAL`, `HIGH`, or `ALL`.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-ServerlessFunctionAggregation-sortOrder"></a>
The order to sort results by. Valid values are `ASC` and `DESC`.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_ServerlessFunctionAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ServerlessFunctionAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ServerlessFunctionAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ServerlessFunctionAggregation)
