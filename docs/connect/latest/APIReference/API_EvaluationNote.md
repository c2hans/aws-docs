---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationNote.html
---

# EvaluationNote
<a name="API_EvaluationNote"></a>

Information about notes for a contact evaluation.

## Contents
<a name="API_EvaluationNote_Contents"></a>

 ** Value **   <a name="connect-Type-EvaluationNote-Value"></a>
The note for an item (section or question) in a contact evaluation.
Even though a note in an evaluation can have up to 3072 chars, there is also a limit on the total number of chars for all the notes in the evaluation combined. Assuming there are N questions in the evaluation being submitted, then the max char limit for all notes combined is N x 1024.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Required: No

## See Also
<a name="API_EvaluationNote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationNote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationNote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationNote)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
