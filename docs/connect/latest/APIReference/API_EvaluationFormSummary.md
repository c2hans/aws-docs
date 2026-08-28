---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSummary.html
---

# EvaluationFormSummary
<a name="API_EvaluationFormSummary"></a>

Summary information about an evaluation form.

## Contents
<a name="API_EvaluationFormSummary_Contents"></a>

 ** CreatedBy **   <a name="connect-Type-EvaluationFormSummary-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the evaluation form.
Type: String
Required: Yes

 ** CreatedTime **   <a name="connect-Type-EvaluationFormSummary-CreatedTime"></a>
The timestamp for when the evaluation form was created.
Type: Timestamp
Required: Yes

 ** EvaluationFormArn **   <a name="connect-Type-EvaluationFormSummary-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationFormSummary-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LastModifiedBy **   <a name="connect-Type-EvaluationFormSummary-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the evaluation form.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationFormSummary-LastModifiedTime"></a>
The timestamp for when the evaluation form was last updated.
Type: Timestamp
Required: Yes

 ** LatestVersion **   <a name="connect-Type-EvaluationFormSummary-LatestVersion"></a>
The version number of the latest evaluation form version.
Type: Integer
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationFormSummary-Title"></a>
A title of the evaluation form.
Type: String
Required: Yes

 ** ActiveVersion **   <a name="connect-Type-EvaluationFormSummary-ActiveVersion"></a>
The version of the active evaluation form version.
Type: Integer
Required: No

 ** LastActivatedBy **   <a name="connect-Type-EvaluationFormSummary-LastActivatedBy"></a>
 The Amazon Resource Name (ARN) of the user who last activated the evaluation form.
Type: String
Required: No

 ** LastActivatedTime **   <a name="connect-Type-EvaluationFormSummary-LastActivatedTime"></a>
The timestamp for when the evaluation form was last activated.
Type: Timestamp
Required: No

## See Also
<a name="API_EvaluationFormSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
