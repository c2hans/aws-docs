---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PreviewPrivacyImpactParametersInput.html
---

# PreviewPrivacyImpactParametersInput
<a name="API_PreviewPrivacyImpactParametersInput"></a>

Specifies the updated epsilon and noise parameters to preview. The preview allows you to see how the maximum number of each type of aggregation function would change with the new parameters.

## Contents
<a name="API_PreviewPrivacyImpactParametersInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** differentialPrivacy **   <a name="API-Type-PreviewPrivacyImpactParametersInput-differentialPrivacy"></a>
An array that specifies the epsilon and noise parameters.
Type: [DifferentialPrivacyPreviewParametersInput](API_DifferentialPrivacyPreviewParametersInput.md) object
Required: No

## See Also
<a name="API_PreviewPrivacyImpactParametersInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PreviewPrivacyImpactParametersInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PreviewPrivacyImpactParametersInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PreviewPrivacyImpactParametersInput)
