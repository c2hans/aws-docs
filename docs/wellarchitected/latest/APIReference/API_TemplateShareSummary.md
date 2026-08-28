---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TemplateShareSummary.html
---

# TemplateShareSummary
<a name="API_TemplateShareSummary"></a>

Summary of a review template share.

## Contents
<a name="API_TemplateShareSummary_Contents"></a>

 ** SharedWith **   <a name="wellarchitected-Type-TemplateShareSummary-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: No

 ** ShareId **   <a name="wellarchitected-Type-TemplateShareSummary-ShareId"></a>
The ID associated with the share.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Status **   <a name="wellarchitected-Type-TemplateShareSummary-Status"></a>
The status of the share request.
Type: String
Valid Values: `ACCEPTED | REJECTED | PENDING | REVOKED | EXPIRED | ASSOCIATING | ASSOCIATED | FAILED`
Required: No

 ** StatusMessage **   <a name="wellarchitected-Type-TemplateShareSummary-StatusMessage"></a>
Review template share invitation status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_TemplateShareSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/TemplateShareSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/TemplateShareSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/TemplateShareSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
