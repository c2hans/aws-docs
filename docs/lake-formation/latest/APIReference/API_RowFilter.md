---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RowFilter.html
---

# RowFilter
<a name="API_RowFilter"></a>

A PartiQL predicate.

## Contents
<a name="API_RowFilter_Contents"></a>

 ** AllRowsWildcard **   <a name="lakeformation-Type-RowFilter-AllRowsWildcard"></a>
A wildcard for all rows.
Type: [AllRowsWildcard](API_AllRowsWildcard.md) object
Required: No

 ** FilterExpression **   <a name="lakeformation-Type-RowFilter-FilterExpression"></a>
A filter expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_RowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RowFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RowFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RowFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
