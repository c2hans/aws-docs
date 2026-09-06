---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationSummary.html
---

# EvaluationSummary
<a name="API_EvaluationSummary"></a>

Summary information about a contact evaluation.

## Contents
<a name="API_EvaluationSummary_Contents"></a>

 ** CreatedTime **   <a name="connect-Type-EvaluationSummary-CreatedTime"></a>
The timestamp for when the evaluation was created.
Type: Timestamp
Required: Yes

 ** EvaluationArn **   <a name="connect-Type-EvaluationSummary-EvaluationArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationSummary-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** EvaluationFormTitle **   <a name="connect-Type-EvaluationSummary-EvaluationFormTitle"></a>
A title of the evaluation form.
Type: String
Required: Yes

 ** EvaluationId **   <a name="connect-Type-EvaluationSummary-EvaluationId"></a>
A unique identifier for the contact evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** EvaluatorArn **   <a name="connect-Type-EvaluationSummary-EvaluatorArn"></a>
The Amazon Resource Name (ARN) of the user who last updated the evaluation.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationSummary-LastModifiedTime"></a>
The timestamp for when the evaluation was last updated.
Type: Timestamp
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationSummary-Status"></a>
The status of the contact evaluation.
Type: String
Valid Values: `DRAFT | SUBMITTED | REVIEW_REQUESTED | UNDER_REVIEW`
Required: Yes

 ** Acknowledgement **   <a name="connect-Type-EvaluationSummary-Acknowledgement"></a>
Information related to evaluation acknowledgement.
Type: [EvaluationAcknowledgementSummary](API_EvaluationAcknowledgementSummary.md) object
Required: No

 ** AutoEvaluationEnabled **   <a name="connect-Type-EvaluationSummary-AutoEvaluationEnabled"></a>
Whether automated evaluation is enabled.
Type: Boolean
Required: No

 ** AutoEvaluationStatus **   <a name="connect-Type-EvaluationSummary-AutoEvaluationStatus"></a>
The status of the contact auto evaluation.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`
Required: No

 ** CalibrationSessionId **   <a name="connect-Type-EvaluationSummary-CalibrationSessionId"></a>
The calibration session ID that this evaluation belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactParticipant **   <a name="connect-Type-EvaluationSummary-ContactParticipant"></a>
Information about a contact participant in the evaluation.
Type: [EvaluationContactParticipant](API_EvaluationContactParticipant.md) object
Required: No

 ** EvaluationType **   <a name="connect-Type-EvaluationSummary-EvaluationType"></a>
Type of the evaluation.
Type: String
Valid Values: `STANDARD | CALIBRATION`
Required: No

 ** Score **   <a name="connect-Type-EvaluationSummary-Score"></a>
The overall score of the contact evaluation.
Type: [EvaluationScore](API_EvaluationScore.md) object
Required: No

## See Also
<a name="API_EvaluationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationSummary)
