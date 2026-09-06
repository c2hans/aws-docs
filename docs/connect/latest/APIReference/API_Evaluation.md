---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Evaluation.html
---

# Evaluation
<a name="API_Evaluation"></a>

Information about a contact evaluation.

## Contents
<a name="API_Evaluation_Contents"></a>

 ** Answers **   <a name="connect-Type-Evaluation-Answers"></a>
A map of question identifiers to answer value.
Type: String to [EvaluationAnswerOutput](API_EvaluationAnswerOutput.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** CreatedTime **   <a name="connect-Type-Evaluation-CreatedTime"></a>
The timestamp for when the evaluation was created.
Type: Timestamp
Required: Yes

 ** EvaluationArn **   <a name="connect-Type-Evaluation-EvaluationArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String
Required: Yes

 ** EvaluationId **   <a name="connect-Type-Evaluation-EvaluationId"></a>
A unique identifier for the contact evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-Evaluation-LastModifiedTime"></a>
The timestamp for when the evaluation was last updated.
Type: Timestamp
Required: Yes

 ** Metadata **   <a name="connect-Type-Evaluation-Metadata"></a>
Metadata about the contact evaluation.
Type: [EvaluationMetadata](API_EvaluationMetadata.md) object
Required: Yes

 ** Notes **   <a name="connect-Type-Evaluation-Notes"></a>
A map of question identifiers to note value.
Type: String to [EvaluationNote](API_EvaluationNote.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** Status **   <a name="connect-Type-Evaluation-Status"></a>
The status of the contact evaluation.
Type: String
Valid Values: `DRAFT | SUBMITTED | REVIEW_REQUESTED | UNDER_REVIEW`
Required: Yes

 ** EvaluationType **   <a name="connect-Type-Evaluation-EvaluationType"></a>
Type of the evaluation.
Type: String
Valid Values: `STANDARD | CALIBRATION`
Required: No

 ** Scores **   <a name="connect-Type-Evaluation-Scores"></a>
A map of item (section or question) identifiers to score value.
Type: String to [EvaluationScore](API_EvaluationScore.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** Tags **   <a name="connect-Type-Evaluation-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Evaluation)
