---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ToolVersion.html
---

# ToolVersion
<a name="API_ToolVersion"></a>

Information about the specific Diagnostic Tool Version.

## Contents
<a name="API_ToolVersion_Contents"></a>

 ** description **   <a name="diagnostictools-Type-ToolVersion-description"></a>
Version description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: Yes

 ** parametersSchema **   <a name="diagnostictools-Type-ToolVersion-parametersSchema"></a>
Diagnostic Tool input parameter schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32764.
Required: Yes

 ** usedFor **   <a name="diagnostictools-Type-ToolVersion-usedFor"></a>
List of use cases where these Diagnostic Tool can be used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: Yes

 ** versionId **   <a name="diagnostictools-Type-ToolVersion-versionId"></a>
Version Identifier associated to specific version of Diagnostic Tool artifact.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: Yes

 ** labels **   <a name="diagnostictools-Type-ToolVersion-labels"></a>
Additional Diagnostic Tool metadata.
Type: Array of strings
Valid Values: `GLOBAL_TOOL`
Required: No

## See Also
<a name="API_ToolVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/ToolVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/ToolVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/ToolVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Diagnostic Tools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query diagnostic-tools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
