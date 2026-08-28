---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSnippetResult.html
---

# CodeSnippetResult
<a name="API_CodeSnippetResult"></a>

Contains information on a code snippet retrieved by Amazon Inspector from a code vulnerability finding.

## Contents
<a name="API_CodeSnippetResult_Contents"></a>

 ** codeSnippet **   <a name="inspector2-Type-CodeSnippetResult-codeSnippet"></a>
Contains information on the retrieved code snippet.
Type: Array of [CodeLine](API_CodeLine.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** endLine **   <a name="inspector2-Type-CodeSnippetResult-endLine"></a>
The line number of the last line of a code snippet.
Type: Integer
Required: No

 ** findingArn **   <a name="inspector2-Type-CodeSnippetResult-findingArn"></a>
The ARN of a finding that the code snippet is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: No

 ** startLine **   <a name="inspector2-Type-CodeSnippetResult-startLine"></a>
The line number of the first line of a code snippet.
Type: Integer
Required: No

 ** suggestedFixes **   <a name="inspector2-Type-CodeSnippetResult-suggestedFixes"></a>
Details of a suggested code fix.
Type: Array of [SuggestedFix](API_SuggestedFix.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_CodeSnippetResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSnippetResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSnippetResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSnippetResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
