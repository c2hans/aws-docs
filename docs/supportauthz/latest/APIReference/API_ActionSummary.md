---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ActionSummary.html
---

# ActionSummary
<a name="API_ActionSummary"></a>

A summary of a support action.

## Contents
<a name="API_ActionSummary_Contents"></a>

 ** action **   <a name="supportauthorization-Type-ActionSummary-action"></a>
The name of the support action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-z][a-z0-9-]*:[A-Za-z0-9_.-]+`
Required: Yes

 ** description **   <a name="supportauthorization-Type-ActionSummary-description"></a>
A description of what the support action does.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: Yes

 ** service **   <a name="supportauthorization-Type-ActionSummary-service"></a>
The AWS service associated with the support action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## See Also
<a name="API_ActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/ActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/ActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/ActionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
