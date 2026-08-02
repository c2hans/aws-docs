---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepAmountCapability.html
---

# StepAmountCapability
<a name="API_StepAmountCapability"></a>

The details outlining the minimum and maximum capability of a step.

## Contents
<a name="API_StepAmountCapability_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-StepAmountCapability-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?amount(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`
Required: Yes

 ** max **   <a name="deadlinecloud-Type-StepAmountCapability-max"></a>
The maximum amount.
Type: Double
Required: No

 ** min **   <a name="deadlinecloud-Type-StepAmountCapability-min"></a>
The minimum amount.
Type: Double
Required: No

 ** value **   <a name="deadlinecloud-Type-StepAmountCapability-value"></a>
The amount value.
Type: Double
Required: No

## See Also
<a name="API_StepAmountCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepAmountCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepAmountCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepAmountCapability)
