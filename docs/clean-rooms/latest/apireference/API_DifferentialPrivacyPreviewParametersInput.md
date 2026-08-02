---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyPreviewParametersInput.html
---

# DifferentialPrivacyPreviewParametersInput
<a name="API_DifferentialPrivacyPreviewParametersInput"></a>

The epsilon and noise parameters that you want to preview.

## Contents
<a name="API_DifferentialPrivacyPreviewParametersInput_Contents"></a>

 ** epsilon **   <a name="API-Type-DifferentialPrivacyPreviewParametersInput-epsilon"></a>
The epsilon value that you want to preview.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

 ** usersNoisePerQuery **   <a name="API-Type-DifferentialPrivacyPreviewParametersInput-usersNoisePerQuery"></a>
Noise added per query is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: Yes

## See Also
<a name="API_DifferentialPrivacyPreviewParametersInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyPreviewParametersInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyPreviewParametersInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyPreviewParametersInput)
