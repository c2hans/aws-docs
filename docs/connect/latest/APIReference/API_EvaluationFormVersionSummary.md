---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormVersionSummary.html
---

# EvaluationFormVersionSummary
<a name="API_EvaluationFormVersionSummary"></a>

Summary information about an evaluation form.

## Contents
<a name="API_EvaluationFormVersionSummary_Contents"></a>

 ** CreatedBy **   <a name="connect-Type-EvaluationFormVersionSummary-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the evaluation form.
Type: String
Required: Yes

 ** CreatedTime **   <a name="connect-Type-EvaluationFormVersionSummary-CreatedTime"></a>
The timestamp for when the evaluation form was created.
Type: Timestamp
Required: Yes

 ** EvaluationFormArn **   <a name="connect-Type-EvaluationFormVersionSummary-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationFormVersionSummary-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** EvaluationFormVersion **   <a name="connect-Type-EvaluationFormVersionSummary-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer
Required: Yes

 ** LastModifiedBy **   <a name="connect-Type-EvaluationFormVersionSummary-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the evaluation form.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationFormVersionSummary-LastModifiedTime"></a>
The timestamp for when the evaluation form was last updated.
Type: Timestamp
Required: Yes

 ** Locked **   <a name="connect-Type-EvaluationFormVersionSummary-Locked"></a>
The flag indicating whether the evaluation form is locked for changes.
Type: Boolean
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationFormVersionSummary-Status"></a>
The status of the evaluation form.
Type: String
Valid Values: `DRAFT | ACTIVE`
Required: Yes

## See Also
<a name="API_EvaluationFormVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
