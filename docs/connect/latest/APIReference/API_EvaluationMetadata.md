---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationMetadata.html
---

# EvaluationMetadata
<a name="API_EvaluationMetadata"></a>

Metadata information about a contact evaluation.

## Contents
<a name="API_EvaluationMetadata_Contents"></a>

 ** ContactId **   <a name="connect-Type-EvaluationMetadata-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** EvaluatorArn **   <a name="connect-Type-EvaluationMetadata-EvaluatorArn"></a>
The Amazon Resource Name (ARN) of the user who last updated the evaluation.
Type: String
Required: Yes

 ** Acknowledgement **   <a name="connect-Type-EvaluationMetadata-Acknowledgement"></a>
Information related to evaluation acknowledgement.
Type: [EvaluationAcknowledgement](API_EvaluationAcknowledgement.md) object
Required: No

 ** AutoEvaluation **   <a name="connect-Type-EvaluationMetadata-AutoEvaluation"></a>
Information related to automated evaluation.
Type: [AutoEvaluationDetails](API_AutoEvaluationDetails.md) object
Required: No

 ** CalibrationSessionId **   <a name="connect-Type-EvaluationMetadata-CalibrationSessionId"></a>
The calibration session ID that this evaluation belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactAgentId **   <a name="connect-Type-EvaluationMetadata-ContactAgentId"></a>
The identifier of the agent who performed the contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactParticipant **   <a name="connect-Type-EvaluationMetadata-ContactParticipant"></a>
Information about a contact participant in this evaluation.
Type: [EvaluationContactParticipant](API_EvaluationContactParticipant.md) object
Required: No

 ** Review **   <a name="connect-Type-EvaluationMetadata-Review"></a>
Information about reviews of this evaluation.
Type: [EvaluationReviewMetadata](API_EvaluationReviewMetadata.md) object
Required: No

 ** SamplingJobId **   <a name="connect-Type-EvaluationMetadata-SamplingJobId"></a>
Identifier of the sampling job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** Score **   <a name="connect-Type-EvaluationMetadata-Score"></a>
The overall score of the contact evaluation.
Type: [EvaluationScore](API_EvaluationScore.md) object
Required: No

## See Also
<a name="API_EvaluationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
