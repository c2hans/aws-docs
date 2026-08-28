---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationSearchSummary.html
---

# EvaluationSearchSummary
<a name="API_EvaluationSearchSummary"></a>

Summary of evaluation obtained from the search operation.

## Contents
<a name="API_EvaluationSearchSummary_Contents"></a>

 ** CreatedTime **   <a name="connect-Type-EvaluationSearchSummary-CreatedTime"></a>
The date and time when the evaluation was created, in UTC time.
Type: Timestamp
Required: Yes

 ** EvaluationArn **   <a name="connect-Type-EvaluationSearchSummary-EvaluationArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String
Required: Yes

 ** EvaluationFormVersion **   <a name="connect-Type-EvaluationSearchSummary-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer
Required: Yes

 ** EvaluationId **   <a name="connect-Type-EvaluationSearchSummary-EvaluationId"></a>
A unique identifier for the contact evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationSearchSummary-LastModifiedTime"></a>
The date and time when the evaluation was modified last time, in UTC time.
Type: Timestamp
Required: Yes

 ** Metadata **   <a name="connect-Type-EvaluationSearchSummary-Metadata"></a>
Summary information about the evaluation search.
Type: [EvaluationSearchMetadata](API_EvaluationSearchMetadata.md) object
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationSearchSummary-Status"></a>
The status of the evaluation.
Type: String
Valid Values: `DRAFT | SUBMITTED | REVIEW_REQUESTED | UNDER_REVIEW`
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationSearchSummary-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** EvaluationFormTitle **   <a name="connect-Type-EvaluationSearchSummary-EvaluationFormTitle"></a>
Title of the evaluation form.
Type: String
Required: No

 ** EvaluationType **   <a name="connect-Type-EvaluationSearchSummary-EvaluationType"></a>
Type of the evaluation.
Type: String
Valid Values: `STANDARD | CALIBRATION`
Required: No

 ** Tags **   <a name="connect-Type-EvaluationSearchSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_EvaluationSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
