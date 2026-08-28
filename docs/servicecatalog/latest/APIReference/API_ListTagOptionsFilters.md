---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListTagOptionsFilters.html
---

# ListTagOptionsFilters
<a name="API_ListTagOptionsFilters"></a>

Filters to use when listing TagOptions.

## Contents
<a name="API_ListTagOptionsFilters_Contents"></a>

 ** Active **   <a name="servicecatalog-Type-ListTagOptionsFilters-Active"></a>
The active state.
Type: Boolean
Required: No

 ** Key **   <a name="servicecatalog-Type-ListTagOptionsFilters-Key"></a>
The TagOption key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Value **   <a name="servicecatalog-Type-ListTagOptionsFilters-Value"></a>
The TagOption value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ListTagOptionsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListTagOptionsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListTagOptionsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListTagOptionsFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
