---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTagStatusEntry.html
---

# CostAllocationTagStatusEntry
<a name="API_CostAllocationTagStatusEntry"></a>

The cost allocation tag status. The status of a key can either be active or inactive.

## Contents
<a name="API_CostAllocationTagStatusEntry_Contents"></a>

 ** Status **   <a name="awscostmanagement-Type-CostAllocationTagStatusEntry-Status"></a>
The status of a cost allocation tag.
Type: String
Valid Values: `Active | Inactive`
Required: Yes

 ** TagKey **   <a name="awscostmanagement-Type-CostAllocationTagStatusEntry-TagKey"></a>
The key for the cost allocation tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_CostAllocationTagStatusEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostAllocationTagStatusEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostAllocationTagStatusEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostAllocationTagStatusEntry)
