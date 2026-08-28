---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_StringSearch.html
---

# StringSearch
<a name="API_StringSearch"></a>

 A structure that defines string search parameters.

## Contents
<a name="API_StringSearch_Contents"></a>

 ** SearchOption **   <a name="billingconductor-Type-StringSearch-SearchOption"></a>
 The search option to be applied when performing the string search.
Type: String
Valid Values: `STARTS_WITH`
Required: Yes

 ** SearchValue **   <a name="billingconductor-Type-StringSearch-SearchValue"></a>
 The value to search for within the specified string field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@ ]+`
Required: Yes

## See Also
<a name="API_StringSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/StringSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/StringSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/StringSearch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
