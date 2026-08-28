---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningLogicStatement.html
---

# AutomatedReasoningLogicStatement
<a name="API_AutomatedReasoningLogicStatement"></a>

Represents a logical statement that can be expressed both in formal logic notation and natural language, providing dual representations for better understanding and validation.

## Contents
<a name="API_AutomatedReasoningLogicStatement_Contents"></a>

 ** logic **   <a name="bedrock-Type-AutomatedReasoningLogicStatement-logic"></a>
The formal logic representation of the statement using mathematical notation and logical operators.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** naturalLanguage **   <a name="bedrock-Type-AutomatedReasoningLogicStatement-naturalLanguage"></a>
The natural language representation of the logical statement, providing a human-readable interpretation of the formal logic.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_AutomatedReasoningLogicStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningLogicStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningLogicStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningLogicStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
