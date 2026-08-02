---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_BundleInformation.html
---

# BundleInformation
<a name="API_BundleInformation"></a>

Information about the pricing bundle.

## Contents
<a name="API_BundleInformation_Contents"></a>

 ** bundleNames **   <a name="tm-Type-BundleInformation-bundleNames"></a>
The bundle names.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** pricingTier **   <a name="tm-Type-BundleInformation-pricingTier"></a>
The pricing tier.
Type: String
Valid Values: `TIER_1 | TIER_2 | TIER_3 | TIER_4`
Required: No

## See Also
<a name="API_BundleInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/BundleInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/BundleInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/BundleInformation)
