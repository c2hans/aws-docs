---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

A tag key-value pair used for resource discovery.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** key **   <a name="ngresiliencehub-Type-ResourceTag-key"></a>
Tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\x00-\x1f\x22]+`
Required: Yes

 ** values **   <a name="ngresiliencehub-Type-ResourceTag-values"></a>
The list of tag values.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\x00-\x1f\x22]*`
Required: Yes

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ResourceTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
