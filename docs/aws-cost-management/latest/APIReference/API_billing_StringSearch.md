---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_StringSearch.html
---

# StringSearch
<a name="API_billing_StringSearch"></a>

 A structure that defines how to search for string values. You can specify a search option and the value to search for.

## Contents
<a name="API_billing_StringSearch_Contents"></a>

 ** searchOption **   <a name="awscostmanagement-Type-billing_StringSearch-searchOption"></a>
 The type of search operation to perform on the string value. Determines how the search value is matched against the target field.
Type: String
Valid Values: `STARTS_WITH`
Required: Yes

 ** searchValue **   <a name="awscostmanagement-Type-billing_StringSearch-searchValue"></a>
 The string value to use in the search operation. This value is compared against the target field using the specified search option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@ ]+`
Required: Yes

## See Also
<a name="API_billing_StringSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/StringSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/StringSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/StringSearch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
