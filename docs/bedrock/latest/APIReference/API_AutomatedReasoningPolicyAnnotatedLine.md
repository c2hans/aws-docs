---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyAnnotatedLine.html
---

# AutomatedReasoningPolicyAnnotatedLine
<a name="API_AutomatedReasoningPolicyAnnotatedLine"></a>

Represents a single line of text from a source document, annotated with its line number for precise referencing.

## Contents
<a name="API_AutomatedReasoningPolicyAnnotatedLine_Contents"></a>

 ** lineNumber **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotatedLine-lineNumber"></a>
The line number of this text within the source document.
Type: Integer
Required: No

 ** lineText **   <a name="bedrock-Type-AutomatedReasoningPolicyAnnotatedLine-lineText"></a>
The actual text content of this line from the source document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyAnnotatedLine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotatedLine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotatedLine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAnnotatedLine)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
