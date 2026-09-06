---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceSharingConfig.html
---

# ResourceSharingConfig
<a name="API_ResourceSharingConfig"></a>

Resource sharing configuration.

## Contents
<a name="API_ResourceSharingConfig_Contents"></a>

 ** Strategy **   <a name="sagemaker-Type-ResourceSharingConfig-Strategy"></a>
The strategy of how idle compute is shared within the cluster. The following are the options of strategies.
+  `DontLend`: entities do not lend idle compute.
+  `Lend`: entities can lend idle compute to entities that can borrow.
+  `LendandBorrow`: entities can lend idle compute and borrow idle compute from other entities.
Default is `LendandBorrow`.
Type: String
Valid Values: `Lend | DontLend | LendAndBorrow`
Required: Yes

 ** AbsoluteBorrowLimits **   <a name="sagemaker-Type-ResourceSharingConfig-AbsoluteBorrowLimits"></a>
The absolute limits on compute resources that can be borrowed from idle compute. When specified, these limits define the maximum amount of specific resource types (such as accelerators, vCPU, or memory) that an entity can borrow, regardless of the percentage-based `BorrowLimit`.
Type: Array of [ComputeQuotaResourceConfig](API_ComputeQuotaResourceConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** BorrowLimit **   <a name="sagemaker-Type-ResourceSharingConfig-BorrowLimit"></a>
The limit on how much idle compute can be borrowed.The values can be 1 - 500 percent of idle compute that the team is allowed to borrow.
Default is `50`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

## See Also
<a name="API_ResourceSharingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResourceSharingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResourceSharingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResourceSharingConfig)
