---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TagValues.html
---

# TagValues
<a name="API_budgets_TagValues"></a>

The values that are available for a tag.

## Contents
<a name="API_budgets_TagValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-budgets_TagValues-Key"></a>
The key for the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-budgets_TagValues-MatchOptions"></a>
The match options that you can use to filter your results.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

 ** Values **   <a name="awscostmanagement-Type-budgets_TagValues-Values"></a>
The specific value of the tag.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_budgets_TagValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/TagValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/TagValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/TagValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
