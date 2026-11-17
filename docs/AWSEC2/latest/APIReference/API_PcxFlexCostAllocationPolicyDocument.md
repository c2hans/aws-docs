---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PcxFlexCostAllocationPolicyDocument.html
---

# PcxFlexCostAllocationPolicyDocument
<a name="API_PcxFlexCostAllocationPolicyDocument"></a>

Describes the cost allocation policy document for Amazon VPC peering connections.

## Contents
<a name="API_PcxFlexCostAllocationPolicyDocument_Contents"></a>

 ** Dimensions.N **
The cost dimensions to report. This parameter is required. The only valid value is `data-transfer`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `data-transfer | data-processing`
Required: Yes

 ** ReportingGranularity.N **
The resource granularity level at which networking costs are allocated. This parameter is required. Specify exactly one value. Valid values are `eni`, `ec2`, `subnet`, `vpc`, `account`, `peering-id`, and `cidr`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `eni | ec2 | subnet | vpc | account | peering-id | cidr`
Required: Yes

 ** CidrRangeSpecifications ** (request), ** CidrRangeSpecifications ** (response)
The CIDR range mappings to use for cost allocation. Specify this value when `ReportingGranularity` is `cidr`, and omit it otherwise.
Type: [FlexCostAllocationCidrRangeSpecifications](API_FlexCostAllocationCidrRangeSpecifications.md) object
Required: No

## See Also
<a name="API_PcxFlexCostAllocationPolicyDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PcxFlexCostAllocationPolicyDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PcxFlexCostAllocationPolicyDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PcxFlexCostAllocationPolicyDocument)
