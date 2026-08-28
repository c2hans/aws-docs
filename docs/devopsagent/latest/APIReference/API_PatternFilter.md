---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PatternFilter.html
---

# PatternFilter
<a name="API_PatternFilter"></a>

A regex-based match condition. Passes when the value matches any pattern.

## Contents
<a name="API_PatternFilter_Contents"></a>

 ** patterns **   <a name="devopsagent-Type-PatternFilter-patterns"></a>
Anchored full-match regex patterns. The condition passes when the value matches at least one pattern.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x1F\x7F-\x9F]+`
Required: Yes

## See Also
<a name="API_PatternFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PatternFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PatternFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PatternFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
