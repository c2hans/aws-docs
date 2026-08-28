---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ToolSummary.html
---

# ToolSummary
<a name="API_ToolSummary"></a>

Information about the Diagnostic Tool.

## Contents
<a name="API_ToolSummary_Contents"></a>

 ** description **   <a name="diagnostictools-Type-ToolSummary-description"></a>
Description the Diagnostic Tool.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: Yes

 ** id **   <a name="diagnostictools-Type-ToolSummary-id"></a>
Unique Identifier for Diagnostic Tool.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `\w+`
Required: Yes

 ** latestVersionId **   <a name="diagnostictools-Type-ToolSummary-latestVersionId"></a>
Version Identifier associated to the latest version of Diagnostic Tool
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: Yes

 ** name **   <a name="diagnostictools-Type-ToolSummary-name"></a>
Describes the Diagnostic Tool Name.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 256.
Pattern: `[\ \w]+`
Required: Yes

 ** usedFor **   <a name="diagnostictools-Type-ToolSummary-usedFor"></a>
List of use cases where these Diagnostic Tool can be used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: Yes

## See Also
<a name="API_ToolSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/ToolSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/ToolSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/ToolSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Diagnostic Tools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query diagnostic-tools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
