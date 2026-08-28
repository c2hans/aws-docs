---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkspacePage.html
---

# WorkspacePage
<a name="API_WorkspacePage"></a>

Contains information about a page configuration in a workspace, including the view assigned to the page.

## Contents
<a name="API_WorkspacePage_Contents"></a>

 ** InputData **   <a name="connect-Type-WorkspacePage-InputData"></a>
A JSON string containing input parameters passed to the view when the page is rendered.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** Page **   <a name="connect-Type-WorkspacePage-Page"></a>
The page identifier. System pages include `HOME` and `AGENT_EXPERIENCE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^(?!\\.$)(?!\\.\\.$)[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]+$`
Required: No

 ** ResourceArn **   <a name="connect-Type-WorkspacePage-ResourceArn"></a>
The Amazon Resource Name (ARN) of the view associated with this page.
Type: String
Required: No

 ** Slug **   <a name="connect-Type-WorkspacePage-Slug"></a>
The URL-friendly identifier for the page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `^$|^[\\p{L}\\p{Z}\\p{N}\\-_.:=@'|]{3,}$`
Required: No

## See Also
<a name="API_WorkspacePage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkspacePage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkspacePage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkspacePage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
