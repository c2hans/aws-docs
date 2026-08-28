---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CheckDetail.html
---

# CheckDetail
<a name="API_CheckDetail"></a>

Account details for a Well-Architected best practice in relation to Trusted Advisor checks.

## Contents
<a name="API_CheckDetail_Contents"></a>

 ** AccountId **   <a name="wellarchitected-Type-CheckDetail-AccountId"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** ChoiceId **   <a name="wellarchitected-Type-CheckDetail-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Description **   <a name="wellarchitected-Type-CheckDetail-Description"></a>
Trusted Advisor check description.
Type: String
Required: No

 ** FlaggedResources **   <a name="wellarchitected-Type-CheckDetail-FlaggedResources"></a>
Count of flagged resources associated to the check.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 9999.
Required: No

 ** Id **   <a name="wellarchitected-Type-CheckDetail-Id"></a>
Trusted Advisor check ID.
Type: String
Required: No

 ** LensArn **   <a name="wellarchitected-Type-CheckDetail-LensArn"></a>
Well-Architected Lens ARN associated to the check.
Type: String
Required: No

 ** Name **   <a name="wellarchitected-Type-CheckDetail-Name"></a>
Trusted Advisor check name.
Type: String
Required: No

 ** PillarId **   <a name="wellarchitected-Type-CheckDetail-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Provider **   <a name="wellarchitected-Type-CheckDetail-Provider"></a>
Provider of the check related to the best practice.
Type: String
Valid Values: `TRUSTED_ADVISOR`
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-CheckDetail-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Reason **   <a name="wellarchitected-Type-CheckDetail-Reason"></a>
Reason associated to the check.
Type: String
Valid Values: `ASSUME_ROLE_ERROR | ACCESS_DENIED | UNKNOWN_ERROR | PREMIUM_SUPPORT_REQUIRED`
Required: No

 ** Status **   <a name="wellarchitected-Type-CheckDetail-Status"></a>
Status associated to the check.
Type: String
Valid Values: `OKAY | WARNING | ERROR | NOT_AVAILABLE | FETCH_FAILED`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-CheckDetail-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_CheckDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CheckDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CheckDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CheckDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
