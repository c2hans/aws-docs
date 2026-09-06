---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTag.html
---

# CostAllocationTag
<a name="API_CostAllocationTag"></a>

The cost allocation tag structure. This includes detailed metadata for the `CostAllocationTag` object.

## Contents
<a name="API_CostAllocationTag_Contents"></a>

 ** Status **   <a name="awscostmanagement-Type-CostAllocationTag-Status"></a>
The status of a cost allocation tag.
Type: String
Valid Values: `Active | Inactive`
Required: Yes

 ** TagKey **   <a name="awscostmanagement-Type-CostAllocationTag-TagKey"></a>
The key for the cost allocation tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** Type **   <a name="awscostmanagement-Type-CostAllocationTag-Type"></a>
The type of cost allocation tag. You can use `AWSGenerated` or `UserDefined` type tags. `AWSGenerated` type tags are tags that AWS defines and applies to support AWS resources for cost allocation purposes. `UserDefined` type tags are tags that you define, create, and apply to resources.
Type: String
Valid Values: `AWSGenerated | UserDefined`
Required: Yes

 ** LastUpdatedDate **   <a name="awscostmanagement-Type-CostAllocationTag-LastUpdatedDate"></a>
The last date that the tag was either activated or deactivated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** LastUsedDate **   <a name="awscostmanagement-Type-CostAllocationTag-LastUsedDate"></a>
The last month that the tag was used on an AWS resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

## See Also
<a name="API_CostAllocationTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostAllocationTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostAllocationTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostAllocationTag)
