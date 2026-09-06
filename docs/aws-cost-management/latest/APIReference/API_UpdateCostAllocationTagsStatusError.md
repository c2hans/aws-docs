---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatusError.html
---

# UpdateCostAllocationTagsStatusError
<a name="API_UpdateCostAllocationTagsStatusError"></a>

Gives a detailed description of the result of an action. It's on each cost allocation tag entry in the request.

## Contents
<a name="API_UpdateCostAllocationTagsStatusError_Contents"></a>

 ** Code **   <a name="awscostmanagement-Type-UpdateCostAllocationTagsStatusError-Code"></a>
An error code representing why the action failed on this entry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Message **   <a name="awscostmanagement-Type-UpdateCostAllocationTagsStatusError-Message"></a>
A message explaining why the action failed on this entry.
Type: String
Required: No

 ** TagKey **   <a name="awscostmanagement-Type-UpdateCostAllocationTagsStatusError-TagKey"></a>
The key for the cost allocation tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_UpdateCostAllocationTagsStatusError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/UpdateCostAllocationTagsStatusError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/UpdateCostAllocationTagsStatusError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/UpdateCostAllocationTagsStatusError)
