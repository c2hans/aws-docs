---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchTermFilterExpression.html
---

# SearchTermFilterExpression
<a name="API_SearchTermFilterExpression"></a>

Searches for a particular search term.

## Contents
<a name="API_SearchTermFilterExpression_Contents"></a>

 ** searchTerm **   <a name="deadlinecloud-Type-SearchTermFilterExpression-searchTerm"></a>
The term to search for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** matchType **   <a name="deadlinecloud-Type-SearchTermFilterExpression-matchType"></a>
Specifies how Deadline Cloud matches your search term in the results. If you don't specify a `matchType` the default is `FUZZY_MATCH`.
+  `FUZZY_MATCH` - Matches if a portion of the search term is found in the result.
+  `CONTAINS` - Matches if the exact search term is contained in the result.
Type: String
Valid Values: `FUZZY_MATCH | CONTAINS`
Required: No

## See Also
<a name="API_SearchTermFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchTermFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchTermFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchTermFilterExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
