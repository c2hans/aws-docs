---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CalculationSummary.html
---

# CalculationSummary
<a name="API_CalculationSummary"></a>

Summary information for a notebook calculation.

## Contents
<a name="API_CalculationSummary_Contents"></a>

 ** CalculationExecutionId **   <a name="athena-Type-CalculationSummary-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** Description **   <a name="athena-Type-CalculationSummary-Description"></a>
A description of the calculation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Status **   <a name="athena-Type-CalculationSummary-Status"></a>
Contains information about the status of the calculation.
Type: [CalculationStatus](API_CalculationStatus.md) object
Required: No

## See Also
<a name="API_CalculationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CalculationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CalculationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CalculationSummary)
