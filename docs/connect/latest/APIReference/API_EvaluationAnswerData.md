---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationAnswerData.html
---

# EvaluationAnswerData
<a name="API_EvaluationAnswerData"></a>

Information about answer data for a contact evaluation. Answer data must be either string, numeric, or not applicable.

## Contents
<a name="API_EvaluationAnswerData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DateTimeValue **   <a name="connect-Type-EvaluationAnswerData-DateTimeValue"></a>
Date and time value provided as an answer to an evaluation question.
Type: String
Required: No

 ** NotApplicable **   <a name="connect-Type-EvaluationAnswerData-NotApplicable"></a>
The flag to mark the question as not applicable.
Type: Boolean
Required: No

 ** NumericValue **   <a name="connect-Type-EvaluationAnswerData-NumericValue"></a>
The numeric value for an answer in a contact evaluation.
Type: Double
Required: No

 ** StringValue **   <a name="connect-Type-EvaluationAnswerData-StringValue"></a>
The string value for an answer in a contact evaluation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

 ** StringValues **   <a name="connect-Type-EvaluationAnswerData-StringValues"></a>
String values provided as answers to evaluation questions.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

## See Also
<a name="API_EvaluationAnswerData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationAnswerData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationAnswerData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationAnswerData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
