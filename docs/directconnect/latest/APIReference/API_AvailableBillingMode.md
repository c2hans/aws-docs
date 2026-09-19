---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AvailableBillingMode.html
---

# AvailableBillingMode
<a name="API_AvailableBillingMode"></a>

Information about a billing mode available at an Direct Connect location.

## Contents
<a name="API_AvailableBillingMode_Contents"></a>

 ** availablePortSpeeds **   <a name="DX-Type-AvailableBillingMode-availablePortSpeeds"></a>
The port speeds available for the billing mode.
Type: Array of strings
Required: No

 ** billingMode **   <a name="DX-Type-AvailableBillingMode-billingMode"></a>
The billing mode.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5 | PortPairFlatRateTier1 | PortPairFlatRateTier2 | PortPairFlatRateTier3 | PortPairFlatRateTier4 | PortPairFlatRateTier5`
Required: No

 ** includedRegions **   <a name="DX-Type-AvailableBillingMode-includedRegions"></a>
The AWS Regions included with the billing mode.
Type: Array of strings
Required: No

## See Also
<a name="API_AvailableBillingMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AvailableBillingMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AvailableBillingMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AvailableBillingMode)
