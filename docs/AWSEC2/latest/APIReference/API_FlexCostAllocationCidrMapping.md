---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FlexCostAllocationCidrMapping.html
---

# FlexCostAllocationCidrMapping

Maps a CIDR range to a label for cost allocation reporting.

## Contents
<a name="API_FlexCostAllocationCidrMapping_Contents"></a>

 ** CidrLabel ** (request), ** CidrLabel ** (response)
The label to assign to the CIDR range. The label can be up to 64 characters long. It can contain letters, numbers, hyphens (`-`), and underscores (`_`), and must start with a letter or a number. This parameter is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-]{0,63}`
Required: Yes

 ** CidrRange ** (request), ** CidrRange ** (response)
The CIDR range. This parameter is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43.
Required: Yes

## See Also
<a name="API_FlexCostAllocationCidrMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FlexCostAllocationCidrMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FlexCostAllocationCidrMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FlexCostAllocationCidrMapping)
