---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyImpact.html
---

# PrivacyImpact
<a name="API_PrivacyImpact"></a>

Provides an estimate of the number of aggregation functions that the member who can query can run given the epsilon and noise parameters.

## Contents
<a name="API_PrivacyImpact_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** differentialPrivacy **   <a name="API-Type-PrivacyImpact-differentialPrivacy"></a>
An object that lists the number and type of aggregation functions you can perform.
Type: [DifferentialPrivacyPrivacyImpact](API_DifferentialPrivacyPrivacyImpact.md) object
Required: No

## See Also
<a name="API_PrivacyImpact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyImpact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyImpact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyImpact)
