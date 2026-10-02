---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CheckSummary.html
---

# CheckSummary
<a name="API_CheckSummary"></a>

Trusted Advisor check summary.

## Contents
<a name="API_CheckSummary_Contents"></a>

 ** AccountSummary **   <a name="wellarchitected-Type-CheckSummary-AccountSummary"></a>
Account summary associated to the check.
Type: String to integer map
Valid Keys: `OKAY | WARNING | ERROR | NOT_AVAILABLE | FETCH_FAILED`
Valid Range: Minimum value of 1. Maximum value of 101.
Required: No

 ** ChoiceId **   <a name="wellarchitected-Type-CheckSummary-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Description **   <a name="wellarchitected-Type-CheckSummary-Description"></a>
Trusted Advisor check description.
Type: String
Required: No

 ** Id **   <a name="wellarchitected-Type-CheckSummary-Id"></a>
Trusted Advisor check ID.
Type: String
Required: No

 ** LensArn **   <a name="wellarchitected-Type-CheckSummary-LensArn"></a>
Well-Architected Lens ARN associated to the check.
Type: String
Required: No

 ** Name **   <a name="wellarchitected-Type-CheckSummary-Name"></a>
Trusted Advisor check name.
Type: String
Required: No

 ** PillarId **   <a name="wellarchitected-Type-CheckSummary-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Provider **   <a name="wellarchitected-Type-CheckSummary-Provider"></a>
Provider of the check related to the best practice.
Type: String
Valid Values: `TRUSTED_ADVISOR`
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-CheckSummary-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Status **   <a name="wellarchitected-Type-CheckSummary-Status"></a>
Status associated to the check.
Type: String
Valid Values: `OKAY | WARNING | ERROR | NOT_AVAILABLE | FETCH_FAILED`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-CheckSummary-UpdatedAt"></a>
The date and time when the check summary was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CheckSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CheckSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CheckSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CheckSummary)
