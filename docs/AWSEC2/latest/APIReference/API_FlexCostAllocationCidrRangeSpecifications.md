---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationCidrRangeSpecifications.html
---

# FlexCostAllocationCidrRangeSpecifications

Specifies the CIDR ranges and labels to use for cost allocation when the reporting granularity is `cidr`.

## Contents
<a name="API_FlexCostAllocationCidrRangeSpecifications_Contents"></a>

 ** Prefixes.N **
The CIDR range to label mappings. You can specify from 1 to 100 mappings. This parameter is required.
Type: Array of [FlexCostAllocationCidrMapping](API_FlexCostAllocationCidrMapping.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** PrefixesType ** (request), ** PrefixesType ** (response)
The type of prefixes to use. This parameter is required. Valid values are `source-prefixes` and `destination-prefixes`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_FlexCostAllocationCidrRangeSpecifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationCidrRangeSpecifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationCidrRangeSpecifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationCidrRangeSpecifications)
