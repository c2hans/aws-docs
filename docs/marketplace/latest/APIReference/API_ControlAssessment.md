---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ControlAssessment.html
---

# ControlAssessment

The result of evaluating a single control as part of an assessment.

## Contents
<a name="API_ControlAssessment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ControlAssessmentResult **   <a name="AWSMarketplaceService-Type-ControlAssessment-ControlAssessmentResult"></a>
The result of the control evaluation.
Type: String
Valid Values: `PASS | FAIL | NOT_EXECUTED | EXEMPTION_PASS`
Required: No

 ** ControlId **   <a name="AWSMarketplaceService-Type-ControlAssessment-ControlId"></a>
The unique ID of the control that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** ControlSummary **   <a name="AWSMarketplaceService-Type-ControlAssessment-ControlSummary"></a>
A summary of what the control produced, such as recommendations for the listing.
Type: [ControlSummary](API_ControlSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Errors **   <a name="AWSMarketplaceService-Type-ControlAssessment-Errors"></a>
An array of `ControlError` objects associated with the control evaluation.
Type: Array of [ControlError](API_ControlError.md) objects
Required: No

 ** VerificationSource **   <a name="AWSMarketplaceService-Type-ControlAssessment-VerificationSource"></a>
Where the result of the control came from. This value doesn't say whether the control passed. A control that you attested to can still have a result of `PASS`. Valid values are:
+  `AWS_VERIFIED` - AWS evaluated the control.
+  `SELF_ATTESTED` - You attested to the result of the control.
Type: String
Valid Values: `AWS_VERIFIED | SELF_ATTESTED`
Required: No

## See Also
<a name="API_ControlAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ControlAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ControlAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ControlAssessment)
