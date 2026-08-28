---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationSearchMetadata.html
---

# EvaluationSearchMetadata
<a name="API_EvaluationSearchMetadata"></a>

Metadata information about an evaluation search.

## Contents
<a name="API_EvaluationSearchMetadata_Contents"></a>

 ** ContactId **   <a name="connect-Type-EvaluationSearchMetadata-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** EvaluatorArn **   <a name="connect-Type-EvaluationSearchMetadata-EvaluatorArn"></a>
The Amazon Resource Name (ARN) of the person who evaluated the contact.
Type: String
Required: Yes

 ** AcknowledgedBy **   <a name="connect-Type-EvaluationSearchMetadata-AcknowledgedBy"></a>
The agent who acknowledged the evaluation.
Type: String
Required: No

 ** AcknowledgedTime **   <a name="connect-Type-EvaluationSearchMetadata-AcknowledgedTime"></a>
When the evaluation was acknowledged by the agent.
Type: Timestamp
Required: No

 ** AcknowledgerComment **   <a name="connect-Type-EvaluationSearchMetadata-AcknowledgerComment"></a>
The comment from the agent when they acknowledged the evaluation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Required: No

 ** AutoEvaluationEnabled **   <a name="connect-Type-EvaluationSearchMetadata-AutoEvaluationEnabled"></a>
Whether auto-evaluation is enabled.
Type: Boolean
Required: No

 ** AutoEvaluationStatus **   <a name="connect-Type-EvaluationSearchMetadata-AutoEvaluationStatus"></a>
The status of the contact auto evaluation.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`
Required: No

 ** CalibrationSessionId **   <a name="connect-Type-EvaluationSearchMetadata-CalibrationSessionId"></a>
The calibration session ID that this evaluation belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactAgentId **   <a name="connect-Type-EvaluationSearchMetadata-ContactAgentId"></a>
The unique ID of the agent who handled the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactParticipantId **   <a name="connect-Type-EvaluationSearchMetadata-ContactParticipantId"></a>
Identifier for a contact participant in the evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactParticipantRole **   <a name="connect-Type-EvaluationSearchMetadata-ContactParticipantRole"></a>
Role of a contact participant in the evaluation.
Type: String
Valid Values: `AGENT | SYSTEM | CUSTOM_BOT | CUSTOMER`
Required: No

 ** EarnedPoints **   <a name="connect-Type-EvaluationSearchMetadata-EarnedPoints"></a>
The points earned for the evaluation.
Type: Integer
Required: No

 ** MaxBasePoint **   <a name="connect-Type-EvaluationSearchMetadata-MaxBasePoint"></a>
The maximum base points possible for the evaluation.
Type: Integer
Required: No

 ** PerformanceCategory **   <a name="connect-Type-EvaluationSearchMetadata-PerformanceCategory"></a>
The performance category for the evaluation score.
Type: String
Valid Values: `NEEDS_IMPROVEMENT | EXCEEDS_EXPECTATIONS`
Required: No

 ** ReviewId **   <a name="connect-Type-EvaluationSearchMetadata-ReviewId"></a>
Identifier for the review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** SamplingJobId **   <a name="connect-Type-EvaluationSearchMetadata-SamplingJobId"></a>
Identifier of the sampling job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ScoreAutomaticFail **   <a name="connect-Type-EvaluationSearchMetadata-ScoreAutomaticFail"></a>
The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag is true.
Type: Boolean
Required: No

 ** ScoreNotApplicable **   <a name="connect-Type-EvaluationSearchMetadata-ScoreNotApplicable"></a>
The flag to mark the item as not applicable for scoring.
Type: Boolean
Required: No

 ** ScorePercentage **   <a name="connect-Type-EvaluationSearchMetadata-ScorePercentage"></a>
The total evaluation score expressed as a percentage.
Type: Double
Required: No

## See Also
<a name="API_EvaluationSearchMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationSearchMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationSearchMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationSearchMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
