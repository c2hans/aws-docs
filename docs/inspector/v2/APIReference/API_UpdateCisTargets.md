---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCisTargets.html
---

# UpdateCisTargets
<a name="API_UpdateCisTargets"></a>

Updates CIS targets.

## Contents
<a name="API_UpdateCisTargets_Contents"></a>

 ** accountIds **   <a name="inspector2-Type-UpdateCisTargets-accountIds"></a>
The target account ids.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Pattern: `\d{12}|ALL_ACCOUNTS|SELF`
Required: No

 ** targetResourceTags **   <a name="inspector2-Type-UpdateCisTargets-targetResourceTags"></a>
The target resource tags.
Type: String to array of strings map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=\-@]*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_UpdateCisTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateCisTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateCisTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateCisTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
