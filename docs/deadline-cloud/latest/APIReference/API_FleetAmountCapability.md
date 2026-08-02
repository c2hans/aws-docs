---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FleetAmountCapability.html
---

# FleetAmountCapability
<a name="API_FleetAmountCapability"></a>

The fleet amount and attribute capabilities.

## Contents
<a name="API_FleetAmountCapability_Contents"></a>

 ** min **   <a name="deadlinecloud-Type-FleetAmountCapability-min"></a>
The minimum amount of fleet worker capability.
Type: Float
Required: Yes

 ** name **   <a name="deadlinecloud-Type-FleetAmountCapability-name"></a>
The name of the fleet capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?amount(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`
Required: Yes

 ** max **   <a name="deadlinecloud-Type-FleetAmountCapability-max"></a>
The maximum amount of the fleet worker capability.
Type: Float
Required: No

## See Also
<a name="API_FleetAmountCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetAmountCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetAmountCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetAmountCapability)
