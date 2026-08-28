---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ControlAssessment.html
---

# ControlAssessment
<a name="API_ControlAssessment"></a>

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

 ** Errors **   <a name="AWSMarketplaceService-Type-ControlAssessment-Errors"></a>
An array of `ControlError` objects associated with the control evaluation.
Type: Array of [ControlError](API_ControlError.md) objects
Required: No

## See Also
<a name="API_ControlAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ControlAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ControlAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ControlAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
