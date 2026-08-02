---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_SpotOptions.html
---

# SpotOptions
<a name="API_SpotOptions"></a>

Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.

## Contents
<a name="API_SpotOptions_Contents"></a>

 ** allocationStrategy **   <a name="PCS-Type-SpotOptions-allocationStrategy"></a>
The Amazon EC2 allocation strategy AWS PCS uses to provision EC2 instances. AWS PCS supports **lowest price**, **capacity optimized**, and **price capacity optimized**. For more information, see [Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) in the *Amazon Elastic Compute Cloud User Guide*. If you don't provide this option, it defaults to **price capacity optimized**.
Type: String
Valid Values: `lowest-price | capacity-optimized | price-capacity-optimized`
Required: No

## See Also
<a name="API_SpotOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/SpotOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/SpotOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/SpotOptions)
